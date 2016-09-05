#!/usr/bin/python2 -tt
import os,sys
import login
#main function
def main():
	os.system("dialog --backtitle 'BIG DATA HADOOP' -title 'WELCOME' --infobox 'AUTOMATIC CLUSTER FORMATION' 15 25 ")
        time.sleep(2.0)
	login.login()

if __name__=="__main__":main()
