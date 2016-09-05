#!/usr/bin/python2 -tt
import os
#*****************************************************************************************

def namenode(add):
        #CORE-SITE.XML
        f=open("/root/Desktop/core-site.xml",'w')
        f.writelines('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>     
<!-- Put site-specific property overrides in this file. -->     
<configuration>
<property>
<name>fs.default.name</name>
<value>hdfs://%s:9001</value>
</property>
</configuration>'''%add)
        f.close()
        #HDFS-SITE.XML
        f=open("/root/Desktop/hdfs-site.xml",'w')
        f.writelines('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>     
<!-- Put site-specific property overrides in this file. -->     
<configuration>
<property>
<name>dfs.name.dir</name>
<value>/hdfsdata</value>
</property>
</configuration>''')
        f.close()
	x=os.system('scp /root/Desktop/{core-site.xml,hdfs-site.xml} root@%s:/etc/hadoop/'%add)
        #x=os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s  'scp /home/dheeraj/Desktop/ip/hadoop-project-master/hadoopdheeraj/{core-site.xml,hdfs-site.xml}  root@%s:/etc/hadoop/   > /dev/null 2>/dev/null' "%add)
        if x==0:
                print"files successfully created"

#namenode format
                os.system('ssh %s hadoop namenode -format  -force'%add)
                #os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no root@%s 'hadoop namenode -format -force >/dev/null 2> /dev/null'"%add)
                os.system('ssh %s hadoop-daemon.sh start namenode'%add)
                #os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no root@%s 'hadoop-daemon.sh start namenode >/dev/null 2>/dev/null'"%add)
                print "namenode created on ip  %s"%add

                print "namenode created check using jps command"

        else:
                print "error creating files on namenode"

