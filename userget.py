#!/usr/bin/python

# Import for CLI handling
import sys


def user_get():
    # Path to the /etc/shadow file where the user information is stored
    # For format of the file check below given link
    # The /etc/passwd is more safe to use because encrypted pass is not stored there
    # https://man.archlinux.org/man/shadow.5.en
    # https://man.archlinux.org/man/passwd.5
    path1 = "/etc/passwd"

    # Opening the File
    u = []  # --> user list
    b = []  # --> background process list
    with open(path1, 'r') as f:

        # Reading the data is the File
        data = f.readlines()

        # Each data string is ':' delimited therefore splitting with ':'
        # If the third data(UID) is >= 1000, then it is a user.
        # otherwise the user is a background process
        for i in data:
            d = i.split(":")
            if int(d[2]) < 1000 or ('nologin' in d[6]):
                b.append(d[0])
            elif int(d[2]) >= 1000 or ('nologin' not in d[6]):
                u.append(d[0])
    return (u, b)


# Utilizing the function
u, b = user_get()

# CLI Handling
if len(sys.argv) >= 2:
    if sys.argv[1] == "-u" or sys.argv[1] == "-U":
        # Printing the user stored
        print("USER IN THE SYSTEM")
        print("=================")
        for i in u:
            print(i)
        print("==================")
    elif sys.argv[1] == "-b" or sys.argv[1] == "-B":
        print("BACKGROUND USERS")
        print("==================")
        for i in b:
            print(i)
        print("==================")
else:
    pass
