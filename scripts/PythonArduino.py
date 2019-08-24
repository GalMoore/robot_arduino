#!/usr/bin/env python

import serial # you need to install the pySerial :pyserial.sourceforge.net
import time
from std_msgs.msg import String
import rospy

arduino = serial.Serial('/dev/ttyACM1', 9600)

def listener_callback(data):

 	if data.data =="listening":
		print "Listnening = LED on..."
		# time.sleep(1) 
		arduino.write('H') 

	elif data.data =="not listening":
		print "Not listening = LED off..."
		# time.sleep(1) 
		arduino.write('L')


if __name__ == '__main__':
	
	print("Starting arduino script")
	rospy.init_node('Python_Arduino_node')
	arduino.write('H')
	# time.sleep(2)
	rospy.Subscriber('/is_robot_listening', String, listener_callback)
	rospy.spin()

























# rospy.Subscriber('/is_robot_listening', String, listener_callback)




# def onOffFunction():
# 	command = raw_input("Type something..: (on/ off / bye )")
# 	if command =="on":
# 		print "The LED is on..."
# 		time.sleep(1) 
# 		arduino.write('H') 
# 		onOffFunction()

# 	elif command =="off":
# 		print "The LED is off..."
# 		time.sleep(1) 
# 		arduino.write('L')
# 		onOffFunction()

# 	elif command =="bye":
# 		print "See You!..."
# 		time.sleep(1) 
# 		arduino.close()
# 	else:
# 		print "Sorry..type another thing..!"
# 		onOffFunction()

# time.sleep(2) #waiting the initialization...

# onOffFunction()
























# #!/usr/bin/env python

# import serial # you need to install the pySerial :pyserial.sourceforge.net
# import time
# from std_msgs.msg import String
# import rospy

# # your Serial port should be different!
# arduino = serial.Serial('/dev/ttyACM0', 9600)

# def onOffFunction():
# 	command = raw_input("Type something..: (on/ off / bye )")
# 	if command =="on":
# 		print "The LED is on..."
# 		time.sleep(1) 
# 		arduino.write('H') 
# 		onOffFunction()

# 	elif command =="off":
# 		print "The LED is off..."
# 		time.sleep(1) 
# 		arduino.write('L')
# 		onOffFunction()

# 	elif command =="bye":
# 		print "See You!..."
# 		time.sleep(1) 
# 		arduino.close()
# 	else:
# 		print "Sorry..type another thing..!"
# 		onOffFunction()

# time.sleep(2) #waiting the initialization...

# onOffFunction()