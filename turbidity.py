import time
 # Import the ADS1x15 module.
import Adafruit_ADS1x15
  
# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115()
 
# Or create an ADS1015 ADC (12-bit) instance.
#adc = Adafruit_ADS1x15.ADS1015()
 
# Note you can change the I2C address from its default (0x48), and/or the I2C
# bus by passing in these optional parameters:
#adc = Adafruit_ADS1x15.ADS1015(address=0x49, busnum=1)
 
# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1
 
print('Reading Turbidity values, press Ctrl-C to quit...')

# Main loop.
while True:
    tursensorValue=adc.read_adc(0, gain=1, data_rate=128)
    phsensorValue=adc.read_adc(1, gain=1, data_rate=128)
    turvoltage=tursensorValue*(0.125/1000)
    phvoltage=phsensorValue*(0.125/1000)
    phvalue=3.5*phvoltage+0.33
    print(f'ph:{phvalue}')
    print(f'sensor:{turvoltage}')
    time.sleep(0.1)
