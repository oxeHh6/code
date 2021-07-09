#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    #得到当前工作目录
    cwd = os.getcwd()
    print("current working directory is " +cwd)

    #检验给出的路径是否是一个文件/目录：
    print(os.path.isfile("c:\\users\\ryan\\calc.exe"))
    print(os.path.isdir("c:\\users\\ryan\\"))

    # 检验给出的路径是否是一个绝对路径：
    print(os.path.isabs("c:\\users\\ryan\\calc.exe"))

    #检验给出的路径是否真地存:
    print(os.path.exists("c:\\a.txt"))

    #返回一个路径的目录名和文件名:
    ret = os.path.split("c:\\users\\ryan\\calc.exe")
    print(type(ret))
    print(ret)

    #分离扩展名：
    ret = os.path.splitext("a.txt")
    print(ret)
    ret = os.path.splitext("c:\\users\\ryan\\calc.exe")
    print(ret)

    #获取路径名：
    ret = os.path.dirname("c:\\users\\ryan\\calc.exe")
    print(ret)

    #获取文件名：
    ret = os.path.basename("c:\\users\\ryan\\calc.exe")
    print(ret)

    #运行shell命令:
    #os.system("calc.exe")

    #读取和设置环境变量:
    ret = os.getenv("PATH")
    print(ret)

    for key in os.environ.keys():
        #print(key)
        print(os.environ.get(key))

    #设置环境变量
    dir = "〜/Dev/pyitem/"
    os.environ['project_path'] = dir
    print(os.environ.get('project_path'))

    os.putenv("myenv", "test")
    print(os.getenv("myenv"))   #putenv 无效，使用上面的方法设置




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
