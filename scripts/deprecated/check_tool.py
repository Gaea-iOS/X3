# This script use to check whether the specify tool is installed.

import os
import subprocess

def is_tool_installed(tool):
    devnull = open(os.devnull, 'w')
    return subprocess.run(['which', tool], stdout = devnull).returncode == 0