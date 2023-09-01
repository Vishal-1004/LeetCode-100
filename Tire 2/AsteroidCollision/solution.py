class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        '''
        when ever an asteroid is going to be added to the ansArr their are two things to occur they are as follows: 
        1. Collision occured 
            Here also three things can occur and they are
                * left asteroid distroyes the right one i.e 3,-1 ... in this case their no more  to distroy so  break;

                * right asteroid distroyes the left one i.e -1,3 ... in this case their can be chance that it could distory more left, so pop out the current left and repeat the check again 

                * both distroyes each other i.e 3,-3 ... in this case theirs no more to distroy so break;

        2. Collision does not occured
        '''
        ansArr = []

        for i in asteroids:
            '''while ansArr has some length and its last element is moving in right side and the ith element is moving in left side then ....'''
            while ansArr and ansArr[-1] > 0 and i < 0:
                '''if collision occures with point 2 that is right distroyes left then just pop out the current left and the while loop contiues'''
                if ansArr[-1] + i < 0:
                    ansArr.pop()

                    '''if left distoyes right then theirs is nothing to distory as well as to pop so we just give a break to our while loop hunt of distruction'''
                elif ansArr[-1] + i > 0:
                    break
                
                    '''if both distroy each other then just pop out the last element from ansArr and give a break to the while loop cause their is nothing to distroy more'''
                else:
                    ansArr.pop()
                    break
            
                '''this else condtion is only executed when the "while" loop break normally/naturally i.e due to the end of its conditions holiding it. If the while loop stops due the break statements then this else condition will not be executed'''
            else:
                '''the left asteroid which has recently distroyes the right asteroid and gave an end to the while loop has to appended at the end of the ansArr'''
                ansArr.append(i)

        return ansArr