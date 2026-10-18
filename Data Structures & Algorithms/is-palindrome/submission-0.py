class Solution:
    def isPalindrome(self, s: str) -> bool:
        glued = "".join(char.lower() for char in s if  char.isalnum())
        if glued == glued[::-1]:
            return True
        else:
            return False