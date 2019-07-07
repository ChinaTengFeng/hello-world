import paramiko


class SSHConnection(object):
    def __init__(self, host, port, username, password):

        self._host = host
        self._port = port
        self._username = username
        self._password = password
        self._transport = None
        self._sftp = None
        self._client = None
        self._connect()  # 建立连接


    def _connect(self):
        transport = paramiko.Transport((self._host, self._port))
        transport.connect(username=self._username, password=self._password)
        self._transport = transport


    # 下载
    def download(self, remotepath, localpath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)

        self._sftp.get(remotepath, localpath)


    # 上传
    def put(self, localpath, remotepath):
        if self._sftp is None:
            self._sftp = paramiko.SFTPClient.from_transport(self._transport)

        self._sftp.put(localpath, remotepath)


    # 执行命令
    def exec_command(self, command):
        if self._client is None:
            self._client = paramiko.SSHClient()

        self._client._transport = self._transport
        stdin, stdout, stderr = self._client.exec_command(command)
        data = stdout.read()
        if len(data) > 0:
            #返回结果为bytes类型
            # print(data.decode('utf-8')) # 打印正确结果
            dic= {'status':'True','body':data}
            return dic

        err = stderr.read()
        if len(err) > 0:
            # print(err.decode('utf-8'))  # 输出错误结果
            dic = {'status': 'Flase', 'body': err}
            return dic

    def close(self):
        if self._transport:
            self._transport.close()

        if self._client:
            self._client.close()


if __name__ == "__main__":
    import time,pandas as pd
    start_time= time.time()
    conn = SSHConnection('10.0.0.11', 22, 'root', '1')
    # conn.exec_command('ls -ll')
    # conn.exec_command('cd /home/test;pwd')  # cd需要特别处理
    # conn.exec_command('pwd')
    # conn.exec_command('tree /home/test')

    #获取 第一列数据
    dic= conn.exec_command("df |awk '{ print $1 }' ")   #可以通过AWK精准拿到需要的数据

    #获取第五行数据，因为有标题的缘故，取值6，
    print(dic['body'].decode('utf-8').split('\n')[6])



    #对返回数据的处理方式：
    # dic = conn.exec_command('ls')
    # with open('a.txt','w') as f:
    #     for i in dic['body'].decode('utf-8'):
    #         f.write(i)
    # df = pd.read_csv(r'E:\Django\flask_lian_xi\Py_ssh\a.txt')
    # print(df)


    conn.close()

