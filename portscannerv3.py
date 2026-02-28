import nmap

nm = nmap.PortScanner()
# That's an internal IP, please double check
target = "google.com"
options = "-sV -sC"

nm.scan(target, arguments=options)

for host in nm.all_hosts():
    print(f"Host: {host} ({nm[host].hostname()})")
    print(f"State: {nm[host].state()}")
    for protocol in nm[host].all_protocols():
        print(f"Protocol: {protocol}")
        port_info = nm[host][protocol]
        for port, data in port_info.items():
            print(f"Port: {port}\tState: {data['state']}")
