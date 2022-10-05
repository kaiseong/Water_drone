import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import matplotlib.pyplot as plt
from pandas.core.indexes import interval
from matplotlib.animation import FuncAnimation

cred=credentials.Certificate('mykey.json')
firebase_admin.initialize_app(cred,{'projectId': 'boat-91ec6'})

db=firestore.client()

doc_ref_Ph=db.collection(u'Ph')
doc_ref_Temp=db.collection(u'Temp')
doc_ref_Turb=db.collection(u'Turb')
copy_time=[]
time=[]
val_ph=[]
val_temp=[]
val_turb=[]
cnt=0

def animate(i):
    docs_Ph=doc_ref_Ph.stream()
    docs_Temp=doc_ref_Temp.stream()
    docs_Turb=doc_ref_Turb.stream()
    
    # PH데이터 뽑아 오기
    for doc in docs_Ph:
        data=doc.to_dict()
        data=dict(sorted(data.items()))
        time=list(data.keys())
        val_ph=list(data.values())
        
        
    # 온도 데이터 뽑아 오기
    for doc in docs_Temp:
        data=doc.to_dict()
        data=dict(sorted(data.items()))
        val_temp=list(data.values())
    
    # 탁도 데이터 뽑아 오기
    for doc in docs_Turb:
        data=doc.to_dict()
        data=dict(sorted(data.items()))
        val_turb=list(data.values())
        
    if (len(time)==len(val_temp)):
        global copy_time
        copy_time=list(range(len(time)))
    print('time :', time, '\n temp : ',val_temp,'\n ph : ',val_ph)
    if (len(time)==len(val_ph) and len(time)==len(val_temp) and len(time)==len(val_turb)):
        plt.cla()
        plt.subplot(2,1,1)
        plt.ylabel("Temp")
        plt.plot(copy_time,val_temp,label='Temp')
        plt.subplot(2,1,2)
        plt.plot(copy_time,val_ph,label='PH')
        plt.plot(copy_time,val_turb,label="Turb")
        plt.legend(loc='upper left')
        plt.tight_layout()

ani=FuncAnimation(plt.gcf(),animate,interval=1000)
plt.tight_layout()
plt.show()    

