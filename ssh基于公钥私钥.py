import paramiko

#使用ssh公钥私钥登录
private_key = paramiko.RSAKey.from_private_key_file(r'E:\Django\flask_lian_xi\Py_ssh\id_rsa.txt')
# 实例化一个transport对象
transport = paramiko.Transport(('10.0.0.11', 22))
# 建立连接
transport.connect(username='root', pkey=private_key)
ssh = paramiko.SSHClient()
ssh._transport = transport

stdin, stdout, stderr = ssh.exec_command('df')
# 获取命令结果
res, err = stdout.read(), stderr.read()
result = res if res else err
print(result.decode())
# 关闭连接
ssh.close()

