#!/usr/bin/python


# Path to the /etc/shadow file where the user information is stored
# For format of the file check below given link
# https://man.archlinux.org/man/shadow.5.en
path1 = "/etc/shadow"

# Opening the File
u = []
with open(path1, 'r') as f:

    # Reading the data is the File
    data = f.readlines()

    # Each data string is ':' delimited therefore splitting with ':'
    # If the second data(encrpted passwork) is "!*" then
    # the user is a background process
    for i in data:
        d = i.split(":")
        if d[1] == "!*":
            pass
        elif d[1] != "!*":
            u.append(d[0])

# Printing the user stored
print("USERNAMES IN THE SYSTEM")
for i in u:
    print(i)
