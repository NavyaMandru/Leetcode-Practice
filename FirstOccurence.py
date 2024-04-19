# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Time complexity - O(n)
# Space complexity - O(1)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not haystack.__contains__(needle):
            return -1
        else:
            return haystack.find(needle)
