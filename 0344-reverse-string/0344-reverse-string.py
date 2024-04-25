class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s)-1
        while True:
            if start >= end:
                break
            tmp = s[start]
            s[start] = s[end]
            s[end] = tmp
            start += 1
            end -= 1
        