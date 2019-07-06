# import time
# from threading import Lock,Thread
# class A(object):
#     lock = Lock()
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#
#         if not cls._instance:
#             obj = object.__new__(cls)
#             cls._instance = obj
#         return cls._instance
#     def __init__(self,ddd):
#         self.ddd = ddd
#         self.lock = Lock()
#
#     def aaa(self,a):
#         # a = True
#         num = 1
#         self.lock.acquire()
#         while True:
#             if num<=10:
#                 print(a  + ' 在用呢 '+ str(num))
#                 num +=1
#             else:
#                 self.lock.release()
#                 break


import time
from threading import Lock,Thread
class A(object):
    lock = Lock()
    _instance = None

    def __new__(cls, *args, **kwargs):

        if not cls._instance:
            obj = object.__new__(cls)
            cls._instance = obj
        return cls._instance
    def __init__(self,ddd):
        self.ddd = ddd
        self.lock = Lock()

    def aaa(self,a):
        # a = True
        num = 1
        self.lock.acquire()
        for i in range(3):
            print(a  + ' 在用呢 '+ str(num))
            num+=1
            time.sleep(1)
        self.lock.release()

info = A('123')
into = A("456")
obj1 = Thread(target=info.aaa,args=('yyy',))
obj2 = Thread(target=into.aaa,args=('xxx',))
obj1.start()
obj2.start()


