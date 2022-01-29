# -*- coding:utf-8 -*-
from PyQt4 import QtCore,QtGui
from gui import Ui_MainWindow
import sys,os,time
import configparser
from configobj import *
from wifi_tool import WiFi_tool

def get_file_path():
    path=sys.path[0]
    if os.path.isdir(path):
         return path
    elif os.path.isfile(path):
         return os.path.dirname(path)

path = get_file_path()
print(path)
result_path = os.path.join(path,'result')

def parser_cfg(filename):
    kargs={}
    cfg=configparser.ConfigParser()
    cfg.read(filename.replace("\\","/"))
    for opt in cfg.sections():
        if opt:
            kargs[opt]={}
    for opt in kargs.keys():
        for k,v in cfg.items(opt):
            kargs[opt][k]=v
    return kargs
    
class MainWindow(QtGui.QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.read_cfg()
        self.init_cfg()
        #对button进行处理
        self.connect(self.ui.connect,QtCore.SIGNAL('clicked()'),self.connect_wifi)
        self.connect(self.ui.disconnect,QtCore.SIGNAL('clicked()'),self.disconnect_wifi)
        self.connect(self.ui.test,QtCore.SIGNAL('clicked()'),self.test_wifi)
        self.connect(self.ui.help,QtCore.SIGNAL('triggered()'),self.about)
        
        self.interface_name()
        self.current_ssid()
        
    def init_cfg(self):
        self.ui.ssid.setText(self.config_dict['config']['ssid'])
        self.ui.password.setText(self.config_dict['config']['password'])
        self.ui.time.setText(self.config_dict['config']['time'])
        self.ui.cur_ssid.setText(self.config_dict['config']['cur_ssid'])
        self.ui.interface_name.setText(self.config_dict['config']['interface_name'])
        self.ui.frequency.setText(self.config_dict['config']['frequency'])
        
    def read_cfg(self,filename='config.ini'):
        basepath=get_file_path()
        print('****%s'% basepath)
        self.cfg_file=os.path.join(basepath,filename)
        print(self.cfg_file)
        self.config_dict = parser_cfg(self.cfg_file)
        
    def save_cfg(self):
        #先把以前的信息读取出来,然后保存成字典,然后把GUI上有的参数替换掉,没有的参数不操作
        init_dict=parser_cfg(self.cfg_file)
        gui_dict={}
        gui_dict['config']={}
        gui_dict['config']['ssid']=self.ui.ssid.text()
        gui_dict['config']['password']=self.ui.password.text()
        gui_dict['config']['time']=self.ui.time.text()
        gui_dict['config']['frequency']=self.ui.frequency.text()
        
        cfg=configparser.ConfigParser()    
        for key,value in init_dict.items():
            cfg.add_section(key)
            for k,v in value.items():
                if key in gui_dict:
                    if k in gui_dict[key]:
                        cfg.set(key, k, gui_dict[key][k])
                        continue
                cfg.set(key, k, v)
        with open(self.cfg_file.replace("\\","/"),"w+") as f:
            cfg.write(f)
        self.config_dict =  parser_cfg(self.cfg_file)
        self.showstate(u"保存配置成功！")
        
        
    def connect_wifi(self):
        self.save_cfg()
        self.read_cfg()
        time.sleep(1)
        self.con_wifi=WiFi_Connect(self)
        self.con_wifi.conn_signal.connect(self.show_curr_ssid)
        self.con_wifi.start_test()
        
        
    def disconnect_wifi(self):
        self.showstate(u"断开无线连接")
        self.dis_wifi=WiFi_Disconnect(self)
        self.dis_wifi.dis_signal.connect(self.show_curr_ssid)
        self.dis_wifi.start_test()
    
    def test_wifi(self):
        self.save_cfg()
        self.read_cfg()
        self._test=WiFi_Test(self)
        self._test.log_signal.connect(self.show_log)
        self._test.start_test()
        
    #显示无线接口名
    def interface_name(self):
        self._name=WiFi_tool().get_interface_name()
        print(self._name)
        self.config_dict['config']['interface_name']=self._name
        msg=self.config_dict['config']['interface_name']
        self.ui.interface_name.setText(msg)
    #显示当前已连接SSID
    def current_ssid(self):
        _ssid=WiFi_tool().get_current_ssid()
        print(_ssid)
        self.config_dict['config']['cur_ssid']=_ssid
        msg=self.config_dict['config']['cur_ssid']
        self.ui.cur_ssid.setText(msg)
    def show_curr_ssid(self,msg):
        self.ui.cur_ssid.setText(msg)
    #显示状态栏
    def showstate(self,msg):
        self.ui.statusbar.showMessage(msg)
    #显示日志打印    
    def show_log(self,msg):
        self.ui.log_text.setText(msg)
    #显示帮助信息
    def about(self):
        QtGui.QMessageBox.about(self,u"帮助信息",u"Auther：FanHao\n1、工具默认加密方式为WPA2-PSK/AES，输入SSID和password，点击connect按钮能够自动连接无线。点击disconnect按钮能够断开无线连接。\n2、右边test按钮主要用来测试：时间间隔为Time时，无线网卡自动连接与断开。Frequency代表测试次数。\n3、当Time为0时，点击test按钮，工具不会进行无线自动连接与断开测试，后台只会一直发ping包。")
    def closeEvent(self,event):
        reply = QtGui.QMessageBox.question(self,'Message','Are you sure to quit?',QtGui.QMessageBox.Yes,QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        
class WiFi_Connect(QtCore.QThread):
    conn_signal=QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(WiFi_Connect,self).__init__(parent)
        self.parent=parent
        self.start_flag=0
    def start_test(self):
        self.start()
    def stop_test(self):
        self.terminate()
        self.wait()
    def run(self):
        # self.parent.showstate('Connecting WiFi')
        #获取参数
        wifi_ssid=self.parent.config_dict['config']['ssid']
        wifi_pwd=self.parent.config_dict['config']['password']
        #初始化无线工具对象
        connect=WiFi_tool()
        t=connect.connect_wifi(wifi_ssid,wifi_pwd)
        # self.conn_signal.emit(t)
        time.sleep(0.2)
        if t:
            cur_ssid=connect.get_current_ssid()
            # print(cur_ssid)
            self.conn_signal.emit(cur_ssid)
            time.sleep(0.2)
            self.parent.showstate(u'Connected WiFi')
        else:
            self.parent.showstate(u'Connect WiFi Failed')
class WiFi_Disconnect(QtCore.QThread):
    dis_signal=QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(WiFi_Disconnect,self).__init__(parent)
        self.parent=parent
        self.start_flag=0
    def start_test(self):
        self.start()
    def stop_test(self):
        self.terminate()
        self.wait()
    def run(self):
        self.parent.showstate('Disonnecting WiFi')
        #初始化无线工具对象
        connect=WiFi_tool()
        re=connect.disconnect_wifi()
        time.sleep(0.2)
        if re:
            cur_ssid=connect.get_current_ssid()
            self.dis_signal.emit(cur_ssid)
            time.sleep(0.2)
            self.parent.showstate(u'Disconnected WiFi')        
#无线自动连接/ping包/断开子线程
class WiFi_Test(QtCore.QThread):
    log_signal=QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(WiFi_Test,self).__init__(parent)
        self.parent=parent
        self.start_flag=0
    def start_test(self):
        self.start()
    def stop_test(self):
        self.terminate()
        self.wait()
    def run(self):
        self.parent.showstate('Test wireless auto connect or disconnect')
        #获取参数
        wifi_ssid=self.parent.config_dict['config']['ssid']
        wifi_pwd=self.parent.config_dict['config']['password']
        wifi_n=int(self.parent.config_dict['config']['frequency'])
        wifi_time=int(self.parent.config_dict['config']['time'])
        #初始化对象
        wifi_test=WiFi_tool()
        if wifi_time==0 or wifi_n==0:
            self.parent.showstate(u'time=0或者frequency=0时，客户端工具不会测试无线自动连接断开')
        else:
            i=1
            while i<=wifi_n:
                wifi_test.connect_wifi(wifi_ssid,wifi_pwd)
                msg=wifi_test.sys_ping(wifi_time)
                self.log_signal.emit(msg)
                time.sleep(wifi_time)
                wifi_test.disconnect_wifi()
                i=i+1
#无线扫描子线程    
class WiFi_Scan(QtCore.QThread):
    scan_signal=QtCore.pyqtSignal(str)
    def __init__(self,parent=None):
        super(WiFi_Disconnect,self).__init__(parent)
        self.parent=parent
        self.start_flag=0
    def start_test(self):
        self.start()
    def stop_test(self):
        self.terminate()
        self.wait()
    def run(self):
        self.parent.showstate('Scaning WiFi')
        #初始化无线工具对象
        Scan=WiFi_tool()
        re=connect.scan_wifi()
        time.sleep(0.2)
        
        self.scan_signal.emit(re)
        time.sleep(0.2)
        self.parent.showstate(u'Scan WiFi Complete')

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    wm=MainWindow()
    wm.show()
    sys.exit(app.exec_())