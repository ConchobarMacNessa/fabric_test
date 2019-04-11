#!/usr/bin/env python
from fabric.api import local

def hello(name='world'):
  print("hello %s" % name)

def deploy():
  local('git status')
  local('git add -p && git commit')
  local('git push')
