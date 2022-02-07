import os

userAnswer = input("command: ")

def copyCat(target):
    os.system("curl " + target + ">> index.html")
    with open("index.html", "r") as index:
        print(index.read())    

match (userAnswer):
    case "shutdown":
        os.system("sudo shutdown -h now")
    case "target":
        target = input("Type site: ")
        copyCat(target)
     