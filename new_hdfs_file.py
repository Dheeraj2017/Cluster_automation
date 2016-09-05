#/usr/bin/python2  -tt

import os

#for datanode
def new_hdfs_file(q):
        #os.system("sshpass -p redhat ssh -o StrictHostKeyChecking=no %s  mkdir /datanode"%k)
        dobj = open('/root/Desktop/typical/datanode/hdfs-site.xml','w')
        dobj.writelines('''<?xml version="1.0"?>
<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

<!-- Put site-specific property overrides in this file. -->

<configuration>
<property>
<name>dfs.data.dir</name>
<value>/datanode</value>
</property>
</configuration>
''')
        dobj.close()
        #os.system("scp /root/Desktop/typical/datanode/hdfs-site.xml  root@%s:/etc/hadoop/"%k)

