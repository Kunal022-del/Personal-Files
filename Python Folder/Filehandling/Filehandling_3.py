class Replace:
    def __init__(self, file, old, new):
        self.file = file
        self.old = old
        self.new = new

    def replaceword(self):
        with open(self.file) as f:
            content = f.read()
            content = content.replace(self.old, self.new)
        with open(self.file, "w") as f:
            f.write(content)


file = input("Enter Filename:")
old = input("Enter old word :")
new = input("Enter new word :")
Replace(file, old, new).replaceword()
