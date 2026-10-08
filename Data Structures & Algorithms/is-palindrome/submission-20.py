class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = 0
        d = len(s) - 1

        while c < d:
            if not s[c].isalnum():
                c += 1
                continue

            if not s[d].isalnum():
                d -= 1
                continue

            if s[c].lower() != s[d].lower():
                return False

            c += 1
            d -= 1

        return True