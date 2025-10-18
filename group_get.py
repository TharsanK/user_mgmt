#!/usr/bin/python


def group_get():
    # Path to the /etc/group file where the user information is stored
    # For format of the file check below given link
    # The /etc/group is more safe to use because encrypted pass is
    # not stored there
    # https://man.archlinux.org/man/group.5
    path1 = "/etc/group"

    # Opening the File
    g = []  # --> group list
    with open(path1, 'r') as f:

        # Reading the data is the File
        data = f.readlines()

        # Each data string is ':' delimited therefore splitting with ':'
        # Check man pages for meaning for the : deliminted values
        for i in data:
            d = i.split(":")
            g.append((d[0], d[2], d[3]))
    return g
