import importlib.util
from pathlib import Path
import sqlite3
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build', ROOT / 'build.py')
build = importlib.util.module_from_spec(spec)
spec.loader.exec_module(build)


class BuildTests(unittest.TestCase):
    def test_no_tm_output_from_other_directory_is_reproducible(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / 'new.dic'
            command = [sys.executable, str(ROOT / 'build.py'), '--no-tm', '--output', str(output)]
            subprocess.run(command, cwd=folder, check=True, capture_output=True)
            self.assertEqual(output.read_bytes(), (ROOT / 'sv_SE.dic').read_bytes())
            subprocess.run(command, cwd=folder, check=True, capture_output=True)
            self.assertEqual(output.read_bytes(), (ROOT / 'sv_SE.dic').read_bytes())

    def test_repairs_count_duplicates_and_missing_final_newline(self):
        with tempfile.TemporaryDirectory() as folder:
            base, output, db = [Path(folder) / x for x in ('base.dic', 'out.dic', 'tm.db')]
            base.write_text('99\nUbuntu/XY\nord/AB\nord/AB\n', encoding='utf-8')
            with sqlite3.connect(db) as conn:
                conn.execute('CREATE TABLE translation_memory (target TEXT)')
                conn.execute('INSERT INTO translation_memory VALUES (?)', ('smörgås smörgås',))
            base.write_text(base.read_text().rstrip('\n'), encoding='utf-8')
            subprocess.run([sys.executable, str(ROOT / 'build.py'), '--base', str(base),
                            '--output', str(output), '--tm-db', str(db), '--min-count', '2'],
                           check=True, capture_output=True)
            self.assertEqual(output.read_text(), '3\nUbuntu/XY\nord/AB\nsmörgås/XY\n')

    def test_missing_database_preserves_output(self):
        with tempfile.TemporaryDirectory() as folder:
            output = Path(folder) / 'out.dic'
            output.write_text('keep me')
            result = subprocess.run([sys.executable, str(ROOT / 'build.py'), '--output', str(output),
                                     '--tm-db', str(Path(folder) / 'absent.db')], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertEqual(output.read_text(), 'keep me')
            self.assertFalse((Path(folder) / 'absent.db').exists())

    def test_checker_failure_propagates(self):
        with patch.object(build.subprocess, 'run', side_effect=subprocess.CalledProcessError(1, 'hunspell')):
            with self.assertRaises(subprocess.CalledProcessError):
                build.check_hunspell({'ord'}, '/missing/dictionary')

    @unittest.skipUnless(shutil.which('hunspell'), 'Hunspell is required')
    def test_spelling_in_both_dictionaries(self):
        good = {'dator', 'översättning', 'stavningskontroll', 'programvara',
                'inställningar', 'användargränssnitt', 'filhanterare',
                'säkerhetskopia', 'operativsystem', 'webbläsare',
                'lösenfras', 'meddelandekö', 'symlänk', 'filbläddrare',
                'åsidosättning', 'fjärrvärd', 'trädvy', 'skogshuggartält',
                'datakällobjekt', 'vertexfärg'}
        bad = {'zzqxxzz', 'stavvningskontroll'}
        for name in ('sv_SE', 'sv_SE_expanded'):
            with self.subTest(dictionary=name):
                self.assertEqual(build.check_hunspell(good | bad, ROOT / name), bad)

    def test_dictionary_counts_and_exact_duplicates(self):
        for filename in ('sv_SE.dic', 'sv_SE_expanded.dic'):
            with self.subTest(filename=filename):
                lines = (ROOT / filename).read_text().splitlines()
                self.assertEqual(int(lines[0]), len(lines) - 1)
                self.assertNotIn('', lines[1:])
                self.assertEqual(len(lines) - 1, len(set(lines[1:])))


if __name__ == '__main__':
    unittest.main()
