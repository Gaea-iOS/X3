# This script is use to update build number.

import os
import time
import subprocess
import argparse
import check_tool

# refer to https://segmentfault.com/a/1190000004678950
# refer to https://developer.apple.com/library/archive/qa/qa1827/_index.html

# You must complete the following steps in your Xcode project.
# 1) Enable agvtool.
# Set Current Project Version to a value of your choosing.
# Set Versioning System to Apple Generic.
# 2) Set up your version and build numbers.
# agvtool searches your application’s Info.plist for your version and build numbers. It updates them if they exist and does nothing, otherwise. Make sure that the CFBundleVersion (Bundle version) and CFBundleShortVersionString (Bundle versions string, short) keys exist in your Info.plist.
# Note: The DYLIB_CURRENT_VERSION (Current Library Version ) build setting specifies the current build version of a library or framework. if you are building a library or framework, be sure to follow the above steps and make sure that the Build Settings pane of your target includes this setting.

def update_build_number(build_number):
    subprocess.run(['agvtool', 'new-version', '-all', build_number])

default_version = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
parser = argparse.ArgumentParser(description="update build number.")
parser.add_argument("--version", type=str, default=default_version, help="the build number to update, default is current date 'yyyymmddHHMMSS'")

args = parser.parse_args()
version = args.version

configuration = os.getenv('CONFIGURATION')

if configuration == 'Release':
    update_build_number(version)
    print(configuration + ' build - Update build number to ' + version)
else:
    print(configuration + ' build - No update for build number')



