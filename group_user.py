#!/usr/bin/python

import subprocess
import sys
import getopt


# Using the gpasswd command for group managment
def add_user_to_group(groupname, username):
    cmd = ["gpasswd"]
    cmd.append("-a")  # For adding a user
    cmd.append(username)  # Providing a user name
    # Providing the group name to which the user needs to be added to
    cmd.append(groupname)
    subprocess.run(cmd)


# Argument Handling
argv = sys.argv[1:]
short_opts = 'u:G:'
long_opts = ['username=', 'group=']

try:
    opts, args = getopt.getopt(argv, short_opts, long_opts)
except getopt.GetoptError as err:
    print(err)
    sys.exit(2)

# Argument Parsing
# Required Variables
username = None
groupname = None


for i in opts:
    if i[0] == '-u':
        username = i[1]
    elif i[0] == "-G":
        groupname = i[1]

# Function Invoke
add_user_to_group(groupname, username)
