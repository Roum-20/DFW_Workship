import re

from collections import defaultdict

from datetime import datetime

logfile_path = '/home/kali/prog9.log'

clients = set()

servers = set()

communications = set()

server_ports = []

client_ports = []

os_detected = set()

timestamps = []

with open(logfile_path, 'r') as file:

  for line in file:

    # Assuming log format: timestamp client_ip:client_port server_ip:server_port OS

    match = re.match(r'(\S+ \S+) (\S+):(\d+) (\S+):(\d+) (\S+)', line)

    if match:

      timestamp_str, client_ip, client_port, server_ip, server_port, os_info = match.groups()

       

      clients.add((client_ip, client_port))

      servers.add((server_ip, server_port))

      communications.add((client_ip, client_port, server_ip, server_port))

      server_ports.append(server_port)

      client_ports.append(client_port)

      os_detected.add(os_info)

      timestamps.append(datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S"))


unique_clients_count = len(clients)

unique_servers_count = len(servers)

unique_communications_count = len(communications)

unique_server_ports_count = len(set(server_ports))

unique_client_ports_count = len(set(client_ports))


port_usage = defaultdict(int)

for port in server_ports + client_ports:

  port_usage[port] += 1


most_used_port = max(port_usage, key=port_usage.get) if port_usage else None

least_used_port = min(port_usage, key=port_usage.get) if port_usage else None


latest_timestamp = max(timestamps) if timestamps else None

oldest_timestamp = min(timestamps) if timestamps else None

print(f"**Unique Clients Count:** {unique_clients_count}")

print(f"**Unique Servers Count:** {unique_servers_count}")

print(f"**Unique Server-Client Communications Count:** {unique_communications_count}")

print(f"**Unique Server Ports Count:** {unique_server_ports_count}")

print(f"**Unique Client Ports Count:** {unique_client_ports_count}")

print(f"**Most Used Port:** {most_used_port if most_used_port else 'N/A'}")

print(f"**Least Used Port:** {least_used_port if least_used_port else 'N/A'}")

print(f"**Latest Packet Timestamp:** {latest_timestamp if latest_timestamp else 'N/A'}")

print(f"**Oldest Packet Timestamp:** {oldest_timestamp if oldest_timestamp else 'N/A'}")

print(f"**Detected Operating Systems:** {', '.join(os_detected) if os_detected else 'N/A'}")


client_activity = defaultdict(int)

for client_ip, client_port in clients:

  client_activity[(client_ip, client_port)] += 1

longest_active_client = max(client_activity.items(), key=lambda item: item[1], default=(None, 0))

if longest_active_client[0]:

  print(f"**Longest Active Client IP and Port:** {longest_active_client[0][0]}:{longest_active_client[0][1]} with {longest_active_client[1]} packets")

else:

  print("**Longest Active Client IP and Port:** N/A")
  #log will iput will be provided
