Fastcopy:
=========

A shell script to copy files over a local network using tar, netcat and pipes

Why?
----

A small script to speed up large file transfers over a local network without NFS or Samba.

Based on:
---------

 * http://arkanis.de/weblog/2009-05-22-fast-file-transfer-with-netcat
 * http://www.screenage.de/blog/2007/12/30/using-netcat-and-tar-for-network-file-transfer/
 * http://serverfault.com/questions/18125/how-to-copy-a-large-number-of-files-quickly-between-two-servers

Usage:
------

 # place 'receiver.sh' in the destination folder
 # place 'sender.sh' in the source folder
 # start receiver: './receiver.sh -p port'
 # start sender: './sender.sh -s folder/ -d target_ip -p port'
 # wait....
 
Screenshot:
-----------
 

