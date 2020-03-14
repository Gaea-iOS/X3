# This script is use to update bundle version.

import os
import time
import subprocess
import argparse

# refer to https://segmentfault.com/a/1190000004678950
# refer to https://developer.apple.com/library/archive/qa/qa1827/_index.html

# You must complete the following steps in your Xcode project.
# 1) Enable agvtool.
# Set Current Project Version to a value of your choosing.
# Set Versioning System to Apple Generic.
# 2) Set up your version and build numbers.
# agvtool searches your application’s Info.plist for your version and build numbers. It updates them if they exist and does nothing, otherwise. Make sure that the CFBundleVersion (Bundle version) and CFBundleShortVersionString (Bundle versions string, short) keys exist in your Info.plist.
# Note: The DYLIB_CURRENT_VERSION (Current Library Version ) build setting specifies the current build version of a library or framework. if you are building a library or framework, be sure to follow the above steps and make sure that the Build Settings pane of your target includes this setting.

def update_version_number(version_number):
    # Important: When your app includes multiple targets, agvtool will set the version numbers of all your targets to the same number.
    subprocess.run(['agvtool', 'new-marketing-version', version_number])

parser = argparse.ArgumentParser(description="update version number.")
parser.add_argument("--version", required=True, type=str, help="the version number to update")

args = parser.parse_args()
version = args.version

update_version_number(version)
print('Update version number to ' + version)
