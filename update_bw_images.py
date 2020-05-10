#!/usr/bin/env python
import csv
import os
import math
import sys
import datetime
import subprocess
import time
import pygal
from pygal import Config
from pygal.style import Style

def process_data(db, label, num_samples):

  # Read in the last hour's (day's) samples
  history = []
  reader = csv.reader(open(db, 'r'))
  for row in reader:
    history.append((int(row[0]), int(row[1]), int(row[2])))

  ## Grab the current in/out gauge readings. These will wrap every 16 million TB, so expect frequent errors
  #xin, xout = subprocess.check_output('cat /proc/net/dev | grep eth1 | cut -d : -f 2 | awk \'{print $1, $9}\'', shell=True).split(' ')
  #
  ## Throw out the oldest sample and push our new one onto the list
  #history = history[-(num_samples - 1):]
  #history.append((int(time.time()), int(xin), int(xout)))
  #
  ## Save the data with our new sample at the end
  #with open(db, 'wb') as db_file:
  #  writer = csv.writer(db_file)
  #  writer.writerows(history)

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
  #return [(100 * xout / scale) for sec, xin, xout in transfers]
  return [xout for sec, xin, xout in transfers]

def get_range(data):
  max_scale = 1
  for point in data:
    if point > max_scale:
      # I want the chart's top showable value to be the smallest number of Mbit/sec
      # divisible by 50 that's greater than the higest sampled rate
      #  (so max(speed)=99 -> 100; max(speed)=51 -> 100)
      max_scale = (int(math.ceil(point)) / 50) * 50 + 50
  return [0, max_scale]

def make_image(data, filepath, title, labels, major_labels):
  custom_style = Style(
    background='#fff',
    plot_background='transparent',
    title_font_size=14,
    guide_stroke_dasharray = '1,0',
    major_guide_stroke_dasharray = '1,0',
    foreground='rgba(0, 0, 0, .87)',
    foreground_strong='rgba(0, 0, 0, .87)',
    foreground_subtle='rgba(0, 0, 0, .87)',
    stroke_opacity='1',
    stroke_opacity_hover='1',
    stroke_width=10,
    stroke_width_hover=10,
    opacity='1',
    opacity_hover='1',
    colors=('#C5D4B5BB', '#3D7930')
  )
  print(custom_style.to_dict())

  r = get_range(data)

  config = Config()
  config.interpolate = 'cubic'
  config.style = custom_style
  config.width=400
  config.height=225
  config.explicit_size=True
  config.margin_left=0
  config.margin_right=0
  config.margin_top=10
  config.margin_bottom=30
  config.show_minor_x_labels = False
  config.truncate_label=-1
  config.show_legend=False
  config.include_x_axis = True
  config.range = r
  config.show_dots = False

  chart = pygal.Line(config)
  chart.title = ("Throughput (%s, Mb/s)" % (title))
  chart.x_labels = labels
  chart.x_labels_major = major_labels
  chart.y_labels = [x for x in range(0, r[1] + 1, 100 if (r[1] > 550) else 50)]
  chart.add(None, data, fill=True)
  chart.add(None, data)
  #with open(filepath, 'w') as output:
  #  output.write(chart.render())
  chart.render_to_png(filepath)


if __name__ == "__main__":
  now = datetime.datetime.now()

  data = process_data('/home/mirror/web/bw_minutely.csv', 'Last Hour', 60)
  labels = [':' + str((m + now.minute) % 60) for m in range(0, 59)]
  make_image(data, '/home/mirror/web/bw_minutely.png', 'Last Hour', labels, [':0', ':10', ':20', ':30', ':40', ':50'])

  data = process_data('/home/mirror/web/bw_hourly.csv', 'Last Day', 48)
  labels = [str((h - (now.hour * 2 + now.minute / 30) + 48) % 48) for h in range(0, 47, 8)]
  make_image(data, '/home/mirror/web/bw_hourly.png', 'Last Day', labels, ['00', '04', '08', '12', '16', '20'])

