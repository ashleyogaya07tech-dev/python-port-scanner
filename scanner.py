import socket
import sys

# ============================================================
# SIMPLE PORT SCANNER - CYBERSECURITY LEARNING PROJECT
# ============================================================
# This program scans for open ports on a target IP address.
# It uses the socket library to attempt connections to each
# port. If a connection succeeds, the port is marked as open.
# ============================================================

print("=" * 60)
print("       CYBERSECURITY PYTHON PROJECT - PORT SCANNER")
print("=" * 60)
print("\nThis tool will scan ports 1-1024 on a target IP address.")
print("To scan your local machine, use: 127.0.0.1\n")

# ============================================================
# STEP 1: GET TARGET IP ADDRESS FROM USER
# ============================================================
target = input("Enter target IP address (e.g., 127.0.0.1): ").strip()

# If user enters nothing, show error and exit
if not target:
    print("[ERROR] No IP address provided. Exiting...")
    sys.exit(1)

# ============================================================
# STEP 2: VALIDATE THE IP ADDRESS
# ============================================================
# The socket.inet_aton() function checks if the IP is valid
# Valid format: XXX.XXX.XXX.XXX (where X is 0-255)
try:
    socket.inet_aton(target)
except socket.error:
    print(f"[ERROR] '{target}' is not a valid IP address.")
    print("Please use format: 192.168.1.1 or 127.0.0.1")
    sys.exit(1)

print(f"\n[INFO] Target IP: {target}")
print("[INFO] Scanning ports 1-1024...")
print("[INFO] This may take a minute. Please wait...\n")

# ============================================================
# STEP 3: CREATE A LIST TO STORE OPEN PORTS
# ============================================================
open_ports = []

# ============================================================
# STEP 4: SCAN EACH PORT
# ============================================================
try:
    for port in range(1, 1025):
        # Create a socket object
        # AF_INET = Internet Protocol (IPv4)
        # SOCK_STREAM = TCP (for connection-oriented communication)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set timeout to 0.3 seconds (keeps scan fast)
        # If no response in 0.3s, we assume port is closed
        s.settimeout(0.3)

        # connect_ex() attempts to connect without raising exceptions
        # Returns 0 if connection successful, non-zero otherwise
        result = s.connect_ex((target, port))

        # If result is 0, port is open/reachable
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        # Close the socket to free up resources
        s.close()

    # ========================================================
    # STEP 5: DISPLAY SCAN RESULTS
    # ========================================================
    print("\n" + "=" * 60)
    print(f"[SUCCESS] Scan complete!")
    print(f"[RESULT] Found {len(open_ports)} open port(s)")
    
    if open_ports:
        ports_str = ", ".join(map(str, open_ports))
        print(f"[PORTS] {ports_str}")
    else:
        print("[INFO] No open ports found in the range 1-1024")
    
    print("=" * 60)

# ============================================================
# STEP 6: ERROR HANDLING
# ============================================================
# Handle user interruption (Ctrl+C)
except KeyboardInterrupt:
    print("\n")
    print("[WARNING] Scan interrupted by user (Ctrl+C pressed)")
    if open_ports:
        print(f"[INFO] Open ports found before interruption: {open_ports}")
    sys.exit(1)

# Handle hostname resolution errors
except socket.gaierror:
    print("\n[ERROR] Hostname could not be resolved")
    sys.exit(1)

# Handle other socket errors
except socket.error as e:
    print(f"\n[ERROR] Socket error occurred: {e}")
    sys.exit(1)