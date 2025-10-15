#!/usr/bin/python

import subprocess  # Module for executing terminal commands
import sys  # Module for collecting args
import getopt  # Module for getting options

# The Main Function


def user_add(username, shell, groups, home=False):
    cmd = ['useradd']
    if home == True:
        cmd.append('-m')
    cmd.append('-G')
    for i in groups:
        cmd.append(i)
    cmd.append(username)
    cmd.extend(['-s', shell])
    subprocess.run(cmd)
    subprocess.run(['passwd', username])
# The functions add the given argument collected from the getopts
# and sys.argv and then construct a proper useradd command stored
# in the cmd variable which is then executed using the subprocess
# module


# SETTING ARGUMENT AND OPTIONS
argv = sys.argv[1:]
short = "ms:G:"
long = ["shell=", "groups="]

# COLLECTING ARGUMENTS AND OPTIONS
try:
    opts, args = getopt.getopt(argv, short, long)
except getopt.GetoptError as err:
    print(err)
    print("Please read the man page")
    sys.exit(2)

# PROCESSING ARGUMENTS AND OPTIONS
# Required Variables
home = False
groups = []
shell = None
username = None

for i, v in opts:
    if i == "-m":
        home = True

    elif i == "-G":
        for j in v.split(","):
            groups.append(j)

    elif i == "-s":
        shell = v

username = args[0]
user_add(username, shell, groups, home)
