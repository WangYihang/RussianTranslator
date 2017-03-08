#!/usr/bin/env python
# encoding:utf8

import os
import shutil
import ConfigParser
import getpass


# global-start
configParser = ConfigParser.SafeConfigParser()
installPath = "/opt/rufy/"
# global-end


def getConfigParser():
    global configParser
    configParser.read("./Config/config.conf")
    return configParser


def copyFile(src, dst):
    srcFile = open(src, "r")
    dstFile = open(dst, "w")
    for line in srcFile:
        dstFile.write(line)
    dstFile.close()
    srcFile.close()


def showSuccess():
    print "安装完成 , 请输入 : 'rufy help' 进行测试"


def showHelp():
    print "请您以管理员的身份运行 , 如果您并没有这样做 , 安装可能会失败"
    print "如果您确保您已经以管理员的身份运行了该脚本 , 请您输入 y 以继续安装"
    print "如果您并不确定 , 请您输入 n 结束脚本 , 然后使用sudo以管理员的身份运行"
    choice = ""
    while choice == "":
        choice = raw_input("请选择 : ")
        if choice.startswith('y') or choice.startswith('Y'):
            return True


def getCurrentDicName():
    temp = os.getcwd()
    return temp.split("/")[-1]

def main():
    if not showHelp():
        exit(1)
    global configParser
    copyFile("./Config/config.example.conf", "./Config/config.conf")
    configParser = getConfigParser()
    # 先删除之前的安装
    os.system("sudo rm -rf /opt/rufy/")
    os.system("sudo rm /bin/rufy")
    # 开始安装
    os.system("pip install -r requirements.txt")
    currentDicName = getCurrentDicName()
    shutil.copytree("../" + currentDicName, installPath)
    # create a soft link
    os.system("ln -s " + installPath + "rufy" + " /bin/rufy")
    showSuccess()


if __name__ == '__main__':
    main()
