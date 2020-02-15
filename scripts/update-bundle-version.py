# This script is use to update bundle version.

import os
import time
import subprocess

def update_bundle_version(plist, bundle_version):
    subprocess.run(['/usr/libexec/PlistBuddy', '-c', 'Set CFBundleVersion ' + bundle_version, plist])

plist = os.getenv('PROJECT_DIR') + '/' + os.getenv('INFOPLIST_FILE')
configuration = os.getenv('CONFIGURATION')

if configuration == 'Debug':
    bundle_version = time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))
    update_bundle_version(plist, bundle_version)
    print(configuration + ' build - Bumped bundle version to ' + bundle_version)
else:
    print(configuration + ' build - Not bumping bundle version')