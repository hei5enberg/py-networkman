#!/usr/bin/python
import os

class NetwokManager:
    def __init__(self):
        self.con = {"gprs":"trfl-gprs","wlan":"trfl-wlan","eth":"trfl-eth"}

    def activate_con(self,con):
        if os.system("sudo nmcli con up " + str(self.con[con])) is 0:
            return True
        return False

    def delete_con(self,con):
        if os.system("sudo nmcli con delete " + str(self.con[con])) is 0:
            return True
        return False

    def add_con(self,ctype,conf=None):
        stat = 0
        if ctype == "gprs":
            stat = os.system('sudo nmcli connection add type gsm con-name trfl-gprs ifname "*" apn ' + str(conf["apn"]))
        elif ctype == "wlan":
            stat = os.system('sudo nmcli con add con-name trfl-wlan ifname "*" type wifi ssid ' + str(conf["ssid"]))
            if stat is 0:
                stat = os.system("sudo nmcli con mod trfl-wlan wifi-sec.key-mgmt wpa-psk wifi-sec.psk " + str(conf["pswd"]))
                if stat is 0:
                    if not conf["dhcp"]:
                        stat = os.system('sudo nmcli con mod trfl-wlan ipv4.method manual ipv4.addresses '+str(conf["ip"])+' ipv4.gateway '+str(conf["gateway"])+' ipv4.dns '+str(conf["dns"]))
        elif ctype == "eth":
            stat = os.system('sudo nmcli con add type ethernet con-name trfl-eth ifname "*"')
            if stat is 0:
                if not conf["dhcp"]:
                    stat = os.system('sudo nmcli con mod trfl-eth ipv4.method manual ipv4.addresses '+str(conf["ip"])+' ipv4.gateway '+str(conf["gateway"])+' ipv4.dns '+str(conf["dns"]))
        else:
            print "unknown option ", ctype
            stat = -1
        if stat is 0:
            return True
        return False

    def gprs_set(self,apn):
        self.delete_con("gprs")
        conf = {"apn":apn}
        self.add_con(ctype="gprs", conf=conf)


    def wifi_set(self,ssid,pswd,dhcp=True,ip=None,gateway=None,dns=None):
        self.delete_con("wlan")
        conf = {"ssid":ssid,"pswd":pswd,"dhcp":dhcp,"ip":ip,"gateway":gateway,"dns":dns}
        self.add_con(ctype="wlan", conf=conf)

    def eth_set(self,dhcp=True,ip=None,gateway=None,dns=None):
        self.delete_con("eth")
        conf = {"dhcp":dhcp, "ip":ip, "gateway":gateway,"dns":dns}
        self.add_con(ctype="eth", conf=conf)


if __name__ == "__main__":
    nm = NetwokManager()
    # nm.delete_con("gprs")
    # nm.wifi_set("TRFL","trfl@123",dhcp=True)
    # nm.eth_set(False,"192.168.0.122/24","192.168.0.1",'"8.8.8.8 8.8.4.4"')
    # nm.wifi_set("TRFL","trfl@123",False,"192.168.0.219/24","192.168.0.1",'"8.8.8.8 8.8.4.4"')
    # nm.wifi_set("TRFL","trfl@123")
    nm.wifi_set("TRFL","trfl@123")
    # nm.gprs_set("aircelgprs")
    nm.activate_con("wlan")
    # nm.eth_set()
