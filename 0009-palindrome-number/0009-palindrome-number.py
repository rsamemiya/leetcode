class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        #convert integer to string
        #put string into a list
        #reverse the list
        #if input == reversed variable
            #return true
        #else:
            #return false
            
        
        return list(str(x)) == list(str(x))[::-1]
           
        