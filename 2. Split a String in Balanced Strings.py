#https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution(object):
    def balancedStringSplit(self, s):
        counter = 0
        result = 0
        for char in s:
            
            if char == 'R':
                counter += 1
            else:
                counter -= 1
            
            if counter == 0:
                result += 1
            
        return result
        
