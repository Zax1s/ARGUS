import socket

def IPFinder(subdomainName):
    try:
        addr_info = socket.getaddrinfo(subdomainName, None)
        ips = [info[4][0] for info in addr_info]
    except Exception as e:
        return None
    return(ips)