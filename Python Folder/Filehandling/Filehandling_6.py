class Treegenerator:
    def __init__(self, file, height):
        self.file = file
        self.height = height

    def generatetree(self):
        tree = ""
        for i in range(self.height):
            tree += " " * (self.height - i + 1) + "*" * (2 * i + 1) + "\n"
        tree += " " * (self.height + 1) + "*\n"
        return tree

    def savetree(self):
        with open(self.file, "w") as f:
            f.write(self.generatetree())


file = input("Enter Filename :")
Height = int(input("Enter Height of Tree :"))
tree_inh = Treegenerator(file, Height)
tree_inh.generatetree()
tree_inh.savetree()
