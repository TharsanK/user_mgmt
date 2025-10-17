#!/usr/bin/python

import subprocess
import sys
import getopt


def user_add_to_group(username, groupname):
    cmd = ["usermod"]
    cmd.append(username)
    cmd.append("-aG")
    cmd.append(groupname)
    subprocess.run(cmd)


# sys.argv and opts setup
argv = sys.argv[1:]
short_options = "u:G:"
long_options = ["username=", "groups="]

try:
    opts, args = getopt.getopt(argv, short_options, long_options)

except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

username = None
groups = None

for i in opts:
    if i[0] == "-u":
        username = i[1]
    elif i[0] == "-G":
        groups = i[1]

user_add_to_group(username, groups)
