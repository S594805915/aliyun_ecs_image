# coding:utf-8
import os
from aliyunsdkcore import client
from libs.image import ImageOp
from libs.instance import InstanceOp
from libs.snapshot import SnapshotOp
from libs.template_instance_initial import TplInstanceInitual


def init_client(access_id, access_key, region_id):
    c = client.AcsClient(access_id, access_key, region_id)
    return c

if __name__ == '__main__':
    image_name = 'aliyun_shzhen_ecs_img_v01'
    access_id = os.environ.get('ACCESSID')
    access_key = os.environ.get('ACCESSKEY')
    region_id = os.environ.get('REGIONID')
    instance = InstanceOp()
    snapshot = SnapshotOp()
    image = ImageOp()
    tplInstanceInitual = TplInstanceInitual()

    clt = init_client(access_id, access_key, region_id)

