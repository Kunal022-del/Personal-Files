class VowelCount:
    def __init__(self, filename):
        self.filename = filename

    def counts(self):
        with open(self.filename) as f:
            content = f.readlines()
            vowelcount, consonat = 0, 0
            for i in range(len(content)):
                for j in content[i].lower().split():
                    for s in j:
                        if s in "aeiou":
                            vowelcount += 1
                        elif s.isdigit() is False:
                            consonat += 1
        print("Total number of vowels :", vowelcount)
        print("Total number of consonant :", consonat)


files = input("Enter Filename :")
VowelCount(files).counts()
