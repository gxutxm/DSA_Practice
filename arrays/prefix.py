'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        
        if not strs:
            return ""
        shortest_word = strs[0]    

        for word in strs:
            if len(word) < len(shortest_word):
                shortest_word = word

        for index in range(len(shortest_word)):
            for word in strs:
                if word[index] != shortest_word[index]:
                    return shortest_word[:index]
        return shortest_word    