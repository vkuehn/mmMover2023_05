from time import sleep


def write(ser, command):
    command = str(command) + '\r'
    ser.write(command.encode())


def serial_read(ser):
    sleep(0.1)
    data = b''

    wait_bytes = ser.inWaiting()
    print(str(wait_bytes) + ' bytes waiting in serial port')
    for i in range(ser.inWaiting()):
        b = ser.read(1)
        if b != b'\r':
            if b == b'\n':
                return data
            else:
                data += b
    return False
