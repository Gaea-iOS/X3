# This script is use to import a keychain file.

import argparse
import subprocess
import os
import json

def unlock_keychain(keychain, password):
    subprocess.run(["security", "unlock-keychain", "-p", password, keychain])

def lock_keychain(keychain):
    subprocess.run(["security", "set-keychain-settings", "-u", keychain])
        
def list_keychains(keychains):   
    cmd = ["security", "list-keychains", "-s"] + keychains
    subprocess.run(cmd)

def set_key_partition_list(keychain, password):
    subprocess.run(["security", "set-key-partition-list", "-S", "apple-tool:,apple:,codesign:", "-s", "-k", password, keychain], stdout=subprocess.PIPE)

def get_settings(setting_file):
    f = open(setting_file)
    settings = json.load(f)
    return settings 

def import_keychain(keychain, password):
    unlock_keychain(keychain, password)
    list_keychains(["login.keychain", keychain])
    set_key_partition_list(keychain, password)
    lock_keychain(keychain)

parser = argparse.ArgumentParser(description="import keychain.")

parser.add_argument("--keychain", required=True, type=str, help="the path of keychain")
parser.add_argument("--password", required=True, type=str, help="the password of keychain")

args = parser.parse_args()

keychain = args.keychain
password = args.password

import_keychain(keychain, password)