import subprocess
import json
import os


f = open(os.path.abspath(os.getcwd()) + '/config.json')
config = json.load(f)
f.close()

print(config["dependencies"])
for key, value in config["dependencies"].items():
    subprocess.run(["pip","install", key+value])
