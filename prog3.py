import subprocess

import os

import argparse

path=input("/home/kali/image/ ")

res=subprocess.run(["md5sum", path], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)

print(res.stdout.split()[0])

d_path=input("Directory Path: ")

file_names = os.listdir(d_path)

names = [file for file in names if os.path.isfile(os.path.join(d_path,file))]

parser = argparse.ArgumentParser(description="Working of Argparse")

parser.add_argument("name", type=str, help="Your name")

parser.add_argument("class", type=str, help="Your class")

args = parser.parse_args()

print("{args.name}, {args.class}")
