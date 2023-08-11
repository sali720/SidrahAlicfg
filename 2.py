import unittest
from sid import is_pangram  # Import the function you want to test

class TestIsPangram(unittest.TestCase):

    def test_empty_string(self):
        # An empty string shouldn't be a pangram
        result = is_pangram("")
        self.assertFalse(result)

    def test_lowercase_pangram(self):
        # A lowercase pangram is still a valid pangram
        result = is_pangram("the quick brown fox jumps over the lazy dog")
        self.assertTrue(result)

    def test_uppercase_pangram(self):
        # An uppercase pangram is a valid pangram
        result = is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG")
        self.assertTrue(result)

    def test_mixed_case_pangram(self):
        # A mixed-case pangram is still a valid pangram
        result = is_pangram("ThE QuiCk BrOwN FoX JuMpS OvEr ThE LaZy DoG")
        self.assertTrue(result)

    def test_non_pangram(self):
        # A string missing some letters should not be considered a pangram
        result = is_pangram("The quick brown fox jumps over the lazy cat")
        self.assertFalse(result)

    def test_empty_alphabet(self):
        # An empty input string should not be a pangram
        result = is_pangram("hello world")
        self.assertFalse(result)

    def test_special_characters(self):
        # Special characters should not affect the pangram check
        result = is_pangram("The quick brown fox jumps over the lazy dog!!")
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()
