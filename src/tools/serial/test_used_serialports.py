import serial.tools.list_ports
from time import sleep

import common as cm


print('search used serial ports')
ports = list(serial.tools.list_ports.comports())
if len(ports) == 0:
    print('no used ports found')
for p in ports:
    print('write to ' + p.description + ' on port ' + p.device)
    ser = serial.Serial(p.device, 38400)
    cm.write(ser, '?')
    sr = cm.serial_read(ser)
    if isinstance(sr, bool):
        sr = str(sr)
    else:
        sr = str(sr.decode())
    print('Serial result was ' + sr)

