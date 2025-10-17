#!/usr/bin/python

import subprocess
import sys
import getopt


# Using the usermod cmd in order to add user to the list of groups given
# -aG ---> Append user to a new group with out deleting the user from the
# previous groups
def user_add_to_group(username, groupname):
    cmd = ["usermod"]
    cmd.append(username)
    cmd.append("-aG")
    cmd.append(groupname)
    subprocess.run(cmd)


# sys.argv and opts setup
# -u --> username
# -G --> list of the group names
argv = sys.argv[1:]
short_options = "u:G:"
long_options = ["username=", "groups="]

try:
    opts, args = getopt.getopt(argv, short_options, long_options)

except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

# Required Variables
username = None
groups = None

# Looping through the options
# -u --> for username collection
# -G --> for group list collection
for i in opts:
    if i[0] == "-u":
        username = i[1]
    elif i[0] == "-G":
        groups = i[1]

user_add_to_group(username, groups)
