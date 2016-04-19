import paramiko


class TplInstanceInitual:
    def __init__(self):
        pass

    def upload_files (self, host, port, username, password, local_path, server_path):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)
        ssh_ftp = ssh.open_sftp()
        ssh_ftp.put(local_path, server_path, confirm=True)
        ssh.close()

    def exec_files (self, host, port, username, password, server_path):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=port, username=username, password=password)
        _, ssh_stdout1, ssh_stderr1 = ssh.exec_command('chmod u+x %s' % server_path)
        _, ssh_stdout2, ssh_stderr2 = ssh.exec_command(server_path)
        for line in ssh_stderr2.readlines():
            print line.strip()
        ssh.close()

