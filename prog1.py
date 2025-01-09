import sys
import subprocess 

hash=sys.argv[1]

file1=sys.argv[2]

file2=sys.argv[3]

res1=subprocess.run([hash,file1],stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)

res2=subprocess.run([hash,file2],stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)

if(res1.stdout.split()[0]==res2.stdout.split()[0]):

      print("hash is same")

else:

      print("hash is not same")

#code for terminal
#python3 q1.py sha256sum file1.txt file2.txt
