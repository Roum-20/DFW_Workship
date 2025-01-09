import re



# Input and output file paths

input_file = "pre_process.csv"



# Regular expression to check if a line s



suspicious_macs=set()

# Open the input file for reading and the output file for writing

with open(input_file, "r") as infile:

  for line in infile:

    # Check if the line starts with a number

      mac_address = line.split()[1]

      vendor_name = line.split()[4]

      if vendor_name not in ["HP", "Dell"]:

        suspicious_macs.add(mac_address)



if suspicious_macs:

  print("Suspicious MAC addresses found:")

  for mac in suspicious_macs:

    print(mac)

else:

  print("No suspicious MAC addresses found.")