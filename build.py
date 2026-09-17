#!/usr/bin/env python3
"""Extend the checked-in Swedish dictionary with translation-memory candidates."""

import argparse
from collections import Counter
from pathlib import Path
import re
import sqlite3
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parent


def load_dic(path):
    """Read entries without changing case, flags or morphology data."""
    lines = Path(path).read_text(encoding='utf-8').splitlines()
    if not lines or not lines[0].isdigit():
        raise ValueError(f'{path}: missing numeric entry count')
    entries = list(dict.fromkeys(line for line in lines[1:] if line.strip()))
    words = {line.split('\t')[0].split('/')[0].lower() for line in entries}
    return words, [str(len(entries)) + '\n'] + [line + '\n' for line in entries]


def extract_tm_words(db_path, min_count=5):
    """Count Swedish word occurrences, streaming a read-only database."""
    uri = Path(db_path).resolve().as_uri() + '?mode=ro'
    conn = sqlite3.connect(uri, uri=True)
    try:
        all_words = Counter()
        for (target,) in conn.execute("SELECT target FROM translation_memory WHERE target != ''"):
            all_words.update(w.lower() for w in re.findall(r'\b[a-zåäöA-ZÅÄÖ]{4,}\b', target))
        return {w: c for w, c in all_words.items() if c >= min_count}
    finally:
        conn.close()


def check_hunspell(words, dic_path):
    """Return unknown words; a failed checker must not look like success."""
    word_list = sorted(words)
    misspelled = set()
    for i in range(0, len(word_list), 5000):
        result = subprocess.run(
            ['hunspell', '-i', 'UTF-8', '-d', str(dic_path), '-p', '/dev/null', '-l'],
            input='\n'.join(word_list[i:i + 5000]) + '\n',
            capture_output=True, text=True, encoding='utf-8', timeout=30, check=True)
        misspelled.update(result.stdout.splitlines())
    return misspelled


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--tm-db', default='~/.openclaw/data/translation-memory.db')
    parser.add_argument('--no-tm', action='store_true', help='Skip translation memory')
    parser.add_argument('--min-count', type=int, default=5)
    parser.add_argument('--base', type=Path, default=ROOT / 'sv_SE.dic',
                        help='Input dictionary (defaults to the checked-in dictionary)')
    parser.add_argument('--output', type=Path, default=ROOT / 'sv_SE.dic')
    args = parser.parse_args()
    if args.min_count < 1:
        parser.error('--min-count must be positive')

    existing, lines = load_dic(args.base)
    tm_words = {}
    if not args.no_tm:
        tm_db = Path(args.tm_db).expanduser()
        if not tm_db.is_file():
            parser.error(f'TM database not found: {tm_db}; use --no-tm to skip it')
        tm_words = extract_tm_words(tm_db, args.min_count)

    # Preserve the existing conservative candidate heuristic. Frequency alone
    # does not establish correct spelling; review additions before publishing.
    new_words = sorted(w for w in tm_words if w not in existing
                       and any(ch in 'åäö' for ch in w) and len(w) >= 5
                       and re.fullmatch(r'[a-zåäö-]+', w))
    entries = lines[1:] + [w + '/XY\n' for w in new_words]
    content = str(len(entries)) + '\n' + ''.join(entries)
    # Keep existing file permissions and leave the original intact on failure.
    mode = args.output.stat().st_mode & 0o777 if args.output.exists() else 0o644
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', dir=args.output.parent,
                                         delete=False) as stream:
            temporary = Path(stream.name)
            stream.write(content)
        temporary.chmod(mode)
        temporary.replace(args.output)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()
    print(f'Written {len(entries)} entries ({len(new_words)} new) to {args.output}')


if __name__ == '__main__':
    main()
