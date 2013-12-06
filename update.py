#! /usr/bin/python
import os, subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))

subprocess.call([ 'python',
                  os.path.join('..', 'venus', 'planet.py'),
                  'planet.ini' ])
subprocess.call([ 'aws', 's3', 'sync',
                  '--region', 'us-east-1',
                  '--acl', 'public-read',
                  'public/', 's3://tempura.8-p.info/' ])
