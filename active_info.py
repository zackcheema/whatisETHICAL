import nmap
import sys
import time

nm_scan = nmap.PortScanner()

print('\nRunning...\n')

nm_scanner =  nm_scan.scan(sys.argv[1], '80', arguments ='-O')

host_is = "The host is: "+nm_scanner['scan'][sys.argv[1]]['status']['state']+".\n"
port_is = "The port 80 is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"
method_is = "The method of scanning is: "+nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"
os_assessment = "OS check: \nThere is a %s percent chance that the host is running %s"%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'], nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+".\n"

with open('%s.txt'%sys.argv[1], 'w') as f:
    f.write(host_is+port_is+method_is+os_assessment)
    f.write("\nReport Generated at "+time.strftime('%Y-%M-%D_%H:%M:%S GMT', time.gmtime()))

print("\nScan Complete!")