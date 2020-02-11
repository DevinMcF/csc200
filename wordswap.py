# New game
# Choose a word and writes, you only know length
# you have to make a word with same length
# earn/lose coinds depending on diference between word (how close they are)
# a-z
# position by poisition basis
# Same Characer/Same position = no coins move
# if word 1 is before in alphabet, then you pay how many between, inclusive
# if your word
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

class Word:
    def __init__(self, word):
        self.word = word
        self.letters = list(self.word)
        self.numletters = []
        for letter in self.letters:
            self.numletters.append(alphabet.index(letter) + 1)


    def compare(self, other):
        coins = []
        for i in range(len(self.numletters)):
            amount = self.numletters[i] - other.numletters[i]
            coins.append(amount)
        end = str(sum(coins))
        if end[0] == "-":
            end = end[1:]
            suffix = "earned"
        elif end[0] != "-":
            suffix = "cost"
        return [end, suffix]

def cost_to_swap(word1, word2):
    string_word1 = word1
    string_word2 = word2
    word1 = Word(word1)
    word2 = Word(word2)
    word2.compare(word1)
    amount = word2.compare(word1)[0]
    suffix = word2.compare(word1)[1]
    if amount == "1":
        print(f"Swapping letters to make {string_word2} look like {string_word1} {suffix} {amount} coin.")
    elif amount == "0":
        print(f"Swapping letters to make {string_word1} look like {string_word2} was FREE.")
    else:
        print(f"Swapping letters to make {string_word1} look like {string_word2} {suffix} {amount} coins.")

cost_to_swap("agnes", "heard")


def cost_to_swap(word1, word2):
    nums1 = []
    for letter in word1:
        nums1.append(alphabet.index(letter) + 1)