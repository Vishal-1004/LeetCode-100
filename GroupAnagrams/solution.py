class Solution:
    '''let us concider an example 
    ["eat","tea","tan","ate","nat","bat"], here we are planning to create a dictionary where the sorted string is the key and the value will be an array which contains the original string which will be same as that of the key if sorted that is
    ansDict = {
    'aet': ['eat','tea','ate'],
    'ant': ['tan','nat'],
    'abt': ['bat']
    }  
    here we will run a for loop throught the array and will sort every string and check whether the string is there in the dict or not 
    if the sorted string is their in the dict then append the original string in the array as done below and if not there then create an empty array as the value for the given sorted string as its key.'''
    def groupAnagrams(self, strs):
        ansDict = {}

        for i in strs:
            sortedStirng = sorted(i)

            '''if the sorted string is not available in the dict as a key then create one key value pair for it with value as an empty array for the given key'''
            if sortedStirng not in ansDict:
                ansDict[sortedStirng] = []

            '''and here every string "i" has to appended in the value array of its sorted string key'''
            ansDict[sortedStirng].append(i)

        '''finally all the values fo the dict will be returned as a list '''
        return list(ansDict.values())