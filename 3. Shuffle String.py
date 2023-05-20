#https://leetcode.com/problems/shuffle-string/
class Solution(object):
    def restoreString(self, s, indices):
        
        #Create a list with same length and indices
        n = len(s)
        result = ['']*n
        
        for i in range(n):
            result[indices[i]] = s[i]
            
        return ''.join(result)
