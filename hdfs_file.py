#/usr/bin/python2  -tt
import os

def hdfs_file(ip_addr):
        file_ob=open('hdfs-site.xml','w')
        file_ob.writelines('''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.name.dir</name>
<value>/namenode</value>
</property>
</configuration>
''')
        file_ob.close()
        os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s  'scp /home/dheeraj/Desktop/ip/hadoop-project-master/hadoopdheeraj/hdfs-site.xml  root@%s:/etc/hadoop/   > /dev/null' "%ip_addr)

