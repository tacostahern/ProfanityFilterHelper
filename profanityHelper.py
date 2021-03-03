'''
This program will be used to help the profanity filter in Verse Travers
'''

import os

def main():
    profanityList = readFile()
    repeat = 'Y'
    wordPresent = False
    while repeat.lower() == 'y':
        profanity = input("Please enter the new profanity word: ")

        for i in profanityList:
            if i == profanity:
                print(profanity, "is already in the list.")
                wordPresent = True

        if wordPresent == False:
            profanityList.append(profanity)
            print(profanity, "added to the list.")
        repeat = input("Add more words? Enter 'Y' for yes: ")
    writeFile(profanityList)
        

def readFile():
    f1 = "profanityList.txt"

    if os.path.isfile(f1):
        infile = open(f1, "r")
        data = infile.read()

        profanityList = data.split("|")

    else:
        print("File does not exist!")
        profanityList = list()

    return profanityList

def writeFile(profanityList):
    f1 = "profanityList.txt"

    if os.path.isfile(f1):
        outfile = open(f1, "w")
        for i in profanityList:
            outfile.write(i + "|")

main()
