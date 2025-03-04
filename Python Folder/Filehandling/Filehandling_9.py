class Alphabet:
    def __init__(self, file):
        self.file = file

    def alphabetaz(self):
        with open(self.file, "a+") as f:
            for i in range(ord("A"), ord("Z") + 1):
                f.write(chr(i))
            f.write("\n")
            for j in range(ord("a"), ord("z") + 1):
                f.write(chr(j))


files = input("Enter Filename :")
Alphabet(files).alphabetaz()
