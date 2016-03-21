# coding:utf-8
import os
import time
import paramiko
from aliyunsdkcore import client
from image import ImageOp
from instance import InstanceOp
from snapshot import SnapshotOp


def init_client(access_id, access_key, region_id):
	c = client.AcsClient(access_id, access_key, region_id)
	return c


def remote_execute_script_ssh(host, port, username, password, local_path, server_path):
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, port=port, username=username, password=password)
	ssh_ftp = ssh.open_sftp()
	ssh_ftp.put(local_path, server_path, confirm=True)
	_, ssh_stdout1, ssh_stderr1 = ssh.exec_command('chmod u+x %s' % server_path)
	_, ssh_stdout2, ssh_stderr2 = ssh.exec_command(server_path)
	for line in ssh_stderr2.readlines():
		print line.strip()
	ssh.close()


if __name__ == '__main__':
	image_name = 'aliyun_shzhen_ecs_img_v01'
	access_id = os.environ.get('ACCESSID')
	access_key = os.environ.get('ACCESSKEY')
	region_id = os.environ.get('REGIONID')
	instance = InstanceOp()
	snapshot = SnapshotOp()
	image = ImageOp()

	# clt = init_client(access_id, access_key, region_id)
	clt = init_client('JP4blw1Ph7OOQ37D', 'J05XE0hAX8fiGQDIDNeaAd8PpDaAWg', 'cn-shenzhen')
	# instance_id = instance.create_instance(clt)
	# while instance.get_instance_status(client, instance_id) != 'Running':
	# 	print('instance is starting...')
	# 	time.sleep(5)
	# print "Instance {instance_id} is running".format(instance_id=instance_id)
	#
	# instance_ip = instance.get_instance_ip(clt, instance_id)
	#
	# remote_execute_script_ssh(instance_ip, 22, 'root', 'Aa123456', 'tmpl.sh', '/tmp/tmpl.sh')
	#
	# disk_id = instance.get_instance_disk_id(clt, instance_id)
	# snapshot_id = snapshot.create_snapshot(clt, disk_id)
	# snapshot_status = snapshot.get_snapshot_status(clt, disk_id)
	# while snapshot_status[0] == 'progressing':
	# 	print(snapshot_status[1])
	# 	time.sleep(5)
	# 	snapshot_status = snapshot.get_snapshot_status(clt, disk_id)
	#
	# if snapshot_status[0] == 'accomplished':
	# 	print "{snapshot_id} is created. its source disk is {disk_id}".format(snapshot_id=snapshot_id, disk_id=disk_id)
	# else:
	# 	print "create snapshot error"
	#
	# image_id = image.create_image(clt, image_name=image_name, snapshot_id=snapshot_id)
	# print "Image[image_id] is created finished"
	#
	# instance.stop_instance(clt, instance_id)
	# while instance.get_instance_status(client, instance_id) != 'Stopped':
	# 	print('instance is stopping...')
	# 	time.sleep(5)
	# print "Instance {instance_id} is stopped".format(instance_id=instance_id)
	#
	# instance.delete_instance(clt, instance_id)
	# print "Instance {instance_id} is Dropped".format(instance_id=instance_id)

	print image.list_image_id(clt)

