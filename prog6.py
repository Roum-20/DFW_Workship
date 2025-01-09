import sys

import subprocess

import os

 

t_name=sys.argv[1]

ip_path=sys.argv[2]

op_path=sys.argv[3]

type=sys.argv[4]


if t_name=="foremost":

  operation=[t_name,"-i",ip_path,"-o",op_path,"-t",type]

elif t_name=="magicrescue":

   operation=[t_name,"-r",type,"-d",ip_path,op_path]

else:

  print("Invalid")


Pres=subprocess.run(operation,check=True)

print(res)

#output for terminal
#python3 q6.py foremost input/image.dd output/derctory pdf
