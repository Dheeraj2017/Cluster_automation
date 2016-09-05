#!/usr/bin/python2  -tt
import os

def copy(add):
        os.system("ssh %s  rm -rf /datanode  > /dev/null"%add)
        os.system("ssh %s  mkdir /datanode  > /dev/null"%add)
        os.system("scp /root/Desktop/typical/datanode/hdfs-site.xml  root@%s:/etc/hadoop/    > /dev/null"%add)
        os.system("scp /root/Desktop/typical/datanode/core-site.xml  root@%s:/etc/hadoop/   > /dev/null"%add)
        os.system("scp /root/Desktop/typical/datanode/mapred-site.xml  root@%s:/etc/hadoop/   > /dev/null"%add)
