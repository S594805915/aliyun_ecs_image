import json

from aliyunsdkecs.request.v20140526 import CreateImageRequest
from aliyunsdkecs.request.v20140526 import DeleteImageRequest
from aliyunsdkecs.request.v20140526 import DescribeImagesRequest


class ImageOp:
    def __init__(self):
        super

    def create_image(self, client, image_name, snapshot_id):
        image_create = CreateImageRequest.CreateImageRequest()
        image_create.set_SnapshotId(snapshot_id)
        image_create.set_ImageName(image_name)
        image_create.set_accept_format('json')
        try:
            result = json.loads(client.do_action(image_create))
        except Exception:
            print Exception.message
        return result['ImageId']


    def delete_image(self, client, image_id):
        image_delete = DeleteImageRequest.DeleteImageRequest()
        image_delete.set_ImageId(image_id)
        try:
            client.do_action(image_delete)
        except Exception:
            print Exception.message

    def list_image_id(self, client):
        image_desc = DescribeImagesRequest.DescribeImagesRequest()
        image_desc.set_Status('Status')
        image_desc.set_ImageOwnerAlias('system')
        image_desc.set_accept_format('json')
        # image_id = image_desc.get_ImageId()
        try:
            return client.do_action(image_desc)
        except Exception, e:
            print e.message
