from os import system


characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
punctuation = ['.',',','!',' ', "\"", ':', ';', '<', '>', '?', '(', ')']
while True:
    system('cls')
    print("\n\t\t\t\t\t\t\tCIPHOTRON 3000\n".center(500,'='))
    print("\n\t\t\t\t\t\tDeveloped By Bhargava Madhav.\n")
    print(" Please Choose One Of The Following Options: \n\n 0. Exit The Program\n\n 1. ROT13 (AKA Caesar Cipher)\n\n 2. Vigenère Cipher\n")
    answer = input("\n [>] Enter The Corresponding Number Of Your Choice: ")
    def ROT13(word):
        result = ""
        for letter in word:
            iscapital = letter.isupper()
            letter = letter.upper()
            if letter in punctuation or letter.isdecimal():
                result = result + letter
            else:
                try:
                    letter = characters[characters.index(letter) + 13]
                    if iscapital:
                        result = result + letter
                    else:
                        result = result + letter.lower()
                except IndexError:
                    letter = characters[characters.index(letter) - 13]
                    if iscapital:
                        result = result + letter
                    else:
                        result = result + letter.lower()
        print("\n The Encoded/Decoded Result is: %s\n" % result)

    def VigenereCipher_encode(word):
        result = ""
        a = 0
        keyword = input("\n[>] Please Enter a Keyword of Your Choice: ")
        keyword = keyword.upper()
        for letter in keyword:
            if letter in punctuation or letter.isdecimal():
                keyword = keyword.replace(letter, '')
        for letter in word:
            iscapital = letter.isupper()
            letter = letter.upper()
            if letter in punctuation or letter.isdecimal():
                result = result + letter
            else:
                try:
                    newl = characters[characters.index(letter) + characters.index(keyword[a])]
                    if iscapital:
                        result = result + newl
                    else:
                        result = result + newl.lower()
                    a += 1
                except IndexError:
                    if a > (len(keyword) - 1):
                        a = 0
                    newl = characters[(characters.index(letter) + characters.index(keyword[a])) - 26]
                    if iscapital:
                        result = result + newl
                    else:
                        result = result + newl.lower()
                    a += 1
        print("\n The Encoded Result is: %s\n" % result)

    def VigenereCipher_decode(word):
        result = ""
        a = 0
        keyword = input("\n[>] Please Enter The Keyword: ")
        keyword = keyword.upper()
        for letter in keyword:
            if letter in punctuation or letter.isdecimal():
                keyword = keyword.replace(letter, '')
        for letter in word:
            iscapital = letter.isupper()
            letter = letter.upper()
            if letter in punctuation or letter.isdecimal():
                result = result + letter
            else:
                try:
                    newl = characters[characters.index(letter) - characters.index(keyword[a])]
                    if iscapital:
                        result = result + newl
                    else:
                        result = result + newl.lower()
                    a += 1
                except IndexError:
                    if a > (len(keyword) - 1):
                        a = 0
                    newl = characters[characters.index(letter) - characters.index(keyword[a])]
                    if iscapital:
                        result = result + newl
                    else:
                        result = result + newl.lower()
                    a += 1
        print("\n The Decoded Result is: %s\n" % result)
                

    if answer == "1":
        system('cls')
        word = input("\n[>] Please Enter The Word/Sentence You'd Like To Encode/Decode In ROT13 (AKA Caesar Cipher): ")
        ROT13(word)
        input("\n Press Enter To Continue. ")
    elif answer == "2":
        system('cls')
        print("\nWhat Would You Like To Do Using Vigenère Cipher?\n\n 1. Encode a Plaintext\n\n 2. Decode a Ciphertext\n")
        answer1 = input("\n [>] Enter The Corresponding Number Of Your Choice: ")
        if answer1 == "1":
            system('cls')
            word = input("\n[>] Please Enter The Word/Sentence You'd Like To Encode Using The Vigenère Cipher: ")
            VigenereCipher_encode(word)
            input("\n Press Enter To Continue. ")
        elif answer1 == "2":
            system('cls')
            word = input("\n[>] Please Enter The Word/Sentence You'd Like To Decode Using The Vigenère Cipher: ")
            VigenereCipher_decode(word)
            input("\n Press Enter To Continue. ")
        else:
            input("\n Invalid Input. Please Try Again.")
    elif answer == "0":
        print("\n Exiting The Program...")
        break
    else:
        input("\n Invalid Input. Please Try Again.")