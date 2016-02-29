import json

from aliyunsdkecs.request.v20140526 import DescribeSnapshotsRequest
from aliyunsdkecs.request.v20140526 import CreateSnapshotRequest
from aliyunsdkecs.request.v20140526 import DeleteSnapshotRequest


class SnapshotOp:
	def __init__(self):
		super

	@staticmethod
	def create_snapshot(self, client, disk_id):
		snapshot_create = CreateSnapshotRequest.CreateSnapshotRequest()
		snapshot_create.set_DiskId(disk_id)
		snapshot_create.set_accept_format('json')
		snapshot_create.set_Description('All in one ecs template')
		try:
			result = json.loads(client.do_action(snapshot_create))
		except Exception:
			print Exception.message
		snapshot_id = result["SnapshotId"]
		return snapshot_id

	@staticmethod
	def delete_snapshot(self, client, snapshot_id):
		snapshot_delete = DeleteSnapshotRequest.DeleteSnapshotRequest()
		snapshot_delete.set_SnapshotId(snapshot_id)
		snapshot_delete.set_accept_format('json')
		try:
			client.do_action(snapshot_delete)
		except Exception:
			print Exception.message

	@staticmethod
	def get_snapshot_status(self, client, disk_id):
		snapshot_status = DescribeSnapshotsRequest.DescribeSnapshotsRequest()
		snapshot_status.set_DiskId(disk_id)
		snapshot_status.set_accept_format('json')
		try:
			result = json.loads(client.do_action(snapshot_status))
		except Exception:
			print Exception.message
		status = result["Snapshots"]["Snapshot"][0]["Status"]
		progress = result["Snapshots"]["Snapshot"][0]["Progress"]
		return [status, progress]