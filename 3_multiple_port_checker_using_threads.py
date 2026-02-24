import socket 
import threading as th

def port_check(ip,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))
    if result == 0:
        print(f"Port: {port} is open!")

    s.close()

threads = []

for port in range(1,1024):
    t = th.Thread(target=port_check, args=("8.8.8.8",port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Scan complete!")




