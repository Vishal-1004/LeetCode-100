class Solution(object):
    def maxProduct(self, words):
        '''this function takes two array as input and runs a for loop along then, if at any point the values turns out to be True for both the arrays at the same index then we will return True which indicates that both the arrays have a letter in common and hence cannot be used to finding maximum product, else we will return False'''
        def common(chars1, chars2):
            for c1, c2 in zip(chars1, chars2):
                if c1 and c2: return True
            return False
        
        '''creating arrays which contains 26 false values to represent all 26 letters of alphabets, this array is created for every word in present in the list [words].chars is a 2D array.'''
        chars, ans = [[False]*26 for i in range(len(words))], 0

        '''here enumerate will assign a key:value pari to all the words in such a way that i = index (key) and word = each word in the list words (value)'''
        for i, word in enumerate(words):
            '''now for every word we assign True to all the characters which has appeared in the word in the chars array which we have created'''
            for ch in word:
                chars[i][ord(ch) - ord('a')] = True
            
            '''since i represent an index number so we run a for loop till i and if both the word at ith and jth index donot have anything in common then we find the max product length and update the ans value.'''
            for j in range(i):
                if not common(chars[i], chars[j]):
                    ans = max(ans, len(words[i]) * len(words[j]))
        return ans