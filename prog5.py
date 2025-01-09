import subprocess

import sys

import os


 

if len(sys.argv) != 5:

  print("Usage: python script.py <tool> <input_file> <output_dir> <config_file>")

  sys.exit(1)


 

tool = sys.argv[1]

input_file = sys.argv[2]

output_dir = sys.argv[3]

config_file = sys.argv[4]


 

os.makedirs(output_dir, exist_ok=True)


 

if tool.lower() == "foremost":

  command = ["foremost", "-i", input_file, "-o", output_dir, "-c", config_file]

elif tool.lower() == "scalpel":

  command = ["scalpel", input_file, "-o", output_dir, "-c", config_file]

else:

  print("Unsupported tool. Please use 'foremost' or 'scalpel'.")

  sys.exit(1)

 

print(f"Running command: {' '.join(command)}")

result = subprocess.run(command)


 

if result.returncode == 0:

  print(f"{tool.capitalize()} completed successfully.")

else:

  print(f"An error occurred while running {tool}. Return code: {result.returncode}")
  
  #python3 prog5.py foremost /home/kali/image/image.dd /home/kali/prog5.output foremost.conf
