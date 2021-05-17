import argparse
import os

ap = argparse.ArgumentParser()
ap.add_argument("-f", "--file", type = str, required = True)
ap.add_argument("-p", "--path", type = str, required = False)
args = ap.parse_args()

filename = str(args.file)
path = str(args.path)

if path == "None":
    os.system(f"scp {filename} pi@192.168.100.15:~/rusty/")
else:
    os.system(f"scp {filename} pi@192.168.100.15:~/{path}")