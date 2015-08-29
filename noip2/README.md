# noip2: Debian & systemd
Updating your public IP dynamically with ``www.noip.com`` on Debian 8+

## Register a free domain at www.noip.com
http://www.noip.com

## Install noip2 from source
http://www.noip.com/support/knowledgebase/installing-the-linux-dynamic-update-client-on-ubuntu/
 * cd /usr/local/src/
 * wget http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz
 * tar xf noip-duc-linux.tar.gz
 * cd noip-2.1.9-1/
 * make install (this asks your username + password

## Create a Systemd service
https://bbs.archlinux.org/viewtopic.php?id=146167

Create the file ``/etc/systemd/system/noip2.service``

```
[Unit]
Description=No-IP Dynamic DNS Update Client
After=network.target

[Service]
Type=forking
ExecStart=/usr/local/bin/noip2

[Install]
WantedBy=multi-user.target

```

Testing:
 * ``systemctl status noip2.service``
 * ``systemctl start noip2.service`` (start immediately)
 * ``systemctl enable noip2.service`` (start at boot time)
