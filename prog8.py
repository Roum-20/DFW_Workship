import re
from datetime import datetime

# Path to the p0f log file
log_file = "/home/kali/prog_8log.txt"

# Initialize sets for unique servers, clients, and ports
unique_servers = set()
unique_clients = set()
server_client_pairs = set()
unique_server_ports = set()
unique_client_ports = set()

# Initialize variables for the oldest and most recent packet timestamps
oldest_packet = None
most_recent_packet = None

# Read the p0f log file line by line
with open(log_file, 'r') as file:
    for line in file:
        # Extract server and client IPs
        server_match = re.search(r"srv=([0-9\.]+)", line)
        client_match = re.search(r"cli=([0-9\.]+)", line)
        if server_match and client_match:
            server_ip = server_match.group(1)
            client_ip = client_match.group(1)
            unique_servers.add(server_ip)
            unique_clients.add(client_ip)
            server_client_pairs.add((client_ip, server_ip))

        # Extract server and client ports
        server_port_match = re.search(r"sport=([0-9]+)", line)
        client_port_match = re.search(r"dport=([0-9]+)", line)
        if server_port_match:
            unique_server_ports.add(server_port_match.group(1))
        if client_port_match:
            unique_client_ports.add(client_port_match.group(1))

        # Extract timestamps
        timestamp_match = re.search(r"ts=([0-9\-: ]+)", line)
        if timestamp_match:
            timestamp = datetime.strptime(timestamp_match.group(1), "%Y-%m-%d %H:%M:%S")
            if oldest_packet is None or timestamp < oldest_packet:
                oldest_packet = timestamp
            if most_recent_packet is None or timestamp > most_recent_packet:
                most_recent_packet = timestamp

# Print the results
print(f"Number of unique servers: {len(unique_servers)}")
print(f"Number of unique clients: {len(unique_clients)}")
print(f"Number of unique server-client communications: {len(server_client_pairs)}")
print(f"Number of unique server ports: {len(unique_server_ports)}")
print(f"Number of unique client ports: {len(unique_client_ports)}")
print(f"Most recent packet timestamp: {most_recent_packet}")
print(f"Oldest packet timestamp: {oldest_packet}")

#run p0f -i eth in terminal save the result in txt file give that txt file in path in py code 
#python3 q8.py
