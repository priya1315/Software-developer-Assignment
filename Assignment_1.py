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

if __name__ == "__main__":
    test_str = "String; 2be reversed..."
    expected = "gnirtS; eb2 desrever..."
    result = Solution.reverse_words(test_str)
    assert result == expected, f"Got {result}, expected {expected}"
    print("Test passed!")

