



import time
from multiprocessing import Lock,Process



class A(object):
    """
    把nc中原有vm全部迁出，可以在迁出是接收新的vm
    """
    lock = Lock()

    def __init__(self,bbb):
        self.bbb=bbb
        self.lock = Lock()


    def qianru(self,msg):

        self.lock.acquire()
        print('------开始迁入-----------')
        print(msg +' ru ' +  self.bbb)
        time.sleep(2)

        self.lock.release()
        print('----迁入结束------')


    def qianchu(self,msg):


        self.lock.acquire()
        print('-------开始迁出------')
        print(msg +' chu ' + self.bbb )
        time.sleep(2)
        self.lock.release()
        print('----------迁出结束-------')

    def migrate_enter(self,l1,l2):
        pass

    def migrate_out(self,l1,l2):
        pass



if __name__ =='__main__':
    starttime = time.time()
    info = A('yyy')
    into = A("xxx")

    #模拟三个 NC 迁入、迁出
    obj = Process(target=info.qianru,args=('info__1',))
    obj12 = Process(target=info.qianru,args=('info__2',))
    obj13 = Process(target=info.qianru,args=('info__3',))
    obj2 = Process(target=into.qianchu,args=('intto__1',))
    obj222 = Process(target=into.qianchu,args=('intto__2',))
    obj223 = Process(target=into.qianchu,args=('intto__3',))

    obj.start()  #迁入
    obj2.start()  # 迁出

    obj12.start()
    obj222.start()
    #
    obj13.start()
    obj223.start()


    #计算运行时间
    obj.join()
    obj12.join()
    obj13.join()
    obj2.join()
    obj222.join()
    obj223.join()
    endtime = time.time()
    print(endtime - starttime)

#搞定
