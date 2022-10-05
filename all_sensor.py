import time
import Adafruit_ADS1x15
import glob
import firebase_admin
import time
import datetime
from firebase_admin import credentials
from firebase_admin import firestore

cred=credentials.Certificate("./mykey.json")
firebase_admin.initialize_app(cred)
db=firestore.client()
state=True


base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir+'28*')[0]
device_file =device_folder + '/w1_slave'
adc = Adafruit_ADS1x15.ADS1115()
Gain = 1

def read_temp_raw():
    f=open(device_file,'r')
    lines=f.readlines()
    f.close()
    return lines
def read_temp():
    lines=read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines=read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string=lines[1][equals_pos+2:]
        temp_c=float(temp_string)/1000.0
        return temp_c

while True:
	sensorValue=adc.read_adc(0, gain=Gain, data_rate=128)
	voltage = sensorValue*(0.125/1000)
	print(voltage,end="")
	phsensorValue=adc.read_adc(1, gain=1, data_rate=128)
	phvoltage=phsensorValue*(0.125/1000)
	phvalue=3.5*phvoltage+0.33

	#print("/", end="")
	#print(sensorValue)
	#print(read_temp())


	now=datetime.datetime.now()
	nowday=now.strftime('%Y-%m-%d')
	nowtime=now.strftime('%H:%M:%S')
	if state:
		db.collection(u'Ph').document(nowday).set(0)
		db.collection(u'Temp').document(nowday).set(0)
		db.collection(u'Turb').document(nowday).set(0)
		state=False
	doc_ref_Ph=db.collection(u'Ph').document(nowday)
	doc_ref_Temp=db.collection(u'Temp').document(nowday)
	doc_ref_Turb=db.collection(u'Turb').document(nowday)
	doc_ref_Ph.update({nowtime:phvalue})
	doc_ref_Temp.update({nowtime:read_temp()})
	doc_ref_Turb.update({nowtime:voltage})
	time.sleep(5)
