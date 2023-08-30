import heapq
class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        '''First we will split the given string into an array where we will be keeping all the words used in the string separately'''
        ansString = ""
        useDict ={}
        useArr = list(map(str,text.split()))
        #print(useArr)

        '''Now we will create a dictionary and group words of same lengths in one i.e if the string is "Hi i am vishal" then the dictionary will be {2:['Hi','am'],1:['i'],6:['vishal']}.'''
        for i in useArr:
            if len(i) not in useDict:
                useDict[len(i)] = []
            useDict[len(i)].append(i)

        #print(useDict)
        '''Now we will create a heap and push all these value into it and our min heap will automatically sort the dictionary based on its length. Here in heap we will be storing a tuple whose first element will be the length of the words and the second element will the array of words of the given length.'''
        heap = []
        for length,words in useDict.items():
            heapq.heappush(heap,(length,words))

        '''Now we will pop out the top tuples from the heap one by one and if the word which we are going to add in the ansString is our first words so then we capatalize it else we add that word with all its letters in lower case. For doing so we have used some variable and some inbuilt functions as you can see below.'''
        start = True
        while len(heap) != 0:
            length,wordArr = heapq.heappop(heap)

            if start == True:
                element = 1
                for i in wordArr:
                    if element == 1:
                        ansString += i.capitalize()
                        ansString += " "
                        element += 1
                    else:
                        ansString += i.lower()
                        ansString += " "
            
                start = False
            else:
                for i in wordArr:
                    ansString += i.lower()
                    ansString += " "

        #print(len(ansString))
        '''One more thing to note is that after adding every word in the ansString we also have to add space " ", but while returing the ansString we slice the string in such a way that the last space " " we have added in not displayed as shown below.'''
        return ansString[:len(ansString)-1]


