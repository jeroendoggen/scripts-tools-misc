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

 1. place 'receiver.sh' in the destination folder
 2. place 'sender.sh' in the source folder
 3. start receiver: './receiver.sh -p port'
 4. start sender: './sender.sh -s source_folder/ -d destination_ip -p port'
 5. wait....
 
Screenshot:
-----------
Speed test between an old AMD64 and an Intel i3 pc over gigabit Ethernet using a 1GB ramdisk for the source and the destination.

 * rsync speed: ~24M bytes/sec
 * fastcopy speed: ~87M bytes/sec

![Screenshot](screenshot/fastCopyScreenshot.png?raw=true)

