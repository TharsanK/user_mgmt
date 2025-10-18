#!/usr/bin/python


import subprocess


# Using the usermod cmd in order to add user to the list of groups given
# -aG ---> Append user to a new group with out deleting the user from the
# previous groups
def user_add_to_group(username, groupname):
    cmd = ["usermod"]
    cmd.append(username)
    cmd.append("-aG")
    cmd.append(groupname)
    subprocess.run(cmd)
