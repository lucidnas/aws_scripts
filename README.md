# aws_scripts
A bunch of AWS scripts to perform basic tasks
--------------------------------------------------------------------------------------

nacl.py:
--------
This script uses AWS Boto 3 SDK to return the appropriate Network Acl
required to block the source IP attacking an instance as reported by Alertlogic. 

The program accepts the IP of an instance as a cmd line argument or prompts the 
user to enter an instance IP if no argument is provided by the user. 

Usage: 
```
$ python nacl.py 10.246.1.56
Nacl to block Source IP: acl-7eebc71a

$ python nacl.py
Enter Instance IP: 10.246.1.56
Nacl to block Source IP: acl-7eebc71a
```

Create an alias to call the script from anywhere in the terminal:
```
alias nacl='python ~/where/you/saved/the/script/nacl.py'
```
```
$ nacl 10.246.1.56
Nacl to block Source IP: acl-7eebc71a
```
elb.py:
-------
This script utilizes AWS Boto 3 SDK to return the state of the instances behind an ELB.

The program accepts the the name of an ELB as a cmdline argument or prompts the user to enter
the name of the ELB.

Usage:

```
$ python elb.py hub-puppet-elb-elb
State of instances behind hub-puppet-elb-elb
InstanceID          InstanceName InstanceState  PrivateIP     SystemStatus InstanceStatus
i-00d1ffdfaac6f5f80 puppet       InService      10.246.3.232  ok           ok

$ python elb.py
Enter ELB: hub-puppet-elb-elb
State of instances behind hub-puppet-elb-elb
InstanceID          InstanceName InstanceState  PrivateIP     SystemStatus InstanceStatus
i-00d1ffdfaac6f5f80 puppet       InService      10.246.3.232  ok           ok
```

If no name is provided, the program returns the list of ELBs in that region. This is especially helpful if you entered the wrong ELB name.
```
$ python elb.py
Enter ELB: 
Could not locate ELB entered. Printing all available ELbs in region

LoadBalancers:
hub-puppet-elb-elb
hub-exttoint-elb-internal-elb
```
Create an alias to call the script from anywhere in the terminal
```
alias pelb='python ~/scripts/NOC-Scripts/elb.py'
```
