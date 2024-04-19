
# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# Time complexity - O(n)
# Space complexity - O(1)


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        
        for i in range(len(s)):
            s = s[1:]+s[0]
            if s == goal:
                return True
