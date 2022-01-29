# -*- coding:utf-8 -*-
import sys
import os
import time
import pywifi
from pywifi import const

#WIFI工具模拟客户端自动连接断开
class WiFi_tool(object):

    def __init__(self):
        #获取无线接口，并初始化
        self.wifi=pywifi.PyWiFi()
        self.iface=self.wifi.interfaces()[0]
        # print(self.iface)
    
    def get_interface_name(self):
        #获取当前无线接口名
        self.name=self.iface.name()
        print(self.name)
        return self.name

    def scan_wifi(self):
        # 起始获得的是列表，列表中存放的是无线网卡对象。
        # 可能一台电脑有多个网卡，请注意选择
        # 如果网卡选择错了，程序会卡住，不出结果。
        # ssid 是名称 ，signal 是信号强度
        self.iface.scan()
        time.sleep(3)
        result=self.iface.scan_results()
        # print(result)
        for i in range(len(result)):
            _ssid=result[i].ssid.encode("UTF-8")
            _signal=result[i].signal
            _bssid=result[i].bssid
            print(u'SSID:%s,BSSID:%s,Signal:%s' % (_ssid.decode('UTF-8','strict'),_bssid,_signal))

    def connect_wifi(self,ssid,pwd):
        self.iface.disconnect()
        time.sleep(1)
        profile=pywifi.Profile()
        profile.ssid=ssid
        profile.auth=const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher=const.CIPHER_TYPE_CCMP
        profile.key=pwd
        
        self.iface.remove_all_network_profiles()
        tmp_profile=self.iface.add_network_profile(profile)
        
        self.iface.connect(tmp_profile)
        time.sleep(8)
        
        if self.iface.status() == const.IFACE_CONNECTED:
            # return u'无线网卡已成功连接SSID'
            print(u'连接SSID成功')
            return True
        else:
            # return u'无线网卡连接SSID失败'
            print(u'连接SSID失败')
            return False
    
    def disconnect_wifi(self):
        #断开无线连接
        self.iface.disconnect()
        if self.iface.status() == const.IFACE_DISCONNECTED:
            print(u'断开WIFI连接成功')
            return True
        else:
            print(u'断开WIFI连接失败')
            return False

    def get_current_ssid(self):
        # result=os.system(u"netsh wlan show interfaces")
        result=os.popen(u"netsh wlan show interfaces |findstr SSID")
        #切割字符串
        text_str=result.read().split('\n')[0].split(' ')[-1].strip()
        # print(text_str)
        return text_str
    
    def sys_ping(self,n):
        #ping设备LAN IP，检测是否连接成功
        # result=os.system(u'ping 192.168.1.1 -n %s' % n)
        re=os.popen(u'ping 192.168.1.1 -n %s' % n)
        text_str=re.read().strip()
        return text_str

    # def test_wifi(self,time,f):
    #     i=0
    #     while i<= f:
    #         self.connect_wifi(ssid,pwd)
    #         # time.sleep(time)
    #         self.sys_ping(time)
    #         self.diconnect_wifi()
    #         f=f+1

# class WRLO:
    # def write(self,msg):    
        # fd = open("log.log",'a+')
        # fd.write(msg)
        #fd.flush()
        
if __name__ == "__main__":
    test=WiFi_tool()
    # test.scan_wifi()
    # test.get_interface_name()
    # test.connect_wifi(ssid='WiFi-Test',pwd='12345678')
    test.get_current_ssid()
    # test.test_wifi(time=5,f=3)
    # sys.stdout = WRLO()
    # test.sys_ping(n=5)
    # get_current_ssid()