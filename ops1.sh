#!/bin/bash
username="TraMiya McNeese"
echo "Hello, $username!"
if [ -f /var/log/syslog ]; then
   echo "Syslog found!"
else
    echo "Syslog missing!"

fi 