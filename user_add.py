#!/usr/bin/python


import subprocess
from rich.text import Text
from rich.console import Console


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


# CLI USER INTEFACE CREATION


# Console Creation
con = Console()

# Piping Output in subprocess
cmd1 = subprocess.Popen(["figlet", "-c", "USER_ADD"], stdout=subprocess.PIPE)
cmd2 = subprocess.Popen(
    ["lolcat", "-a"], stdin=cmd1.stdout)
cmd1.stdout.close()

cmd2.communicate()


# Introductory text
intro = Text("WELCOME TO THE USER ADD CLI USER INTERFACE",
             style="bold blue", justify="center")

# Output Managment
con.print(intro)
