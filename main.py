__author__ = 'Arian'
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import  pandas as pd
from bkt import *
from sklearn.neighbors import KNeighborsClassifier
from KNSS import *

fig = plt.figure()
img = scipy.io.loadmat('D:\MSC\BD\hws\img\patches.mat')
#cv2.imshow('Image', img)
#print(img.keys())
mg = np.array((img['patches']))
PDS_mg = pd.DataFrame(mg,columns = ['p'+str(i) for i in range(mg.shape[1])])
"""-------------------------------------------------------  change size of data -------------------------"""
ten_percent_PDS = PDS_mg.iloc[:,0:594]
#print(mg[:,0].reshape(20,20))
#plt.figure(1)
#for i in range (1,61):
#    plt.subplot(3,20,i)
#    imgplot = plt.imshow(mg[:,i].reshape(20,20))
#
#
#plt.show()
#print [p for p in PDS_mg]
#print list(PDS_mg.columns)
#print bckt_line(np.array([1,2]).T,np.array([0,1]).T,3)
df_hsh = bcktiz(ten_percent_PDS,10)
#print df_hsh
#print df_hsh.duplicated({False})
#print df_hsh.loc[:,(df_hsh.transpose()).duplicated({False})]
""" -------------------------------------Q3 p4------------------------------------- """
kk =10
#

#print dups
#print dups['p1171']
#print dups['p2046']
#dd = {'p3':1 ,'p5':2 ,'p9':3, 'p10':4 ,'p2046':5,'p1171':6}


#
#dd={}
dups = duplicate_columns(df_hsh,5,4,kk)
#plt.figure(1)
#p_1171 =dups['p1171']
#p_2046 =dups['p2046']
#for i in range(kk):
#    #dd[p_1171[i]]= i
#    plt.subplot(2,kk,i+1)
#    imgplot = plt.imshow(ten_percent_PDS[p_1171[i]].values.reshape(20,20))
#    plt.subplot(2,kk,(i+1)+kk)
#    imgplot = plt.imshow(ten_percent_PDS[p_2046[i]].values.reshape(20,20))
#plt.suptitle("KNN_LSh")
#
#
#plt.figure(2)
#dict_1171 = KNN_Single_Point(kk ,ten_percent_PDS,'p1171' )
#dict_2046 = KNN_Single_Point(kk ,ten_percent_PDS,'p2046' )
##print lst_1171
#for i in range(kk):
#    #dd[p_1171[i]]= i
#    plt.subplot(2,kk,i+1)
#    imgplot = plt.imshow(ten_percent_PDS[dict_1171['p1171'][i][0]].values.reshape(20,20))
#    plt.subplot(2,kk,(i+1)+kk)
#    imgplot = plt.imshow(ten_percent_PDS[dict_2046['p2046'][i][0]].values.reshape(20,20))
#plt.suptitle("KNN")

#plt.figure(3)
#plt.subplot(1,2,1)
#imgplot = plt.imshow(ten_percent_PDS['p1171'].values.reshape(20,20))
#plt.title('p1171')
#plt.subplot(2,2,2)
#imgplot = plt.imshow(ten_percent_PDS['p2046'].values.reshape(20,20))
#plt.title('p2046')

""" -----------------------------------------  Q3 p3-----------------"""
plt.figure(4)
dict_3_3 = KNN_SS(kk , ten_percent_PDS)
acc_3_3 = {}
print dict_3_3
print dups
#for p in dups.keys():
#    acc_3_3[p] = []
for p in dups.keys():
   acc_3_3[p]=(len(list(set(dict_3_3[p])-set(dups[p]))) )

print acc_3_3

plt.scatter([int(x[0][1:]) for x in acc_3_3.items()],[1.0*x[1]/kk for x in acc_3_3.items()])
plt.xlabel("point id")
plt.ylabel("diff")






plt.show()


