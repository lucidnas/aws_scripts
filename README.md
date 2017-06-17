# aws_scripts
A bunch of AWS scripts to perform basic tasks
--------------------------------------------------------------------------------------

A quick tour of all the scripts and their proper usage.
-------------------------------------------------------

nacl.py:
--------
This script uses AWS Boto 3 API to return the appropriate Network Acl
required to block the source IP attacking an instance as reported by Alertlogic. 

The program accepts the IP of an instance as a cmd line argument or prompts the 
user to enter an instance IP if no argument is provided by the user. 

Usage: 
From LTS do either of the following:

[amohammed@lw-lts-155: ~/scripts/NOC-Scripts <lw-sandbox ap-southeast-1 59:09>]

$ python nacl.py 10.246.1.56

Nacl to block Source IP: acl-7eebc71a

[amohammed@lw-lts-155: ~/scripts/NOC-Scripts <lw-sandbox ap-southeast-1 55:32>]

$ python nacl.py
Enter Instance IP: 10.246.1.56

Nacl to block Source IP: acl-7eebc71a

Create an alias to call the script from anywhere in the terminal:

alias nacl='python ~/where/you/saved/the/script/nacl.py'

[amohammed@lw-lts-155: ~ <lw-sandbox ap-southeast-1 47:20>]

$ nacl 10.246.1.56

Nacl to block Source IP: acl-7eebc71a

elb.py:
-------
This script utilizes AWS Boto 3 API to return the state of the instances behind an ELB.

The program accepts the the name of an ELB as a cmdline argument or prompts the user to enter
the name of the ELB.

Usage:
From LTS do either of the the following:

[amohammed@lw-lts-155: ~/scripts/NOC-Scripts <lw-sandbox ap-southeast-1 36:20>]

$ python elb.py hub-puppet-elb-elb

State of instances behind hub-puppet-elb-elb

InstanceID i-00d1ffdfaac6f5f80

InstanceName puppet

InstanceState InService

PrivateIP 10.246.3.232

SystemStatus ok

InstanceStatus ok
   

[amohammed@lw-lts-155: ~/scripts/NOC-Scripts <lw-sandbox ap-southeast-1 31:38>]

$ python elb.py
Enter ELB: hub-puppet-elb-elb

State of instances behind hub-puppet-elb-elb

InstanceID i-00d1ffdfaac6f5f80

InstanceName puppet

InstanceState InService

PrivateIP 10.246.3.232

SystemStatus ok

InstanceStatus ok                                                           

If no name is provided, the program returns the list of ELBs in that region. This is especially helpful if you entered the wrong ELB name.

[amohammed@lw-lts-155: ~/scripts/NOC-Scripts <lw-sandbox ap-southeast-1 31:20>]
$ python elb.py
Enter ELB: 
Could not locate ELB entered. Printing all available ELbs in region

LoadBalancers:
hub-puppet-elb-elb
hub-exttoint-elb-internal-elb

Create an alias to call the script from anywhere in the terminal
alias pelb='python ~/scripts/NOC-Scripts/elb.py '

client_bastion.sh:
-----------------
This is a shell script that logs you into a client's bastion server using the bastion's full dns name.
e.g. ubuntu@bastion.sans.aws.logicworks.net. 

The program accepts the name of a particular client and logs you into the client's bastion using the ubuntu user.
It also adds and forwards your ssh keys to the bastion server.

Usage:
From LTS do the follwoing:

$ ./client_bastion sans
Logging into sans's bastion server..
Identity added: /home/lw-staff/amohammed/.ssh/id_rsa (/home/lw-staff/amohammed/.ssh/id_rsa)
Identity added: /home/lw-staff/amohammed/.ssh/id_dsa (/home/lw-staff/amohammed/.ssh/id_dsa)
Welcome to Ubuntu 14.04.4 LTS (GNU/Linux 3.13.0-48-generic x86_64)

Last login: Sat Jun 17 12:32:25 2017 from corpfw.noc.logicworks.net
ubuntu@mgmt-bastion-129:~$ 

Create an alias to call the script from anywhere.
alias bastion='~/scripts/NOC-Scripts/client_bastion' 
