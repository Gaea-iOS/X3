# This script is used to create a keychain file and import p12 files using keychain setting file.
# A keychain setting file format:
# {
#     "name": "xxx.keychain",     // name of the keychain file
#     "password": "123456",       // password of the keychain file
#     "p12s": [                   // p12 files
#         {
#             "name": "x3",       // name of the p12
#             "password": "1234"  // password of the p12
#         }
#     ]
# }

import argparse
import subprocess
import os
import json

def createKeychain(keychain, password):
    print(keychain + ' ' + password)
    subprocess.run(["security", "create-keychain", "-p", password, keychain])

def importP12(keychain, p12, p12Password):
    subprocess.run(["security", "import", p12, "-P", p12Password, "-k", keychain])

def importP12s(keychain, p12Settings):
    for settings in p12Settings:
        p12 = settings["name"]
        password = settings["password"]
        importP12(keychain, p12, password)

def getSettings(setting_file):
    f = open(setting_file)
    settings = json.load(f)
    return settings 

parser = argparse.ArgumentParser(description="create a keychain and import p12 files using a keychain setting file.")

parser.add_argument("--setting", required=True, type=str, help="the keychain setting file, which must be a json file.")

args = parser.parse_args()

settings = getSettings(args.setting)

keychain = os.getcwd() + '/' + settings['name']
password = settings['password']
p12Settings = settings['p12s']

createKeychain(keychain, password)
importP12s(keychain, p12Settings)