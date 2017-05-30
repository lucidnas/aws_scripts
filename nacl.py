import boto3
import sys

elb = boto3.client('elb')
ec2 = boto3.client('ec2')


def main():

    while True:
        target_ip = raw_input('Enter Target IP: ')
        if target_ip not in get_network_interfaces_info().keys():
            print "The IP you entered is nowhere to be found. Could be in a different region, please try again."
        else:
            print '--------------------------------------'
            print "Nacl to block Source IP: {0}".format(nacl_of(target_ip))
            print '--------------------------------------'
        sys.exit(0)

def nacl_of(target_ip):
    subnet = get_network_interfaces_info()[target_ip]
    for nacls,subnets in get_network_acls().items():
        for item in subnets:
            if subnet == item:
                return nacls

def get_network_interfaces_info():
    net_interfaces = ec2.describe_network_interfaces()['NetworkInterfaces']
    return {item['PrivateIpAddress']:item['SubnetId'] for item in net_interfaces}

def get_network_acls():
    nacl = ec2.describe_network_acls(Filters=[{'Name':'association.subnet-id', 'Values':['*']}])['NetworkAcls']
    return  {item['NetworkAclId']:[subnet['SubnetId'] for subnet in item['Associations']] for item in nacl}


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "Shutdown requested...exiting"
        sys.exit(130)
