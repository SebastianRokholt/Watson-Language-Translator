import unittest
from translator import french_to_english, english_to_french


# Testing the frenchToEnglish function
class TestF2E(unittest.TestCase):
    def test1(self):
        # test for null input
        self.assertIsNone(french_to_english())
        # Test for the translation of the world 'Hello' and 'Bonjour'.
        self.assertEqual(french_to_english("Bonjour"), "Hello")

# Testing the englishToFrench function
class TestE2F(unittest.TestCase):
    def test1(self):
        # test for null input
        self.assertIsNone(english_to_french())
        # Test for the translation of the world 'Hello' and 'Bonjour'.
        self.assertEqual(english_to_french("Hello"), "Bonjour")


# Run unit tests
if __name__ == "__main__":
    unittest.main()
