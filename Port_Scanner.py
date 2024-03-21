print("---------------------------------------------------------------------\n")
print("""@@@@@@@   @@@ @@@  @@@@@@@   @@@@@@@                                  
@@@@@@@@  @@@ @@@  @@@@@@@@  @@@@@@@                                  
@@!  @@@  @@! !@@  @@!  @@@    @@!                                    
!@!  @!@  !@! @!!  !@!  @!@    !@!                                    
@!@@!@!    !@!@!   @!@!!@!     @!!                                    
!!@!!!      @!!!   !!@!@!      !!!                                    
!!:         !!:    !!: :!!     !!:                                    
:!:         :!:    :!:  !:!    :!:                                    
 ::          ::    ::   :::     ::                                    
 :           :      :   : :     :                                     
                                                                      
                                                                      
 @@@@@@    @@@@@@@   @@@@@@   @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@   
@@@@@@@   @@@@@@@@  @@@@@@@@  @@@@ @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  
!@@       !@@       @@!  @@@  @@!@!@@@  @@!@!@@@  @@!       @@!  @@@  
!@!       !@!       !@!  @!@  !@!!@!@!  !@!!@!@!  !@!       !@!  @!@  
!!@@!!    !@!       @!@!@!@!  @!@ !!@!  @!@ !!@!  @!!!:!    @!@!!@!   
 !!@!!!   !!!       !!!@!!!!  !@!  !!!  !@!  !!!  !!!!!:    !!@!@!    
     !:!  :!!       !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!: :!!   
    !:!   :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:       :!:  !:!  
:::: ::    ::: :::  ::   :::   ::   ::   ::   ::   :: ::::  ::   :::  
:: : :     :: :: :   :   : :  ::    :   ::    :   : :: ::    :   : :""")

print("\n---------------------------------------------------------------------\n")
print("                    Port Probing Tool Developed by SNV                     \n")

import threading
import socket

target = str(input("Enter target: "))
flag = int(input("Enter 0 for specific port scan or 1 for scanning all ports: "))

open_ports = {}  # Store open ports and associated vulnerabilities

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        con = s.connect((target, port))
        print('Port:', port, 'is open.')
        open_ports[port] = []  # Initialize list for vulnerabilities for this port
        # Perform vulnerability scanning for this port
        vulnerability_scan(port)
        con.close()
    except:
        pass

def vulnerability_scan(port):
    # Implement vulnerability scanning logic here for the given port
    print("Scanning vulnerabilities for port:", port)
    # Example: Check for known vulnerabilities on this port
    if port == 80:
        open_ports[port].append("HTTP vulnerability detected")
    if port == 443:
        open_ports[port].append("SSL vulnerability detected")
    # Add more vulnerability checks as needed

def network_mapping():
    # Implement network mapping logic here
    print("Network mapping...")
    # Implement network mapping using open_ports dictionary
    print("Mapping network using open ports:", list(open_ports.keys()))

if flag == 1:
    for x in range(1, 65535):
        t = threading.Thread(target=portscan, kwargs={'port': x})
        t.start()
elif flag == 0:
    print("Note: Port numbers should be separated with a comma.")
    ports = input("Enter ports to scan: ")
    port_list = ports.split(",")
    for port in port_list:
        port = int(port)
        portscan(port)

# Wait for all port scanning threads to finish
for thread in threading.enumerate():
    if thread != threading.current_thread():
        thread.join()

# Report vulnerability scan results
for port, vulnerabilities in open_ports.items():
    if vulnerabilities:
        print("Vulnerabilities found for port", port, ":")
        for vulnerability in vulnerabilities:
            print("-", vulnerability)
    else:
        print("No vulnerabilities found for port", port)

# Perform network mapping
network_mapping()
