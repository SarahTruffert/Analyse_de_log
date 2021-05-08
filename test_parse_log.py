import unittest
from parse_log import convertir_minutes, percentage, tri_dico

class TestParseLog(unittest.TestCase):
    def test_convertir_minutes(self):
        self.assertEqual(convertir_minutes("09:37", "10:40"), 63)
        self.assertEqual(type(convertir_minutes("09:37", "10:40")), int)
        self.assertIsNotNone(convertir_minutes("09:37", "10:40"))

    def test_percentage(self):
        self.assertEqual(percentage(65, 100, 970), 6.701030927835052)
        self.assertEqual(type(percentage(65, 100, 970)), float)

    def test_tri_dico(self):
        self.assertIsInstance(tri_dico({'Dictionaries': 15, 'Break': 65, 'Exercices': 340}), list)