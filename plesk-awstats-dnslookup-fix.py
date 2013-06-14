# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import sys
import fileinput
import win32file

VHOSTS_PATH = 'C:\\inetpub\\vhosts\\'
EXCLUDE = ['.skel', 'default', 'fs', 'Servers', 'sitebuilder', 'sqladmin', 'webmail']
AWSTATS_PATH = 'C:\\Program Files (x86)\\Parallels\\Plesk\\Additional\\AWStats\\wwwroot\\cgi-bin\\awstats.%s.conf'

folders = os.listdir(VHOSTS_PATH)
if not folders:
    print('Unable to get folder list of %s' % VHOSTS_PATH)
    sys.exit(1)

for folder in folders:
    if folder in EXCLUDE:
        continue
    domain_awstats_config = VHOSTS_PATH + folder + '\\statistics\\webstat\\AWStats\\cgi-bin\\awstats.%s.conf' % folder
    domain_awstats_config_backup = domain_awstats_config + '.original'
    if os.path.exists(domain_awstats_config):
        win32file.CopyFile(domain_awstats_config, domain_awstats_config_backup, 0)
        for line in fileinput.input(domain_awstats_config, inplace = 1):
            print(line.replace("DNSLookup=1", "DNSLookup=2"), end="")
        fileinput.close()
    global_awstats_config = AWSTATS_PATH % folder
    global_awstats_config_backup = global_awstats_config + '.original'
    if os.path.exists(AWSTATS_PATH % folder):
        win32file.CopyFile(global_awstats_config, global_awstats_config_backup, 0)
        for line in fileinput.input(global_awstats_config, inplace = 1):
            print(line.replace("DNSLookup=1", "DNSLookup=2"), end="")
        fileinput.close()
