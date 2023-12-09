import smbus
import time


if __name__ == "__main__":
    address = 0x48
    bus = smbus.SMBus(1)
    while True:
        val = bus.read_byte(address)
        val = int(val)
        print(val)
        bus.write_byte_data(address, 0x40, val)
        time.sleep(1)
