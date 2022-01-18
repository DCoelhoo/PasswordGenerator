import string
import random

allCharacters = list(string.ascii_letters + string.digits + "!#%&/@?=()")
onlyLetters = list(string.ascii_letters)
onlyNum = list(string.digits)
onlySpecialCharacters = list("!#%&/@?=()")

def PasswordGen():
    print("What type of password do you want? \n "
          "With all characters: type 1 \n "
          "Only numbers : type 2 \n "
          "Only Letters: type 3 \n "
          "Only Special Characters: type 4")

    passType = (int(input("R: ")))
    passLen = (int(input("Enter the password len: ")))

    random.shuffle(allCharacters)

    newPass = []

    if passType == 1:
        for i in range(passLen):
            newPass.append(random.choice(allCharacters))

        random.shuffle(newPass)
        print("".join(newPass))
    elif passType == 2:
        for i in range(passLen):
            newPass.append(random.choice(onlyNum))

        random.shuffle(newPass)
        print("".join(newPass))
    elif passType == 3:
        for i in range(passLen):
            newPass.append(random.choice(onlyLetters))

        random.shuffle(newPass)
        print("".join(newPass))
    elif passType == 4:
        for i in range(passLen):
            newPass.append(random.choice(onlySpecialCharacters))

        random.shuffle(newPass)
        print("".join(newPass))
    else:
        print("Please, choose a valid answer.")




PasswordGen()

closeApp = string(input("Write something to close the app: "))

