class Encrypter:

    def __init__(self, keys, values, dictionary):
        self.w1k = keys
        self.w2k = values
        self.dictCopy = dictionary
        self.word1 = "".join(keys)
        self.word2 = "".join(values)
        self.encrypt(self.word1)
        self.decrypt(self.word2)

    def encrypt(self, word1):
        encryptWord = ""
        for i in range(len(self.w1k)):
            if (i >= len(self.w1k) or i >= len(self.w2k)):
                encryptWord = ""
                break
            encryptWord += self.w2k[i]
        print("The encrypted word is: ", encryptWord)

    def decrypt(self, word2):
        num = 0
        mapping = dict(zip(self.w1k, self.w2k))
        usedWords = []
        print(mapping)
        for x in range(len(self.dictCopy)):
            for word in self.dictCopy[x]:
                if word in usedWords:
                    continue
                usedWords.append(word)
                if word[0] not in mapping.keys():
                    continue
                print(word)
                encrypted_word = ''.join(mapping[char] for char in word)
                if encrypted_word == word2:
                    #print(encrypted_word, word2)
                    num += 1
        print("The decrypted number of words is: ", num)
    # def decrypt(self, word2):
    #     num = 1
    #     testDict = {}
    #     for i in range(len(self.w2k)):
    #         if self.w2k[i] not in testDict:
    #             testDict[self.w2k[i]] = 0
    #     for i in range(len(self.w2k)):
    #         testDict[self.w2k[i]] += 1
    #     for i in testDict.values():
    #         num *= i
    #     print(testDict)
    #     print("The decrypted number of words is: ", num)
        

keys = ['a', 'b', 'c', 'd']
values = ["ei", "zf", "ei", "am"]
dictionary = [["abcd", "acbd", "adbc", "badc", "dacb", "cadb", "cbda", "abad"],["abcd"], ["eizfeiam"]]


# Your Encrypter object will be instantiated and called as such:
obj = Encrypter(keys, values, dictionary)
