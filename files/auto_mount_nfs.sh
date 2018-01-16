#!/bin/bash
mkdir -p /data
Ab=192.168.11.0/24
Aa=192.168.10.0/24

Ab_mount=2585249f95-hxe21.cn-shenzhen.nas.aliyuncs.com
Aa_mount=2585249f95-whi41.cn-shenzhen.nas.aliyuncs.com

ip_net=`ip route|grep -v '^default'|grep 'eth0' |awk '{print $1}'`

if [ $Ab == $ip_net ]; then
    mount -t nfs -o vers=4.0 $Ab_mount:/ /data/
else
    mount -t nfs -o vers=4.0 $Aa_mount:/ /data/
fi

logger "Logs dir is success mounted!"
