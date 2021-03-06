#!/usr/bin/env python
# -*- coding: utf-8 -*-

import config
import module
import clear
import sys
import time

from datetime import datetime
timestamp = time.time()
time_now = datetime.fromtimestamp(timestamp)
time_utc = datetime.utcfromtimestamp(timestamp)
utc_offset_secs = (time_now - time_utc).total_seconds()

# Flag variable to hold if the current time is behind UTC.
is_behind_utc = False

# If the current time is behind UTC convert the offset
# seconds to a positive value and set the flag variable.
if utc_offset_secs < 0:
    is_behind_utc = True
    utc_offset_secs *= -1

# Build a UTC offset string suitable for use in a timestamp.

if is_behind_utc:
    pos_neg_prefix = "-"
else:
    pos_neg_prefix = "+"

utc_offset = time.gmtime(utc_offset_secs)
utc_offset_fmt = time.strftime("%H", utc_offset)
gmt = int(pos_neg_prefix + utc_offset_fmt)

####Lade das Configfile
cfg = config.Config()
try:
  cfg.readConfig(sys.argv[1])
except:
  cfg.readConfig("config.ini")

clear = clear.Clear()
clear.clear(cfg.token,cfg.ivchatId,cfg)

modul = module.Module()
if cfg.nuller == "true":
  modul.nuller(cfg,gmt)
else:
	print("Es wurde nichts aktiviert. Pr\U000000fcfe im Configfile das die Attribute 'rocketStops' oder 'lureModule' auf 'true' gesetzt sind")