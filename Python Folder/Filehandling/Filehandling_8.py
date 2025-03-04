import os


def runosfiles():
    file1 = input("Enter 1st Filename :")
    file2 = input("Enter 2nd Filename :")
    choice = int(input("Enter choice (1/2) :\n1.Rename\n2.Remove"))
    if choice == 1:
        os.rename(file1, file2)
    elif choice == 2:
        os.remove(file1)
    else:
        print("Invalid Choice")


runosfiles()
