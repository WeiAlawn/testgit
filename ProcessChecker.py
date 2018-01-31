#!/usr/bin/env python
# _*_encoding: utf-8_*_

"""
@version: 
@author: Alawn
@license: Apache Licence 
@file: ProcessChecker.py
@time: 2018/1/29 9:05
"""
import win32com.client


def check_exist(process_name):
    WMI = win32com.client.GetObject('winmgmts:')
    processCodeCov = WMI.ExecQuery('select * from Win32_process WHERE  Name ="%s"' % process_name)
    if len(processCodeCov) > 0:
        print "%s is exists" % process_name
    else:
        print "%s is not exists" % process_name


if __name__ == '__main__':
    check_exist('pycharm.exe')
