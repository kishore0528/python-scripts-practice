import socket
import threading as th

def port_scan(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    result = s.connect_ex((ip, port))

    if not result:
        try:
            banner = s.recv(1024)
            print(f"Port {port} is OPEN. Banner: {banner.decode().strip()}")
        except:
            print(f"Port {port} is OPEN but silent.")

    s.close()

threads = []
ports = [21, 22, 53, 80, 443, 223]

for port in ports:
    t = th.Thread(target=port_scan, args=("100.125.147.99", port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Scan complete!")
