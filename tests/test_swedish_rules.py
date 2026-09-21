"""Check reviewed word forms directly; grammar/style examples are not scored."""
import ctypes
import ctypes.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class SwedishRulesTests(unittest.TestCase):
    def check_words(self, dictionary, cases):
        library = ctypes.util.find_library('hunspell-1.7')
        self.assertIsNotNone(library, 'libhunspell-1.7 is required')
        lib = ctypes.CDLL(library)
        lib.Hunspell_create.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
        lib.Hunspell_create.restype = ctypes.c_void_p
        lib.Hunspell_spell.argtypes = [ctypes.c_void_p, ctypes.c_char_p]
        lib.Hunspell_spell.restype = ctypes.c_int
        lib.Hunspell_destroy.argtypes = [ctypes.c_void_p]
        lib.Hunspell_destroy.restype = None
        handle = lib.Hunspell_create(str(ROOT/(dictionary+'.aff')).encode(),
                                     str(ROOT/(dictionary+'.dic')).encode())
        self.assertTrue(handle)
        try:
            for word, expected in cases:
                with self.subTest(dictionary=dictionary, word=word):
                    self.assertEqual(bool(lib.Hunspell_spell(handle, word.encode())), expected)
        finally:
            lib.Hunspell_destroy(handle)

    def test_sourced_word_cases(self):
        corpus = json.loads((ROOT/'tests/swedish-rules.json').read_text())
        self.check_words('sv_SE', [(c['text'], c['expected_accept']) for c in corpus['cases']
                                   if c['scope'] == 'word'])

    def test_corrections_and_neuter_paradigm(self):
        corrections = json.loads((ROOT/'lexical-corrections.json').read_text())['corrections']
        cases = [(c['word'], False) for c in corrections]
        cases += [(c['replacement'], True) for c in corrections]
        cases += [(w, True) for w in ('enspann', 'enspanns', 'enspannet', 'enspannets',
                                      'enspannen', 'enspannens')]
        for dictionary in ('sv_SE', 'sv_SE_expanded'):
            self.check_words(dictionary, cases)


if __name__ == '__main__':
    unittest.main()
