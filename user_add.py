#!/usr/bin/python


import subprocess


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
