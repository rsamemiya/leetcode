class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #create a dictionary that will hold the anagram of the strings in the array
        result_dictionary ={}
        
        #create empty list that will have all lists added to which    you'll return at the end
        
        result_list = []
        
        #Iterate through array of strings:
        for i in range(len(strs)):
        
            #Turn each element into a list by applying sorted(element)
            sorted_element = sorted(strs[i])
        
            #Turn the sorted list back into a string by using "".join(element)
            restrung = "".join(sorted_element)
            
            #if anagram is not in dictionary:
            if restrung not in result_dictionary:
                #add anagram as a key to dictionary = iterated element and put it inside a list
                result_dictionary[restrung] =[strs[i]]
            #else:
            else:
                #append iterated element to that list in the dictionary
                result_dictionary[restrung].append(strs[i])
        #iterate through dictionary's values
        for k in result_dictionary:
        
            #append each value to the empty list that you created at the beginning
            result_list.append(result_dictionary[k])
            
        #return that list
        return result_list

        
        
        