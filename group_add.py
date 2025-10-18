#!/usr/bin/python


import subprocess


# Main Function --> Creating and groups using the groupadd cmd
# and setting passwd using the gpasswd command
def group_add(gname):
    subprocess.run(['groupadd', gname])
    subprocess.run(['gpasswd', gname])
