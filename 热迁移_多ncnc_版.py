# status = {'stdin':None,'stdout':None}
# nc = {'2601-1': {'stdin':None,'stdout':None}, '3652-12': {'stdin':None,'stdout':None}, '5543-12': {'stdin':None,'stdout':None}}
# vm_name = {'VM1': '2601-1', 'VM2': '3652-12', 'VM3': '5543-12'}

#nc与vm的对应关系   nc_id:[ nc_id中的所有VM]
vm = {'210-10':['Q','W','R','T'],'251-0':['ss'], '2256-10':['a','b','c','d','g','h','p'],'222':['ddd','cc','fff']}
#所有nc
nc = ['210-10','251-0','2256-10','222']

#传入nc列表，生成迁移对应关系的字典
def huo_qu_dui_li(args):
    num = len(args)
    if num<2:
        raise ValueError('必须参入两个nc_id')
    li = {}
    if num <=2:
        li[args[0]] = args[1]
    else:
        for i in range(num):
            n = i+1
            if n<num:
                li[args[i]] = args[n]
            else:
                li[args[i]] = args[0]
    return li

li= huo_qu_dui_li(nc)

# 迁移
def jiao_huan2(dic):

    k = {}   #生成 nc 对应 VM数量的字典
    for i in dic:
        nc = len(vm[i])
        k[i] = nc
    # print(k)
    # li =  {'210-10': '251-0', '251-0': '2256-10', '2256-10': '210-10'}
    # k =   {'210-10': 4, '251-0': 3, '2256-10': 7}
    #开始交换
    for j in dic.keys():
        for i in range(k[j]):
            msg = vm[j].pop(0)
            vm[dic[j]].append(msg)

    return vm

print(vm)
jiao_huan2(li)
print(vm)
jiao_huan2(li)
print(vm)
jiao_huan2(li)
print(vm)
jiao_huan2(li)
print(vm)

F:\练习\答题练习\热迁移多nc多vm版.py
