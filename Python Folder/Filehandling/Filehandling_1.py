class WordsFindLine:
    def __init__(self, filename):
        self.filename = filename

    def create(self):
        with open(self.filename, "w") as f:
            f.write("Hello Kunal\n" * 10)

    def wordfind(self, word):
        with open(self.filename) as f:
            content = f.readlines()
            for i in range(len(content)):
                if word in content[i]:
                    print(f"{word} is in line {i+1}")


files = input("Enter Filename :")
word = input("Enter Word to Find :")
word_inst = WordsFindLine(files)
word_inst.create()
word_inst.wordfind(word)
