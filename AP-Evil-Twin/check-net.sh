ifconfig wlan1 
route -n
echo '\n'
sysctl net.ipv4.ip_forward 
echo '\n'
iptables -t nat -L
echo '\n'
ps -ef | grep -v 'grep' | grep -e 'dnsmasq'
ps -ef | grep -v 'grep' | grep -e 'hostapd'
echo '\n'
netstat -lptun
