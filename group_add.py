#!/usr/bin/python

import subprocess
import sys


def group_add(gname):
    subprocess.run(['groupadd', gname])
    subprocess.run(['gpasswd', gname])


if len(sys.argv) >= 2:
    group_add(sys.argv[1])
else:
    pass
