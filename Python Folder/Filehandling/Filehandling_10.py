class VowelConsonant:
    def __init__(self, file):
        self.file = file

    def wordlist(self):
        with open(self.file) as f:
            vowel, consonant = [], []
            content = f.readlines()
            for i in range(len(content)):
                for j in content[i].split():
                    if any(char.lower() in "aeiou" for char in j):
                        vowel.append(j)
                    else:
                        consonant.append(j)

        print("Vowel list :", vowel)
        print("Consonant List  :", consonant)


files = input("Enter Filename :")
VowelConsonant(files).wordlist()
