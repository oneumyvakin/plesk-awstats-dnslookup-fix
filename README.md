plesk-awstats-dnslookup-fix
===========================

Python script which fix DNSLookup=1 to DNSLookup=2 in Awstats config files of Plesk for Windows

Please use it careful. 
Pathes to vhosts and awstats are hardcoded.
Backup entire C:\Program Files (x86)\Parallels\Plesk\Additional\AWStats\wwwroot\cgi-bin folder before using. 
Scripts creates backup of each config before changing to <old file name>.original file

== Using

c:\python plesk-awstats-dnslookup-fix.py
