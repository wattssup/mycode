#!/usr/bin/env python3

import shutil

import os

os.chdir('/home/student/mycode/')

shutil.move('raynor.obj', 'ceph_storage/') #Moves Raynor to ceph_storage

xname = input('What is the new name for kerrigan.obj? ')  #Gets new name for kerrigan.obj

shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)  #moves kerrigan to ceph_Storage, and renames it to the new name


