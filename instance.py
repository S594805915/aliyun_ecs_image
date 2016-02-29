import json

from aliyunsdkecs.request.v20140526 import CreateInstanceRequest
from aliyunsdkecs.request.v20140526 import DeleteInstanceRequest
from aliyunsdkecs.request.v20140526 import DescribeDisksRequest
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StartInstanceRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest


class InstanceOp:

	def __init__(self):
		super

	@staticmethod
	def create_instance(self, client):
		instance_create = CreateInstanceRequest.CreateInstanceRequest(protocol='https')
		instance_create.set_Description('create xiaoer ecs tmpl')
		instance_create.set_InstanceName('ecs_template_creating')
		instance_create.set_InstanceType('ecs.t1.small')
		instance_create.set_InternetChargeType('InternetChargeType')
		instance_create.set_InternetMaxBandwidthOut('5')
		instance_create.set_Password('Aa123456.')
		instance_create.set_SystemDiskSize(50)
		instance_create.set_accept_format('json')
		try:
			result = json.loads(client.do_action(instance_create))
		except Exception:
			print Exception.message
		return result["InstanceId"]

	@staticmethod
	def start_instance(self, client, instance_id):
		instance_start = StartInstanceRequest.StartInstanceRequest()
		instance_start.set_InstanceId(instance_id)
		try:
			client.do_action(instance_start)
		except Exception:
			print Exception.message

	@staticmethod
	def stop_instance(self, client, instance_id):
		instance_stop = StopInstanceRequest.StopInstanceRequest()
		instance_stop.set_InstanceId(instance_id)
		try:
			client.do_action(instance_stop)
		except Exception:
			print Exception.message

	@staticmethod
	def delete_instance(self, client, instance_id):
		instance_delete = DeleteInstanceRequest.DeleteInstanceRequest()
		instance_delete.set_InstanceId(instance_id)
		try:
			client.do_action(instance_delete)
		except Exception:
			print Exception.message

	@staticmethod
	def get_instance_ip(self, client, instance_id):
		instance_desc = DescribeInstancesRequest.DescribeInstancesRequest()
		instance_desc.set_InstanceIds([instance_id])
		instance_desc.set_accept_format('json')
		try:
			instances = json.loads(client.do_action(instance_desc))
		except Exception:
			print Exception.message
		instance_ip = instances["Instances"]["Instance"][0]["PublicIpAddress"]["IpAddress"][0]
		return instance_ip

	@staticmethod
	def get_instance_disk_id(self, client, instance_id):
		instance_desc = DescribeDisksRequest.DescribeDisksRequest()
		instance_desc.set_InstanceId(instance_id)
		instance_desc.set_accept_format('json')
		try:
			instances = json.loads(client.do_action(instance_desc))
		except Exception:
			print Exception.message
		instance_ip = instances["Disks"]["Disk"][0]["DiskId"]
		return instance_ip

	@staticmethod
	def get_instance_status(self, client, instance_id):
		instance_status = DescribeInstancesRequest.DescribeInstancesRequest()
		instance_status.set_InstanceIds([instance_id])
		instance_status.set_accept_format('json')
		try:
			result = json.loads(client.do_action(instance_status))
		except Exception:
			print Exception.message
		status = result["Instances"]["Instance"][0]["Status"]
		return status