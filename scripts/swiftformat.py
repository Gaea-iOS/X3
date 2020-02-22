import subprocess

def swiftformat(file, config):
    print("format " + file)
    subprocess.run(["swiftformat", file, "--config", config])


