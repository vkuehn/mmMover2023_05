import serial.tools.list_ports
import sys

import common as cm

device = '/dev/ttyACM0'


def serial_active(device_name):
    for p in ports:
        if p.device == device_name:
            return True
    return False


print('search used serial ports')
ports = list(serial.tools.list_ports.comports())
if len(ports) == 0:
    print('no used ports found')
    sys.exit()
    
if not serial_active(device):
    print(device + ' is not part of active ports')
    sys.exit()

for i in range(1000):
    print('{}   write to device {}'.format(str(i), device))
    ser = serial.Serial(device, 38400)
    cm.write(ser, 'led13')
    sr = cm.serial_read(ser)
    if isinstance(sr, bool):
        sr = str(sr)
    else:
        sr = str(sr.decode())
    print('Serial result was ' + sr)
