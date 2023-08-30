class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        '''
        Lets take an example: People = [1, 1, 2, 3, 9, 10, 11, 12] and Limit = 12
        Since we want to minimise the number of boats used, we must try to form pair of largest and smallest numbers to fit them into one boat if possible. Taking two smaller weight people and adding them to one boat might waste some precious space.

        Now we can see that as 12 tries to form a pair. Logically being the largest number it should start from the smallest. So it goes to 1's, then 2 then 3 and so on to form a pair. Now one thing to note is that if 12 cannot form a pair with the smallest number(that is 1), then there is no point looking forward to 2, 3 ... as it is certain that numbers beyond 1 will be equal to or larger than 1 and will definitely exceed the boats rated capacity if it did with 1 in the first place.
        
        Thus if the people[hi] cannot be seated with people[lo] in one boat then that means that people[hi] cannot form a pair with any of the remaining people, and we will thus stop looking for a partner for that person and give him a boat for him/her self.'''
        people.sort()
        lo = 0
        hi = len(people)-1
        boats = 0

        while lo<=hi:
            if people[lo] + people[hi] <= limit:
                lo += 1
                hi -= 1
            else:
                hi -= 1
            
            boats += 1
        
        return boats