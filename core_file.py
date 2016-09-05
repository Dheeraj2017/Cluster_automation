#/usr/bin/python2  -tt
import os
def core_file(ip_addr):
        fobj=open('core-site.xml','w')
        fobj.writelines('''
<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>
'''%ip_addr)
        fobj.close()
        os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s  'scp /home/dheeraj/Desktop/ip/hadoop-project-master/hadoopdheeraj/core-site.xml  root@%s:/etc/hadoop/   > /dev/null' "%ip_addr)

