#!/bin/bash
timestamp=`date +"%Y%m%d%H%M%S"`
image_version=$timestamp
#packer build -var "image_version=$image_version" aliyun.json
packer build -var image_version=$timestamp aliyun.json

