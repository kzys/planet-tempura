# -*- coding: utf-8 -*-

from xml.etree import ElementTree
import sys, re, hashlib

def dump(content):
  md5 = hashlib.md5()
  md5.update(content)
  file = open(md5.hexdigest(), 'w')
  file.write(content)
  file.close()

def find_body_nodes(root):
  return root.findall('./{http://www.w3.org/2005/Atom}content') + root.findall('./{http://www.w3.org/2005/Atom}summary')

def has_japanese(content):
  root = ElementTree.fromstring(content)
  nodes = find_body_nodes(root)
  if len(nodes) > 0:
    text = ' '.join(nodes[0].itertext())
    return re.search(ur'[ぁ-ゞ]', text)
  else:
    return False

def main():
  options = dict(zip(sys.argv[1::2], sys.argv[2::2]))
  content = sys.stdin.read()

  if has_japanese(content):
    sys.exit(1)
  else:
    print content

if __name__ == '__main__':
  main()
