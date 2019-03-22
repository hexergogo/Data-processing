import  pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from matplotlib import pyplot as plt


f = pd.read_csv('air_data.csv',encoding='ansi')
# print(f.shape)

#预处理：(1)丢弃票价为空的记录。(2)丢弃票价为0、平均折扣率不为0、总飞行千米数大于0的记录。
index1 = f[f['SUM_YR_1'].isnull()].index
index2 = f[(f['SUM_YR_1']==0) & (f['avg_discount']!=0) & (f['SEG_KM_SUM']>0)].index
index = [i for i in index1]+[i for i in index2]
f.drop(index,axis=0,inplace=True)

#月份计算
def times(A):
    f[A] = [i.year for i in pd.to_datetime(f[A])]
    f['months'] = [i.month for i in pd.to_datetime(f[A])]
    return (2014 - f[A]) * 12 + (4 - f['months'])

#会员入会时间距观测窗口结束的月数
f['L'] =times('FFP_DATE')
#
#客户最近一次乘坐公司飞机距观测窗口结束的月数
f[f['LAST_FLIGHT_DATE']=='2014/2/29  0:00:00'] = 2014/2/29
f['R'] = times('LAST_FLIGHT_DATE')

#观测窗口内的飞行次数
f['F'] = f['FLIGHT_COUNT']
#观测窗口总飞行千米数
f['M'] = f['SEG_KM_SUM']
#平均折扣率
f['C'] = f['avg_discount']

#小数定标标准化
def deci(data):
    data = data/10**(np.ceil(np.log10(data.abs().max())))
    return data
#标准化数据
f['L'] = deci(f['L'])
f['R'] = deci(f['R'])
f['F'] = deci(f['F'])
f['M'] = deci(f['M'])
f['C'] = deci(f['C'])

#k-means
nF = f[['L','R','F','M','C']]
kms = KMeans(n_clusters = 5)
a=kms.fit_predict(nF)

#画图
plt.figure(figsize=(15,15),dpi=150)
L_C_1 = nF[a==0].mean().values
L_C_2 = nF[a==1].mean().values
L_C_3 = nF[a==2].mean().values
L_C_4 = nF[a==3].mean().values
L_C_5 = nF[a==4].mean().values

dataLenth = 5
angles = np.linspace(0,2*np.pi,dataLenth,endpoint=False)
labels = ['L','R','F','M','C']

L_C_1 = np.concatenate((L_C_1,[L_C_1[0]]))
L_C_2 = np.concatenate((L_C_2,[L_C_2[0]]))
L_C_3 = np.concatenate((L_C_3,[L_C_3[0]]))
L_C_4 = np.concatenate((L_C_4,[L_C_4[0]]))
L_C_5 = np.concatenate((L_C_5,[L_C_5[0]]))
angles = np.concatenate((angles,[angles[0]]))

plt.polar(angles,L_C_1,marker='.',linestyle=':')
plt.polar(angles,L_C_2,marker='o',linestyle=':')
plt.polar(angles,L_C_3,marker='s',linestyle=':')
plt.polar(angles,L_C_4,marker='x',linestyle=':')
plt.polar(angles,L_C_5,marker='D',linestyle=':')

plt.show()



