from django import forms
from django.conf import settings

import time
import serial

ser = serial.Serial(
	port="/dev/ttyACM0",
	baudrate=9600,
	parity=serial.PARITY_ODD,
	stopbits=serial.STOPBITS_TWO,
	bytesize=serial.SEVENBITS
	)

class PayForm(forms.Form):
    network = forms.ChoiceField(choices=settings.NETWORK_CHOICES,
	    widget=forms.Select())
    pin = forms.IntegerField()

    def save(self):
	# request = 'AT+CUSD=1,"*555*%s#",15%s' % (self.cleaned_data['pin'], '\r\n')
	request = 'AT+CUSD=1,"*556#",15%s' % '\r\n'

	alive = True

	while alive:
	    for i in request:
		ser.write(i)
	    out = ""

	    time.sleep(2)
	    while ser.inWaiting() > 0:
		out += ser.read()

	    alive = False
	
	if out.find("OK"):
	    return out
