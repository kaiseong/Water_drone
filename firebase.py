import firebase_admin
import time
import datetime
from firebase_admin import credentials
from firebase_admin import firestore


cred=credentials.Certificate("./mykey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
state=True

while True:
	now=datetime.datetime.now()
	nowday=now.strftime('%Y-%m-%d')
	nowtime=now.strftime('%H:%M:%S')
	if state:
		db.collection(u'Ph').document(nowday).set(0)
		db.collection(u'Temp').document(nowday).set(0)
		state=False
	doc_ref_Ph=db.collection(u'Ph').document(nowday)
	doc_ref_Temp=db.collection(u'Temp').document(nowday)

	doc_ref_Ph.update({nowtime:10})
	doc_ref_Temp.update({nowtime:36.5})
	time.sleep(5)
