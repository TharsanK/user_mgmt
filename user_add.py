#!/usr/bin/python


import subprocess
from rich.console import Console
from rich.text import Text
from rich.prompt import Prompt, Confirm
from user_get import user_get
# The Main Function


def user_add(username, shell, groups, home=False):
    cmd = ['useradd']
    if home:
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


# USER INTERFACE
# Welcome message
fig = subprocess.Popen(['figlet', '-c', 'USER _ ADD'], stdout=subprocess.PIPE)

lol = subprocess.Popen(['lolcat'], stdin=fig.stdout)

fig.stdout.close()
lol.communicate()


# Console Creation
con = Console()


# Introduction
intro_msg = """
Welcome to user_add !!!
Here you can add delete and manage all the user in the system.
Respond the following prompts carefully.
"""
intro = Text(intro_msg, style='bold cyan', justify='centre')
con.print(intro)

# Details about the users and groups available
# users
u, b = user_get()
user_msg = Text("USER IN THE SYSTEM", style="bold cyan")
print(user_msg)
for i in u:
    user = Text(i, style='bold cyan', justify='center')
    print(user)

b_msg = Text(
    "BACKGROUND USERS IN THE SYSTEM(Recommended not to touch these) ", style="bold cyan")
print(b_msg)
for i in b:
    b_user = Text(i, style='bold bright_green')
    print(b_user)

# Required Prompts
username = Prompt.ask("Enter the username of the new user")
home = Confirm.ask("Would you like to add a home folder for the new user")
groups = Prompt.ask("Enter the GID of groups to which the user will be added")
groupname = groups.split(',')
shell = Prompt.ask("Enter the shell which the user will use")
