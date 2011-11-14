#!/usr/bin/env python
import csv
import os
import math
import sys
import datetime
import subprocess
import time

if len(sys.argv) != 2:
  print "USAGE: update_bw_chart.py [minutely|hourly]"
  sys.exit()

if sys.argv[1] == 'minutely':
  db = '/home/mirror/web/bw_minutely.csv'
  label = 'Last Hour'
  num_samples = 60
else:
  db = '/home/mirror/web/bw_hourly.csv'
  label = 'Last Day'
  num_samples = 48

# Read in the last hour's (day's) samples
history = []
reader = csv.reader(open(db, 'r'))
for row in reader:
  history.append((int(row[0]), int(row[1]), int(row[2])))

# Grab the current in/out gauge readings. These will wrap every 16 million TB, so expect frequent errors
xin, xout = subprocess.check_output('cat /proc/net/dev | grep eth2 | cut -d : -f 2 | awk \'{print $1, $9}\'', shell=True).split(' ')

# Throw out the oldest sample and push our new one onto the list
history = history[-(num_samples - 1):]
history.append((int(time.time()), int(xin), int(xout)))

# Save the data with our new sample at the end
with open(db, 'wb') as db_file:
  writer = csv.writer(db_file)
  writer.writerows(history)

# We go through the list and calculate transfer rate for each time block between two samples
last_in = history[0][1]
last_out = history[0][2]
last_time = history[0][0]

transfers = []
for sec, xin, xout in history[1:]:
  timediff = sec - last_time
  if timediff == 0:
    timediff = 1
  transfers.append((sec, 8 * (xin - last_in) / float(timediff) / 1000000.0, 8 * (xout - last_out) / float(timediff) / 1000000.0))
  last_in = xin
  last_out = xout
  last_time = sec

# Figure out what the range of our chart should be
scale = 1
for sec, xin, xout in transfers:
  if xout > scale:
   # I want the chart's top showable value to be the smallest number of Mbit/sec
   # divisible by 50 that's greater than the higest sampled rate
   #  (so max(speed)=99 -> 100; max(speed)=51 -> 100)
   xout = int(math.ceil(xout)) 
   scale = (xout / 50) * 50 + 50

# Format each sampled rate as a percentage of the maximal allowable value
format_xfers = ["%d" % (100 * xout / scale) for sec, xin, xout in transfers]

# Pack the samples into a comma-separated list for gcharts
format_str = ','.join(format_xfers)

if sys.argv[1] == 'hourly':
  #begin_hour = (transfers[0][0] / 3600) % 24
  begin_halfhour = datetime.datetime.now().hour * 2 + datetime.datetime.now().minute / 30
  label_str = ','.join([str((h - begin_halfhour + 48) % 48) for h in range(0, 47, 8)])
  print "<img src=\"http://chart.apis.google.com/chart?chxl=1:|00|04|08|12|16|20&chxp=1,%s&chxr=0,0,%d|1,0,48&chxs=1,676767,11.5,0,lt,676767&chxt=y,x&chs=400x225&cht=lc&chco=3D7930&chd=t:%s&chg=14.3,-1,1,1&chls=2,4,0&chm=B,C5D4B5BB,0,0,0&chtt=Throughput (%s, Mb/s)\"/>" % (label_str, scale, format_str, label)
else:
  #begin_minute = (transfers[0][0] / 60) % 60
  begin_minute = datetime.datetime.now().minute
  label_str = ','.join([str((m - begin_minute + 60) % 60) for m in range(0, 59, 10)])
  print '<img src="http://chart.apis.google.com/chart?chxl=1:|%%3A00|%%3A10|%%3A20|%%3A30|%%3A40|%%3A50&&chxp=1,%s&chxr=0,0,%d|1,0,60&chxs=1,676767,11.5,0,lt,676767&chxt=y,x&chs=400x225&cht=lc&chco=3D7930&chd=t:%s&chg=-1,-1,0,0&chls=2,4,0&chm=B,C5D4B5BB,0,0,0&chtt=Throughput (%s, Mb/s)"/>' % (label_str, scale, format_str, label)


