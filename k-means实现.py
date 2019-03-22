import pandas as pd
import numpy as np
import random
from matplotlib import pyplot as plt


f = pd.read_csv('company.csv',encoding='ansi')

def hanshu(x,y,x1,x2,x3,y1,y2,y3):
    x1,y1 = x1,y1
    x2,y2 = x2,y2
    x3,y3 = x3,y3
    loc = zip(x,y)

    list1,list2,list3 = [],[],[]

    for x,y in loc:
        d1 = np.sqrt((x-x1)**2+(y-y1)**2)
        d2 = np.sqrt((x-x2)**2+(y-y2)**2)
        d3 = np.sqrt((x-x3)**2+(y-y3)**2)
        d = min(d1,d2,d3)
        if d == d1:
            list1.append([x,y])
        elif d == d2:
            list2.append([x, y])
        elif d == d3:
            list3.append([x, y])

    list1pd,list2pd,list3pd = pd.DataFrame(list1),pd.DataFrame(list2),pd.DataFrame(list3)

    nx1,ny1 = list1pd[0].mean(),list1pd[1].mean()
    nx2,ny2 = list2pd[0].mean(),list2pd[1].mean()
    nx3,ny3 = list3pd[0].mean(),list3pd[1].mean()
    if nx1 == x1 and nx2 == x2 and nx3 == x3 and ny1 == y1 and ny2 == y2:
        return list1, list2, list3
    else:
        print('111111111111111111111')
        x = f['平均消费周期（天）'].values
        y = f['平均每次消费金额'].values
        return hanshu(x, y, nx1, nx2, nx3, ny1, ny2, ny3)



if __name__ == '__main__':
    x = f['平均消费周期（天）'].values
    y = f['平均每次消费金额'].values
    print(x,y)
    #随机聚类中心
    x1, y1 = random.randint(x.min(), x.max()), random.randint(y.min(), y.max())
    x2, y2 = random.randint(x.min(), x.max()), random.randint(y.min(), y.max())
    x3, y3 = random.randint(x.min(), x.max()), random.randint(y.min(), y.max())

    a = hanshu(x,y,x1,x2,x3,y1,y2,y3)
    list1,list2,list3 = pd.DataFrame(a[0]),pd.DataFrame(a[1]),pd.DataFrame(a[2])

    #画图
    x1 = list1[0]
    y1 = list1[1]
    x2 = list2[0]
    y2 = list2[1]
    x3 = list3[0]
    y3 = list3[1]

    plt.figure()
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    plt.grid(b=True, axis='y')

    plt.scatter(x1, y1)
    plt.scatter(x2, y2)
    plt.scatter(x3, y3)

    plt.show()



