#!/usr/bin/python2  -tt
import os

def datanode(add,job,dat):     #FUNCTION DATANODE
#core-site
        f=open("/root/Music/core-site.xml",'w')
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
        #hdfs-site
        os.system('mkdir -p /datan')
        f=open("/root/Music/hdfs-site.xml",'w')
        f.writelines('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>     
<!-- Put site-specific property overrides in this file. -->     
<configuration>
<property>
<name>dfs.data.dir</name>
<value>/datan</value>
</property>
</configuration>''')
        f.close()
#MAPRED -SITE
        f=open("/root/Music/mapred-site.xml",'w')
        f.writelines('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>     
<!-- Put site-specific property overrides in this file. -->     
<configuration>
<property>
<name>mapred.job.tracker</name>
<value>%s:9002</value>
</property>
</configuration>'''%job)
        f.close()
        x=os.system('scp /root/Music/{core-site.xml,mapred-site.xml,hdfs-site.xml} root@%s:/etc/hadoop/'%dat)
	#x=os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no  root@%s  'scp /home/dheeraj/Desktop/ip/hadoop-project-master/hadoopdheeraj/{core-site.xml,mapred-site.xml,hdfs-site.xml}  root@%s:/etc/hadoop/   > /dev/null 2>/dev/null' "%dat)
        if x==0:

#START DATANODE
                os.system('ssh %s hadoop-daemon.sh start datanode'%dat)
                #os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no root@%s 'hadoop-daemon.sh start datanode >/dev/null 2> /dev/null'"%dat)
#START TASKTRACKER
                os.system('ssh %s hadoop-daemon.sh start tasktracker'%dat)
                #os.system("sshpass -p 'redhat' ssh -o StrictKeyHostChecking=no root@%s 'hadoop-daemon.sh start tasktracker >/dev/null 2> /dev/null'"%dat)      
                print "datanode and task tracker created on ip  %s"%dat
        else:
                print "error creating files on datanode"

