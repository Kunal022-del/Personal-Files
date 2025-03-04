class Anagram:
    def __init__(self, array):
        self.array = array

    def anagram_game(self):
        anagram = {}
        for word in self.array:
            sorted_word = " ".join(sorted(word))
            if sorted_word in anagram:
                anagram[sorted_word].append(word)
            else:
                anagram[sorted_word] = [word]
        print(anagram)


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
Anagram(words).anagram_game()
