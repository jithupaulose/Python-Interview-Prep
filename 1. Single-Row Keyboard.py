https://leetcode.com/problems/single-row-keyboard/

class Solution(object):
    def calculateTime(self, keyboard, word):
        #Create a dictionary that map the characher to index in the keyboard String.
        dictionary_mapping = {value : ind for ind, value in enumerate(keyboard)}
        
        # Initialize the current position and total time.
        current_position = 0
        total_time = 0
        
        #Interate each character in word
        for char in word:
            #Calculate the time move to this characher and add it to total time.
            total_time += abs(current_position - dictionary_mapping[char])
            #Update the current position
            current_position = dictionary_mapping[char]
        return total_time
            
