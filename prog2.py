import sys
import os

path=sys.argv[1]

file_names=os.listdir(path)

names=[file for file in file_names if os.path.isfile(os.path.join(path,file))]

print(file_names)

print(names)
for i in names:
  dd=f"dd if={i} bs=4M i=1"
  print(dd)
  
 #command for terminal 
 #python3 q2.py input directory(jpg.pdf)
