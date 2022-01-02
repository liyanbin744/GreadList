import pyautogui
import serial
ser = serial.Serial('COM3',9600)
def port():
	ser.flushInput()
	while True:
		char = str(ser.readline(),'UTF-8')
		char2 = char[:-2]
		xo,o,yo = char2.partition('y')
		x = int(xo)
		y = int(yo)

		if (508-x)>50 and abs(508-y)<50:
			pyautogui.move(0,-20) 

		if (508-x)>50 and (508-y)>50:
			pyautogui.move(20,-20) 

		if abs(508-x)<50 and (508-y)>50:
			pyautogui.move(20,0) 

		if (x-508)>50 and (508-y)>50:
			pyautogui.move(20,20) 

		if (x-508)>50 and abs(508-y)<50:
			pyautogui.move(0,20) 

		if (x-508)>50 and (y-508)>50:
			pyautogui.move(-20,20) 

		if abs(508-x)<50 and (y-508)>50:
			pyautogui.move(-20,0) 

		if (508-x)>50 and (y-508)>50:
			pyautogui.move(-20,-20) 
