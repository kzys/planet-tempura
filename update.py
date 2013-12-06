#! /usr/bin/python
import os, subprocess

os.chdir(os.path.dirname(os.path.abspath(__file__)))

subprocess.call([ 'python',
                  os.path.join('..', 'venus', 'planet.py'),
                  'planet.ini' ])
