class Solution:
    def minimumPushes(self, word: str) -> int:
        keymap = {i:[] for i in range(2,10)}
        key = 2
        count_keystrokes = 0 
        
        for ch in word:
            if key > 9:
                key = (key+2)%10
            # put the char in the next available key 
            keymap[key].append(ch)
            # update the count of the keystrokes 
            count_keystrokes += len(keymap[key])
            key += 1
            
        return count_keystrokes
            
            
            