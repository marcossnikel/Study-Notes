# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
# A subsequence of a string is a new string that is formed from the original string by 
# deleting some (can be none) of the characters without disturbing the relative positions of the 
# remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

class Solution(object):
    def isSubsequence(self, sequence, array):
        sequenceIdx = 0
        arrayIdx = 0

        sequenceLen = len(sequence)
        arrayLen = len(array)

        while sequenceIdx < sequenceLen and arrayIdx < arrayLen:
            if sequence[sequenceIdx] == array[arrayIdx]:
                sequenceIdx = sequenceIdx + 1
            arrayIdx = arrayIdx + 1
            
        return sequenceIdx == sequenceLen



