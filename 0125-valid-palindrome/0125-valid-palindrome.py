class Solution:
    def isPalindrome(self, s: str) -> bool:
        tmp = []
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                tmp.append(letter.lower())
        
        if tmp == list(reversed(tmp)):
            return True
        return False