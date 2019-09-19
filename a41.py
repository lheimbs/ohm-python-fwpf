#!/usr/bin/env python

import time, sys, os, argparse
import tb_esp as espCtl
from datetime import datetime

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--temp", type=float, default=20,
                help="Temperatur Schwellwert für Anschalten der LED")
ap.add_argument("-f", "--file", default="temp", help="Locaiton of Temperatur-File.")
ap.add_argument("-w", "--wait", type=int, default=30, help="Time to wait between readings.")
FILE = ap.parse_args().file
TEMP = ap.parse_args().temp
WAIT = ap.parse_args().wait

def main():
    start_time = time.time()
    esp = espCtl.open_esp()
    if not esp:
        print("Could not connect to esp!")
        exit(1)

    print(f"Read Temperatures, write values to {FILE} and tun LED on if its > {TEMP}")

    while True:
        curr_temp = espCtl.query_txt(esp, 'md').strip('=')
        if float(curr_temp) > TEMP:
            espCtl.write_txt(esp, '1')
        else:
            espCtl.write_txt(esp, '0')

        with open(FILE, "a+") as f:
            now = datetime.now().strftime("%d.%m.%Y, %H:%M:%S")
            f.write(f"Time: {now} Temperature: {curr_temp}\n")

        now_time = time.time()
        if now_time - start_time > 60.0*5:
            break
        else:
            time.sleep(WAIT - ((now_time - start_time) % WAIT))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Bye")
