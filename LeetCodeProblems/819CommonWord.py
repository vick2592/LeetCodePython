import re


class CommonWord819:
    def mostCommonWord(p, b):
        words = re.findall(r'\w+', p.lower())
        wordCount = {}
        for word in words:
            if (word not in b):
                wordCount[word] = 0

        for word in words:
            if (word in wordCount.keys()):
                wordCount[word] += 1

        value = 0
        word = ''

        for w,v in wordCount.items():
            print(w + " " + str(v))
            if v > value:
                word = w
                value = v

        return word, str(value)

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

print(CommonWord819.mostCommonWord(paragraph,banned)[0], " Is the best word with count ", CommonWord819.mostCommonWord(paragraph,banned)[1])