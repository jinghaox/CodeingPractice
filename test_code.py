import os
import time

time.sleep(1.0)

# change back to py2 format
print os.getcwd()

def test_branch2():
    if os.path.exists(r'c:\'):
        print 'Folder exists'
