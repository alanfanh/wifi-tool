#encoding=utf-8
from distutils.core import setup
import sys
import py2exe

#this allows to run it with a simple double click.
sys.argv.append('py2exe')
#python setup.py py2exe 执行左侧命令使代码生成exe可执行文件
#如果显示错误提示的话 “ msvcp90.dll: no such file or directory”，使用"dll_excludes": ["MSVCP90.dll"]
#bundle_files值为1表示pyd和dll文件会被打包到单文件中，且不能从文件系统中加载python模块；值为2表示pyd和dll文件会被打包到单文件中，但是可以从文件系统中加载python模块。
options = {
        "includes": ["sip"],  #pyQt程序打包时需要添加的，如果不是PyQt程序不需要此项。
        "dll_excludes": ["MSVCP90.dll"],
        "compressed": 0,      #为1，则压缩文件
        "optimize": 2,        #optimize”为优化级别，默认为0。
        "ascii": 0,       #不自动包含encodings和codecs。
        # "bundle_files": 1, 
        }
#bundle_files指将程序打包成单文件（此时除了exe文件外，还会生成一个zip文件。如果不需要zip文件，
        # 还需要设置zipfile=None）。1表示pyd和dll文件会被打包到单文件中，且不能从文件系统中加载python模
        # 块;值为2表示pyd和dll文件会被打包到单文件中，但是可以从文件系统中加载python模块。64位的Py2exe不
        # 要添加本句。
setup(
      name = 'WiFi_Tool',
      version = '1.0.0',
      windows = [{"script":'MainGui.py'}], 
      zipfile = None,    
      options = {'py2exe':options}
      )