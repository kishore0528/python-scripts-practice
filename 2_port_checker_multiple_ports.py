import socket  

def check_port(ip, port):
    # 1. Create a socket object
    # AF_INET means IPv4, SOCK_STREAM means TCP (the reliable connection)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # 2. Set a timeout so we don't wait forever (1 second is plenty)
    s.settimeout(1)
    
    # 3. Try to connect! 
    # The method s.connect_ex((ip, port)) returns 0 if successful
    result = s.connect_ex((ip, port))
    
    # --- YOUR TURN ---
    # Use an 'if' statement here:
    # If result is 0, print "Port is open!"
    # Otherwise, print "Port is closed."
    if result == 0:
        print("Portal is open!")
    else:
        print("The portal is closed.")
    
    # 4. Always close the connection
    s.close()

# Test it on Google's web server (IP: 8.8.8.8, Port: 80)
for port in range(20,26):
    check_port("8.8.8.8", port)