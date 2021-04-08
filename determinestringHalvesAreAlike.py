# run O(n) space O(n+k)

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        s = s.lower() 
        a = s[:len(s) // 2]
        b = s[len(s) // 2:]
        
        
        vowels = {'a', 'e', 'i', 'o', 'u'}
        a_vowel = 0 
        b_vowel = 0 
        
        for aa in a: 
            if aa in vowels:
                a_vowel += 1 
        
        for bb in b: 
            if bb in vowels: 
                b_vowel += 1
        
        return a_vowel == b_vowel
                
        
