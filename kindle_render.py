#!/usr/bin/env python
"""
Render Context Free cfdgs for use on Kindle Touch
=================================================

Usage
-----
 * (optional) update TARGET_DIR to point to your mounted Kindle
 * ./kindle_render.py design1.cfdg design2.cfdg

Setup Instructions
------------------
 * Jailbreak Kindle and set up networking
 * SSH into Kindle and run:
   - mntroot rw
   - mv -f /usr/share/blanket/screensaver /usr/share/blanket/screensaver.bak
   - ln -sfn /mnt/us/screensaver /usr/share/blanket/screensaver

Additional Resources
--------------------
Context Free:
http://www.contextfreeart.org/

Kindle Jailbreak:
http://wiki.mobileread.com/wiki/Kindle_Touch_Hacking#Jailbreak

Kindle Screensavers:
http://wiki.mobileread.com/wiki/Kindle_Touch_Hacking#Screen_Savers
"""
import os
import random
import subprocess
import sys

TARGET_DIR = '/media/Kindle/screensaver'

if not os.path.exists(TARGET_DIR):
    TARGET_DIR = 'screensaver'

if len(sys.argv) < 2:
    print "Please supply one or more filenames to render."
    exit()

subprocess.call(['mkdir', '-p', TARGET_DIR])
NEW_TEMPLATE = os.path.join(TARGET_DIR, 'bg_xsmall_ss%02d.png')

for x in range(1, 100):
    subprocess.call(['cfdg', '-s', '600x800',
                     random.choice(sys.argv[1:]),
                     NEW_TEMPLATE % x])
