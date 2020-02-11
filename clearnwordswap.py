import string
alphabet = list(string.ascii_lowercase)


def cost_to_swap(word1, word2):
    nums1 = []
    nums2 = []
    for letter in word1:
        nums1.append(alphabet.index(letter) + 1)
    for letter in word2:
        nums2.append(alphabet.index(letter) + 1)
    coins = []
    for i in range(len(nums1)):
        coins.append(nums1[i] - nums2[i])
    print(sum(coins))


cost_to_swap("minions", "unicorn")
