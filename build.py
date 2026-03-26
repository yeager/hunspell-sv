#!/usr/bin/env python3
"""Build sv_SE.dic from SFOL base + translation memory additions."""

import argparse
import subprocess
import re
from pathlib import Path
from collections import Counter

def load_dic(path):
    """Load a hunspell .dic file, return set of lowercase words."""
    words = set()
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    for line in lines[1:]:
        word = line.strip().split('/')[0].lower()
        if word:
            words.add(word)
    return words, lines

def extract_tm_words(db_path, min_count=5):
    """Extract Swedish words from translation memory database."""
    import sqlite3
    conn = sqlite3.connect(db_path)
    rows = conn.execute("SELECT target FROM translation_memory WHERE target != ''").fetchall()
    conn.close()
    
    all_words = Counter()
    for row in rows:
        words = re.findall(r'\b[a-zåäöA-ZÅÄÖ]{4,}\b', row[0])
        for w in words:
            all_words[w.lower()] += 1
    
    return {w: c for w, c in all_words.items() if c >= min_count}

def check_hunspell(words, dic_path):
    """Check which words hunspell doesn't know."""
    word_list = sorted(words)
    misspelled = set()
    for i in range(0, len(word_list), 5000):
        batch = word_list[i:i+5000]
        r = subprocess.run(["hunspell", "-d", str(dic_path), "-l"],
            input='\n'.join(batch), capture_output=True, text=True, timeout=30)
        for w in r.stdout.strip().split('\n'):
            if w.strip():
                misspelled.add(w.strip())
    return misspelled

def main():
    parser = argparse.ArgumentParser(description='Build Swedish hunspell dictionary')
    parser.add_argument('--tm-db', default='~/.openclaw/data/translation-memory.db',
                       help='Path to translation memory database')
    parser.add_argument('--min-count', type=int, default=5,
                       help='Minimum TM occurrences to include a word')
    parser.add_argument('--output', default='sv_SE.dic',
                       help='Output dictionary file')
    args = parser.parse_args()
    
    tm_db = Path(args.tm_db).expanduser()
    tm_words = {}
    
    # Try to extract TM words (optional step)
    try:
        if not tm_db.exists():
            print(f"Warning: TM database not found: {tm_db}")
            print("Building dictionary from SFOL base only...")
        else:
            print("Extracting words from TM...")
            tm_words = extract_tm_words(str(tm_db), args.min_count)
            print(f"  Found {len(tm_words)} words with ≥{args.min_count} occurrences")
    except Exception as e:
        print(f"Warning: Failed to extract TM words: {e}")
        print("Building dictionary from SFOL base only...")
        tm_words = {}
    
    # Load current dictionary
    existing, lines = load_dic(args.output)
    print(f"  Current dictionary: {len(existing)} unique words")
    
    # Find new words
    swedish_chars = set('åäöÅÄÖ')
    new_words = []
    for w, c in tm_words.items():
        if w not in existing and any(ch in swedish_chars for ch in w):
            if len(w) >= 5 and re.match(r'^[a-zåäö-]+$', w):
                new_words.append((w, c))
    
    print(f"  New Swedish words to add: {len(new_words)}")
    
    # Append
    count = int(lines[0].strip()) + len(new_words)
    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(f"{count}\n")
        for line in lines[1:]:
            f.write(line)
        for w, c in sorted(new_words):
            f.write(f"{w}/XY\n")
    
    print(f"  Written: {count} entries to {args.output}")

if __name__ == '__main__':
    main()
