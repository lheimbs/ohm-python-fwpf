
# tb_esp_lin.py
# Ansteuerung des Messprogramms auf ESP-8266 Mikrocontroller-Board
# 26.02.2018 V1: Jürgen Krumm, Startversion
# 19.09.2018 V2: Jürgen Krumm, Bootloader-Garbage herausfiltern
# 24.02.2019 V3: Jürgen Krumm, Gemeinsame Version für Win/Linux

import serial
import time
import sys

def write_txt(esp, cmd):
    esp.write(bytes(cmd, "utf-8"))

def query_txt(esp, cmd):
    while esp.readline(): pass    
    write_txt(esp, cmd)
    msg = ""
    while True:
        resp = esp.readline().strip()
        if len(resp) == 0: break
        msg = resp
    return msg.decode("ascii")
    
def query_bytes(esp, cmd):
    while esp.readline(): pass    
    write_txt(esp, cmd)
    resp=esp.readline().strip()
    return resp

def flush_txt(esp):
    nbytes = 0
    while esp.inWaiting() > 0:
        amount=esp.inWaiting()
        data=esp.read(amount)
        nbytes += len(data)
        #print(nbytes, data.hex(), data)
    return nbytes


def open_esp():
    for idx in range(0, 8):
        if sys.platform == "linux":
            port = "/dev/ttyUSB%d" % idx
        else:
            port = "COM%d:" % idx
            
        try:
            esp = serial.serial_for_url(port)
            esp.baudrate = 115200
            esp.timeout = 0.1
            for idx in range(4):
                while flush_txt(esp): pass
                rsp=query_bytes(esp, "0")
                if rsp == b"=ok": return esp
        except Exception as ex:            
            #print(ex)
            pass

    return None

if __name__ == "__main__":
    esp = open_esp()
    print(esp)
    if esp:
        # ESP-LED an
        write_txt(esp, "1")
        # 1 Sekunde warten
        time.sleep(1)
        # ESP-LED aus
        write_txt(esp, "0")
        # 1 Sekunde warten
        time.sleep(1)
        # ESP-LED ein
        write_txt(esp, "1")


        for idx in range(10):
            print("***")
            # Wert messen mit m und als Dezimalwert mit d abholen
            print (query_txt(esp, "md"))
            

        # ESP-LED aus
        write_txt(esp, "0")
