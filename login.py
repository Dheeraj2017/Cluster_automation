#!/usr/bin/python2  -tt
import os,sys,socket
import time
import commands
import getpass
import thread
import operator
import fcntl,struct
import namenode
import jobtracker
import datanode
import client
import yum_install
import hdfs_file
import core_file
import mapred_file
import new_core_file
import new_mapred_file
import start_service
import new_start_service
import copy
import get_ip_address

def login():
        user=os.system("dialog --backtitle 'BIG DATA HADOOP' --title 'USERNAME' --inputbox 'Enter username ' 7 30   2> user.txt")
        passw=os.system("dialog --backtitle 'BIG DATA HADOOP' --title 'PASSWORD' --inputbox 'Enter Password' 7 30   2> pass.txt")
        obj_user=open("user.txt",'r')
        user=obj_user.read()
        obj_user.close()
        obj_pass=open("pass.txt",'r')
        passw=obj_pass.read()
        obj_pass.close()
        if user=="root":
                if passw=="redhat":
                        while True:
                                os.system("dialog --backtitle 'BIG DATA HADOOP'  --title 'MENU' --menu 'Please choose one option' 12 46 2 1  'Automatic Cluster' 2 'Exit' 3 'CUSTOM INSTALLATION' 2> choice.txt ")
                                obj_choice=open("choice.txt")
                                choice=obj_choice.read()
                                obj_choice.close()
                                if choice=="1":
                                        os.system("ifconfig | cut -f1 -d' '")
                                        var=raw_input("Enter the interface name: ")
                                        #ip=get_ip_address(var)
					ip=get_ip_address.get_ip_address(var)
                                        print 'Your current IP address is : %s'%ip
                                        ip_input=raw_input('enter the ip range want to scan in network: ')
                                        net_mask=raw_input('enter the netmask want to scan:')
                                        ip_in=ip_input+'/'+net_mask
                                        new_var='nmap -sP '+ip_in+ '  | grep '+ip_input[0:3]+'  | cut -d: -f 2 | cut -c 22-36'
                                        ip_output=commands.getoutput(new_var)
                                        #**********************
                                        print type(ip_output)
                                        #**********************
                                        list_of_ip=ip_output.split('\n')
                                        ram=dict()
                                        a=ip_input[0:9]+'.254'
                                        for steps in list_of_ip:
                                                if steps==ip or steps==a:
                                                        continue
						command=commands.getoutput("sshpass -p redhat ssh -o StrictHostKeyChecking=no  root@%s  free -m | grep Mem |awk '{print $2}'"%steps)
                                                ram[steps]=command
                                        sort=sorted(ram.items(),key=operator.itemgetter(1))
                                        sorted_ip=sort[0][0]
                                        rec_ip=sorted_ip
                                        #*****************      
                                        print rec_ip
                                        #****************


                                        yum_install.yum_install(rec_ip)
                                        hdfs_file.hdfs_file(rec_ip)
                                        core_file.core_file(rec_ip)
                                        mapred_file.mapred_file(rec_ip)
                                        start_service.start_service(rec_ip)
                                        new_hdfs_file.new_hdfs_file(rec_ip)
                                        new_core_file.new_core_file(rec_ip)
                                        new_mapred_file.new_mapred_file(rec_ip)
                                        new_start_service.new_start_service(rec_ip)



                                        i=0
                                        for val in sort:
                                                i=i+1

                                        j=1
					for newval in sort:
                                                if j<i:
                                                        rec_ip=sort[j][0]
                                                        thread.start_new_thread(copy.copy,(rec_ip))
                                                        #thread.start_new_thread(copy,(rec_ip))
                                                        thread.start_new_thread(start_service.start_service,(rec_ip))
                                                        #thread.start_new_thread(start_service,(rec_ip))
                                                        j=j+1
                                elif choice=="2":
                                        var1=os.system("dialog --backtitle 'BIG DATA HADOOP' --title 'CHOICE' --yesno 'Are you sure Y/N' 5 40")
                                        if var1==0:
                                                print 'Thank you'
                                                time.sleep(3.0)
                                                exit()
                                        else :
                                                continue



                                elif choice=="3":
                                        os.system("ifconfig | cut -f1 -d' '")
                                        var=raw_input("Enter the interface name: ")
					ip=get_ip_address.get_ip_address(var)
                                        #ip=get_ip_address(var)
                                        print 'Your current IP address is : %s'%ip
                                        ip_input=raw_input('enter the ip range want to scan in network: ')
                                        net_mask=raw_input('enter the netmask want to scan:')
                                        ip_in=ip_input+'/'+net_mask
                                        new_var='nmap -sP '+ip_in+ '  | grep '+ip_input[0:3]+'  | cut -d: -f 2 | cut -c 22-36'
                                        ip_output=commands.getoutput(new_var)
                                        print type(ip_output)
                                        list_of_ip=ip_output.split('\n')
                                        ram=dict()
                                        a=ip_input[0:9]+'.254'
                                        for steps in list_of_ip:
                                                if steps==ip or steps==a:
                                                        continue
                                                command=commands.getoutput("sshpass -p redhat ssh -o StrictHostKeyChecking=no  root@%s  free -m | grep Mem |awk '{print $2}'"%steps)
                                                ram[steps]=command
                                        sort=sorted(ram.items(),key=operator.itemgetter(1))
					#**************
                                        print sort
                                        #************* 
                                        ip_var=raw_input("select an IP:")
                                        os.system("dialog --backtitle 'BIG DATA HADOOP'  --title 'MENU' --menu 'Please choose one option' 12 46 2 1 'Create Namenode And Start The Service' 2 'Create Jobtracker And Start The service' 3 'Create Datanode And Tasktracker And Start The Service' 4 'Create Client' 5 'Run Jps' 6 'Exit'  2> other_choice.txt ")
                                        new_obj_choice=open("other_choice.txt")
                                        ch=new_obj_choice.read()
                                        new_obj_choice.close()

                                        """
                                        ch=raw_input('''select appropriate option make carefull choose sequential is preferred:
                                                1. create namenode and start the service 
                                                2. create job tracker and start the service
                                                3. create datanode and tasktracker and start the service
                                                4. create client
                                                5. Jps
                                                6. exit''')
                                        """

                                        if int(ch)==1:
                                                namenode.namenode(ip_var)
                                                #namenode(ip_var)
                                                print("namenode created")


                                        elif int(ch)==2:
                                                nam=raw_input("give IP of name node: ")
                                                #jobtracker(ip_var,nam)
                                                jobtracker.jobtracker(ip_var,nam)
                                                print("jobtracker  created")


                                        elif int(ch)==3:
                                                nam=raw_input("give IP of name node: ")
                                                job=raw_input("give IP of jobtracker node: ")
                                                #datanode(nam,job,ip_var)
                                                datanode.datanode(nam,job,ip_var)
                                                print("data node and task tracker created")
					elif int(ch)==4:
                                                nam=raw_input("enter IP of namenode")
                                                #client(ip_var,nam)
                                                client.client(ip_var,nam)
                                                print("client created")

                                        elif int(ch)==5:
                                                jp=commands.getouput("ssh %s  /usr/java/jdk1.7.0_51/bin/jps"%ip_var)
                                                print jp

                                        else :
                                                print 'wrong selection please try again'
                                                continue

                                elif choice=="":
                                        var1=os.system("dialog --backtitle 'BIG DATA HADOOP' --title 'CHOICE' --yesno 'Are you sure Y/N' 5 40")
                                        if var1==0:
                                                print 'Thank you'
                                                time.sleep(3.0)
                                                exit()
                                        else :
                                                continue
                        else:
                                print 'Wrong Choice'
                else:
                        os.system("dialog --msgbox 'Password is incorrect 6 25'")
                        login()
        else:
                os.system("dialog --msgbox 'Username is incorrect 6 25'")
                        login()
#******************************************************************
login()

