import boto3
import sys
import json

# from json import JSONEncoder
# from uuid import UUID
# import datetime
# JSONEncoder_olddefault = JSONEncoder.default
# def JSONEncoder_newdefault(self, o):
#     if isinstance(o, UUID): return str(o)
#     if isinstance(o, datetime.datetime): return str(o)
#     return JSONEncoder_olddefault(self, o)
# JSONEncoder.default = JSONEncoder_newdefault

#json.dumps(dict,cls=DatetimeEncoder)
elb = boto3.client('elb')
ec2 = boto3.client('ec2')

email_template = ''

display_bar = ['InstanceID', 'InstanceName', 'InstanceState', 'PrivateIP', 'SystemStatus', 'InstanceStatus']
elb_name = ''
region = ['us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1',
 'eu-central-1', 'ap-northeast-1', 'ap-northeast-2',
 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'sa-east-1']


def main():
    if len(sys.argv) < 2:
        elb_name = raw_input('Enter ELB Name: ')
        all_elbs = get_all_elb_names()
        if elb_name in all_elbs:
            instances_info = get_instance_info(elb_name)
            #print instances_info
        # for i in instances_info:
        #     print i.k
            beautifier(elb_name, instances_info)
        else:
            print 'Could not locate ELB entered. Printing all available ELbs in region'
            print '' * 15
            print 'LoadBalancers:'
            print '-' * 15

            for i in get_all_elb_names():
                print i

    else:
        elb_name = sys.argv[1]
        all_elbs = get_all_elb_names()
        if elb_name in all_elbs:
            instances_info = get_instance_info(elb_name)
            beautifier(elb_name, instances_info)
        else:
            print 'Could not locate ELB entered. Printing all available ELBs in region'
            print ''
            print 'LoadBalancers:'
            print '-' * 50
            for i in get_all_elb_names():
                print i

def beautifier(elb_name, instances_info):
    print ''
    print "State of instances behind {0}".format(elb_name)
    print "-" * 120
    print '{:<20} {:<20} {:<20} {:<20} {:<20} {:<20}'.format(*display_bar)
    print "-" * 120
    for k in instances_info:
        for i in sum(k,[]):
            print  '{:<20}'.format(i).rjust(5),
        print ''


def email_template(elb_name, instance_info):
    print
    return

def get_elb_info(elb_name):
    return


def get_instance_info(elb_name):
    inst_names = get_all_instance_names()
    inst_state_info = elb.describe_instance_health(LoadBalancerName=elb_name)['InstanceStates']
    inst_private_ip = get_all_instances_private_ips()
    #print inst_state_info
    inst_state_id_ip= [[[i['InstanceId'],inst_names[i['InstanceId']],
                       i['State'],inst_private_ip[i['InstanceId']]],get_instance_states(i['InstanceId'])]
                       for i in inst_state_info]
    return inst_state_id_ip

def get_all_elb_names():
    lb_desc = elb.describe_load_balancers()['LoadBalancerDescriptions']
    return [i['LoadBalancerName'] for i in lb_desc]

def get_all_instance_names():
    instance_tags = ec2.describe_tags()['Tags']
    return {i['ResourceId']:i['Value'] for i in instance_tags if i['ResourceType'] == 'instance' and i['Key'] == 'Name'}


def get_all_instances_private_ips():
    instance_info = ec2.describe_instances()['Reservations']
    return {d['Instances'][0]['InstanceId']:d['Instances'][0]['PrivateIpAddress'] for d in instance_info}

def get_instance_states(instance):
    instance_states = ec2.describe_instance_status(InstanceIds=[instance])['InstanceStatuses']
    if instance_states == []:
        return ['Stopped', 'Stopped']
    else:
        return [instance_states[0]['SystemStatus']['Status'],instance_states[0]['InstanceStatus']['Status']]


# def get_az():
#     return elb.describe_load_balancers()['LoadBalancerDescriptions'][0]['AvailabilityZones'][0][:-1]
    #az = [i['LoadBalancerName'] for i in lb_desc]

def get_ec2_info():
    return
#response = elb.describe_load_balancers(LoadBalancerNames=[sys.argv[1]])


#z= response['LoadBalancerDescriptions'][0]['Instances']
#health = elb.describe_instance_health(LoadBalancerName=sys.argv[1])

#po = health[u'InstanceStates']



# headers = ['InstanceName', 'InstanceID', 'InstanceStatus', 'SystemStatus', 'InstanceState', 'PassingTraffic']
# row_format = "{:>15}" * (len(headers) + 1)
# print row_format.format("",*headers)

# for each instance, determine its attribute
# for i in xrange(0,len(z)):
#         a = z[i][u'InstanceId']
#
# 	# determine the instance private ip address
# 	desc_inst = ec2.describe_instances(InstanceIds=[z[i][u'InstanceId']])
# 	b= desc_inst[u'Reservations'][
#     0][u'Instances'][0][u'PrivateIpAddress']
#         status_paginator = ec2.get_paginator('describe_instance_status')
#         r2_iterator = status_paginator.paginate(InstanceIds=[z[i][u'InstanceId']])
#
#
# 	for p in po:
# 		if p[u'InstanceId'] == a:
# 			s = p[u'State']
#
#         for r in r2_iterator:
#         	c=  r[u'InstanceStatuses'][0][u'InstanceStatus'][u'Status']
# 	        d=  r[u'InstanceStatuses'][0][u'SystemStatus'][u'Status']
#         	e=  r[u'InstanceStatuses'][0][u'InstanceState'][u'Name']
#
#
#         print row_format.format('',*[a,b,c,d,e,s])
#
if __name__ == "__main__":
 # if you call this script from the command line (the shell) it will
 # run the 'main' function
 main()