import subprocess

conn = subprocess.Popen('dirddddd',
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        shell=True)

res = conn.stdout.read()


# print(res.decode('utf-8'))   解码与执行平台有关，windowns bytes类型 是使用 gbk 编码的， linux 使用 utf-8编码的
# print(res.decode('gbk'))
#
# res2 = conn.stderr.read()
# print(type(res2))
# print(res2.decode('gbk'))


# 解说
# conn 为对象
# subprocess.Popen  如果不指定 输入管道，默认打印到屏幕
# stdout=subprocess.PIPE  指定执行正确命令后的输出管道       stderr=subprocess.PIPE  指定执行错误命令后的错误输出管道
# subprocess.PIPE  为管道的意思
# shell =True   指定使用shell命令解释器

# 结果在管道中，必须 read()读出来。
# PS： 每次结果只能读取一次，如果需要多次使用，可以使用变量接收。。。