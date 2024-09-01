# your code goes here!
# lib/anagram.py

class Anagram:
    def __init__(self, word):
        self.word = word
        # Sort the letters of the original word to compare with other words
        self.sorted_word = ''.join(sorted(word))
    
    def match(self, possible_anagrams):
        matches = []
        for candidate in possible_anagrams:
            # Sort the letters of the candidate word and compare with sorted_word
            if ''.join(sorted(candidate)) == self.sorted_word:
                matches.append(candidate)
        return matches
