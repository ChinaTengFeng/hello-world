import time
l = [i for i in range(10)]
ll = [i for i in range(10,30)]
lll = [i for i in range(30,40)]
print(l)
print(ll)
print(lll)
print('---------------------')

class A():
    """
    迁入必须迁出，不然出错（出错原因是因为，无法判断原有元素，和新迁移元素）

    如果需要迁移 list 数量为奇数，那么第二次实例化时，传入参数第一个必须是未迁移过的。

    """

    def __init__(self,l1,l2):
        self.l1 = l1
        self.l2 = l2
        self.num = len(l1)
    #迁入
    def a(self):
        for i in range(len(self.l2)):
            a = self.l2.pop(0)
            self.l1.append(a)


    #迁出
    def b(self):
        for i in range(self.num):
            a = self.l1.pop(0)
            self.l2.append(a)


ss = time.time()


for i in range(5):
    aa = A(l,ll)
    bb = A(lll,ll)
    aa.a()
    aa.b()
    # 需要迁移 list 数量为奇数时
    bb.a()
    bb.b()
    print(i)




dd = time.time()

print(l)
print(ll)
print(lll)
print(dd-ss)




# l = [1,2,3,4,5,6,7,8,9]
# for i in range(3+1,10):
#     # print(i)
#     print(l.pop(0))
