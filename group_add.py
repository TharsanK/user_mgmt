#!/usr/bin/python

import subprocess
import sys


# Main Function --> Creating and groups using the groupadd cmd
# and setting passwd using the gpasswd command
def group_add(gname):
    subprocess.run(['groupadd', gname])
    subprocess.run(['gpasswd', gname])


# Fundamental Argument Handling
if len(sys.argv) >= 2:
    group_add(sys.argv[1])
else:
    pass
