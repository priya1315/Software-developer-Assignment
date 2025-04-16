import unittest
class Solution:
    def reverse_words(sentence):
        s = list(sentence)
        start = -1

        for i in range(len(sentence) + 1):
            if i < len(sentence) and sentence[i].isalnum():
                if start == -1:
                    start = i
            elif start != -1:
                reverse = i - 1
                while start < reverse:
                    s[start], s[reverse] = s[reverse], s[start]
                    start += 1
                    reverse -= 1
                start = -1
        return ''.join(s)

class TestReverseWords(unittest.TestCase):

    def test_empty_string(self):
        sentence = ""
        expected = ""
        self.assertEqual(Solution.reverse_words(sentence),expected)

    def test_special_chara_only(self):
        sentence = "!@#,%"
        expected = "!@#,%"
        self.assertEqual(Solution.reverse_words(sentence),expected)

    def test_starts_with_space(self):
        sentence = " TestingString123"
        expected = " 321gnirtSgnitseT"
        self.assertEqual(Solution.reverse_words(sentence),expected)

    def test_ends_with_space(self):
        sentence = "TestingString123 "
        expected = "321gnirtSgnitseT "
        self.assertEqual(Solution.reverse_words(sentence),expected)
if __name__ == '__main__':
    unittest.main()
