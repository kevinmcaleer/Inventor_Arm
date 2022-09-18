from phew import *
from phew import connect_to_wifi, server, logging
from phew import render_template
from config import wifi_ssid, wifi_password
from inventor import Inventor2040W, SERVO_1, SERVO_2, SERVO_3, SERVO_4, SERVO_5, SERVO_6 
from time import sleep
import math

# Connect to WiFi
ip = connect_to_wifi(wifi_ssid, wifi_password)

# Create a new board
board = Inventor2040W()

# Set all servos to mid position
for servo in board.servos:
    servo.to_mid()
    print(f'servo: {servo}, value {servo.value()}')
    sleep(1)

def position(arm=None, wrist=None, elbow=None, finger=None, base=None):
    """ Set the servo positions """
    if finger is not None:
        board.servos[SERVO_2].value(finger)
    if arm is not None:
        board.servos[SERVO_4].value(arm)
    if wrist is not None:
        board.servos[SERVO_3].value(wrist)
    if elbow is not None:
        board.servos[SERVO_5].value(elbow)
    if base is not None:
        board.servos[SERVO_6].value(base)
    sleep(0.01)

@server.route('/', methods=['GET','POST'])
def index(request):

    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        
        elbow = request.form.get("elbow", None)
        arm = request.form.get("arm", None)
        base = request.form.get("base", None)
        finger = request.form.get("finger", None)
        wrist = request.form.get("wrist", None)
        if elbow is not None:
            position(elbow=int(elbow))
        if arm is not None:
            position(arm=int(arm))
        if base is not None:
            position(base=int(base))
        if wrist is not None:
            position(wrist=int(wrist))
        if finger is not None:
            position(finger=int(finger))

        # Try without the line below to speed up the response
        return render_template('index.html')
    

# Show the IP Address
logging.info(f'IP: {ip}')
logging.is_disabled = True

# Start the server
server.run()