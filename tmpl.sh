#!/bin/bash
#install jdk
wget http://xiaoer-packages.oss-cn-shenzhen.aliyuncs.com/jdk-7u79-linux-x64.tar.gz
tar -xzvf jdk-7u79-linux-x64.tar.gz
rm jdk-7u79-linux-x64.tar.gz
mv jdk1.7.0_79 /usr/local/
echo 'export JAVA_HOME=/usr/local/jdk1.7.0_79' >> /etc/profile
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> /etc/profile
. /etc/profile

#install docker
apt-get install -y apt-transport-https ca-certificates
apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
echo 'deb https://apt.dockerproject.org/repo ubuntu-trusty main' >> /etc/apt/sources.list
apt-get update
apt-get -y install linux-image-extra-$(uname -r)
apt-get install -y docker-engine
service docker stop

#install common packages
apt-get install -y python-pip telnet vim curl zip unzip git
