#!/usr/bin/python2  -tt
import os
def start_service(add):
        os.system("dialog --infobox 'processing please wait...' 3 34")
        os.system("ssh %s yum install hadoop jdk -y  > /dev/null"%add)
        os.system("dialog --infobox 'processing please wait...' 3 34")
        os.system("ssh %s iptables -F > /dev/null"%add)
        os.system("ssh %s setenforce 0 > /dev/null"%add)
        os.system("ssh %s service iptables save > /dev/null"%add)
        os.system("ssh %s echo Y | hadoop namenode -format  > /dev/null"%add)
        os.system("dialog --infobox 'processing please wait...' 3 34")
        os.system("ssh %s hadoop-daemon.sh stop namenode > /dev/null"%add)
        os.system("ssh %s hadoop-daemon.sh start namenode > /dev/null"%add)
        os.system("ssh %s hadoop-daemon.sh stop jobtracker > /dev/null"%add)
        os.system("ssh %s hadoop-daemon.sh start jobtracker > /dev/null"%add)

