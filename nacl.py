import boto3
import sys


elb = boto3.client('elb')
ec2 = boto3.client('ec2')


def main():
    
