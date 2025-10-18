#!/usr/bin/python


import subprocess


# Using the gpasswd command for group managment
def add_user_to_group(groupname, username):
    cmd = ["gpasswd"]
    cmd.append("-a")  # For adding a user
    cmd.append(username)  # Providing a user name
    # Providing the group name to which the user needs to be added to
    cmd.append(groupname)
    subprocess.run(cmd)
