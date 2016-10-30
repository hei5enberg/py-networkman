nmcli
======

adding connections
==================
1. gprs

    nmcli connection add type gsm con-name "trfl-gprs" ifname "*" apn "[apn-name]"

2. wi-fi

nmcli con add con-name "trfl-gprs" ifname wlan0 type wifi ssid "[ssid]" \
ip4 192.168.100.101/24 gw4 192.168.100.1
nmcli con modify "trfl-gprs" wifi-sec.key-mgmt wpa-psk
nmcli con modify "trfl-gprs" wifi-sec.psk "[password]"

nmcli radio wifi [on | off ]

3. ethernet
nmcli con add type ethernet con-name "trfl-eth" ifname "[eth0]" ip4 10.10.10.10/24 \
gw4 10.10.10.254



adding multiple ip to same interface
=============================
ip addr add 192.168.1.1/24 dev eth0
http://askubuntu.com/questions/547289/how-can-i-from-cli-assign-multiple-ip-addresses-to-one-interface

delete connection
=================
nmcli con delete "con-name"
gprs => nmcli con delete "trfl-gprs"
ethernet => nmcli con delete "trfl-eth"
wi-fi => nmcli con delete "trfl-wlan"


modify connection
==================
ethernet / wifi:

change dns:
nmcli con mod test-lab ipv4.dns "8.8.8.8 8.8.4.4"
ipv4.addresses:                         192.168.1.239/24
ipv4.gateway:                           192.168.1.1

wi-fi:
nmcli con modify "[my-wlan]" wifi-sec.key-mgmt wpa-psk
802-11-wireless-security.psk
wifi-sec.psk "[password]"

gprs:
gsm.apn
gsm.number *99#
