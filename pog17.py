import subprocess

import re

import csv



def scan_ip_mac_and_ports_status(network_range, ports=[22, 80, 81, 135, 139, 445, 1433]):

  try:

    # Convert ports list to a comma-separated string

    ports_str = ",".join(map(str, ports))



    # Run the nmap command to scan IP, MAC, and port statuses

    result = subprocess.run(

      ["sudo", "nmap", "-p", ports_str, network_range],

      stdout=subprocess.PIPE,

      stderr=subprocess.PIPE,

      text=True

    )



    if result.returncode != 0:

      print("Error running nmap:", result.stderr)

      return []



    # Regex patterns

    ip_regex = r"Nmap scan report for ([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)"

    mac_regex = r"MAC Address: ([0-9A-Fa-f:]+)"

    port_status_regex = r"(\d+)/tcp\s+(\w+)\s+(\S+)" # This captures status and service



    devices = []

    ip_address = None

    mac_address = None

    port_status = {str(port): "not found" for port in ports} # Initialize with "not found"

    # services = {str(port): "not found" for port in ports} # Initialize with "not found"

    # Parse the nmap output

    for line in result.stdout.splitlines():

      ip_match = re.search(ip_regex, line)

      mac_match = re.search(mac_regex, line)

      port_status_match = re.search(port_status_regex, line)



      if ip_match:

        # Save current device directly as each IP is unique

        ip_address = ip_match.group(1)



        # Reset MAC and port status for next IP

        mac_address = None

        port_status = {str(port): "not found" for port in ports}



      if mac_match:

        mac_address = mac_match.group(1)



      if port_status_match:

        port = port_status_match.group(1)

        status = port_status_match.group(2)

        service = port_status_match.group(3)

        if port in port_status: # Only consider specified ports

          port_status[port] = {"STATE": status, "SERVICE": service}



      # Once all data is gathered for the device, append to the list

      if ip_address and mac_address:

        devices.append({

          "IP": ip_address,

          "MAC": mac_address if mac_address else "Unknown",

          **port_status,

        })



        ip_address = None

        mac_address = None

        port_status = {str(port): "not found" for port in ports}



    return devices



  except Exception as e:

    print("An error occurred:", str(e))

    return []





def savedthe_file(devices):

  fieldnames = ["IP", "MAC", "22", "80", "81", "135", "139", "445", "1433"]

  with open('output.csv', 'w', newline='') as log_file:

    writer = csv.DictWriter(log_file, fieldnames=fieldnames)

    writer.writeheader()

    for device in devices:

      writer.writerow(device)



# Example usage

network = "172.17.156.58/24" # Replace with your network range

ports = [22, 80, 81, 135, 139, 445, 1433] # List of ports to scan

devices = scan_ip_mac_and_ports_status(network, ports)



# If devices are found, print them and save to a CSV file

if devices:

  print("Discovered devices and their port statuses:")

  for device in devices:

    print(device) # Print each device

  savedthe_file(devices) 

else:

  print("No devices found.")