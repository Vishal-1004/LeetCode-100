class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        '''Before prociding to the solutions we must concider few cases
        /abc/..   here these ".." means that we must pop back from the current directory that is we are currently in abc so we must go back  to root directiory that is "/"
        
        next case is /abc/./cba
        here "." mean that we are refering to the same directiory that is abc so we can write it as /abc/cba
        
        next case is /..
        here though .. means that we must revert back but if we do we cant go back from root directory so we in this case only we stay  in root directory 
        
        next case /abc//cba
        here we have one extra "/" so just remove it and we get /abc/cba
        
        now we can proced with our answer'''
        stack = []
        '''cur is used to store the file names from the given string'''
        cur = ""

        '''we add an extra char that is "/" in the end of the path so that we can work more easily with our code'''
        for c in path + "/":
            '''if c == / then we check for the cur value if it is equal to .. then we revert back to the previous directory by poping out the top directory and this is to be done only when the stack is not empty because if it would have been empty then their is no way to revert back from the root directory'''
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()

                    '''if the leght of  cur is not 0 and cur is not equal to .. or . so it means that we got a directory name to go in, so we will just append it in the stack'''
                elif cur != "" and cur != ".":
                    stack.append(cur)

                '''finally the cur has to be made empty again and again'''
                cur = ""

            else:
                '''if c is not / then it could be either . or .. or some alpha so we just add it in cur'''
                cur += c

        '''since our answer start form the root directory so we just start form / and join rest of the elements of the array with a / too'''
        return  "/" + "/".join(stack)