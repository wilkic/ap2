#!/usr/bin/env python

import os

import numpy as np
import pylab

import matplotlib.pyplot as plt

import ipdb

import time
import datetime as dt

import sys

import traceback

sys.path.append(os.getcwd())
import dataRecording as log
import loadCameras as lc
import processSpots
import processCameras

sys.path.append("..")
import notifications as notify
import get_image as gi

##########################################
##########################################
##########################################


sleepytime = 30


ip = "108.45.109.111"

#to = ['info@goodspeedparking.com',
#      '3474005261@tmomail.net',
#      '3102452197@mms.att.net']
to = ['info@goodspeedparking.com']

threshSurf = 400
edgeLims = [100, 200]


cameras = lc.loadCameras( time.time(), threshSurf, edgeLims )

# When getting the latest image, move it to a directory
# for processing... then delete it when done.
wd = os.path.join( os.getcwd(), 'images_being_processed' )
if not os.path.exists(wd):
    os.makedirs(wd)

# Put spot logs in their own dir
sld, cld, csd = log.setupDirs( os.getcwd() )
dirs = {'sld':sld,'cld':cld,'csd':csd,'wd':wd}

spots = processSpots.create()

#for index in range(0,10):
while True:
    
    try:

        processCameras.processCameras( ip, cameras, dirs, to )
        processSpots.write( cameras, spots )

        processPayments( spots )

        writeTable( spots )

    except Exception, e:
        traceback.print_exc()
        msg = """
        %s
        Catch is going offline due to user error !
        Check my error logs for details...
        %s """ % (str(dt.datetime.now()),str(e))
        #notify.send_msg(msg,to)
        print "%s\n\n%s" % (msg, str(e))
        sys.exit()

    # Do it all over again, after some rest
    time.sleep(sleepytime)

