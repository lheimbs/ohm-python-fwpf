#!/usr/bin/env python

import time, sys, os, argparse
import tb_esp_lin as espCtl
from datetime import datetime

ap = argparse.ArgumentParser()
ap.add_argument("-t", "--temp", type=int, default=25,
                help="Temperatur Schwellwert für Anschalten der LED")
ap.add_argument("-f", "--file", default="temp", help="Locaiton of Temperatur-File.")
FILE = ap.parse_args().file
TEMP = ap.parse_args().temp

start_time = time.time()
wait_time = 30.0

esp = espCtl.open_esp()
if not esp:
    print("Could not connect to esp!")
    exit 1

while True:
    curr_temp = espCtl.query_txt(esp, 'md')
    if curr_temp > TEMP:
        espCtl.write_txt(esp, '1')
    else:
        espCtl.write_txt(esp, '0')

    with open(FILE, "w") as f:
        f.write(f"Time: {datetime.now()} Temperature: {curr_temp}\n")

    now_time = time.time()
    if now_time - start_time > 60.0*5:
        break
    else:
        time.sleep(wait_time - ((now_time - start_time) % wait_time))