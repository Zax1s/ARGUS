from subdomainFinder import subdomainFinder
from IPFinder import IPFinder
from IPAnalyser import IPAnalyser
import ipaddress
import time

def main():
    domainName = str(input())
    subdomainList = subdomainFinder(domainName)
    while subdomainList == None:
        print("Connection error. Retrying...")
        time.sleep(5)
        subdomainList = subdomainFinder(domainName)
    IPList = []
    portList = []
    cveList = []

    print("\n", "=" * 40, sep="")

    for i in range(len(subdomainList)):
        print(subdomainList[i])

    print("")

    flag = 0
    
    for i in range(len(subdomainList)):
        IPSmallList = IPFinder(subdomainList[i])
        if IPSmallList == None:
            print(subdomainList[i], "does not exists.")
            flag = 1
            continue
        for j in range(len(IPSmallList)):
            if IPSmallList[j] not in IPList:
                if ":" in IPSmallList[j]:
                    print(f"IPv6 found: {IPSmallList[j]}")
                else:
                    IPList.append(IPSmallList[j])

    IPList = sorted(IPList, key=ipaddress.ip_address)

    resultList = []

    if flag:
        print("")

    print("=" * 40)

    for i in range(len(IPList)):
        result = IPAnalyser(IPList[i])
        if result != None:
            portSmallList = result[0]
            osSmallList = result[1]
            hardwareSmallList = result[2]
            servicesSmallList = result[3]
            cveSmallList = result[4]

            print(f"IP: {IPList[i]}")
            print(f"Open ports:", *portSmallList)
            print(f"OS:", *osSmallList)
            print(f"Hardware:", *hardwareSmallList)
            print(f"Services:", servicesSmallList)
            print(f"CVE list:")
            for j in range(len(cveSmallList)):
                print(cveSmallList[j][0], cveSmallList[j][1], "-", cveSmallList[j][2])
            print("=" * 40)
            resultList.append(list([IPList[i], portSmallList, osSmallList, hardwareSmallList, servicesSmallList, cveSmallList]))
        else:
            print(f"IP: {IPList[i]}")
            print(f"No information available")
            print("=" * 40)
            resultList.append(list([IPList[i], None]))
if __name__ == "__main__":
    main()
