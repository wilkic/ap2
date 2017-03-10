#!/usr/bin/env python

from utils.Spot import Spot
from utils.Cam import Cam as Camera
from utils.Payment import Payment
from utils.notifications import send_msg as sm
import utils.dataRecording as log
import utils.table
from json import load as jl

import os
import time
import traceback

from copy import copy as copy

##########################################
##########################################
##########################################


sleepytime = 900

data_dir = os.getcwd()

# Spot numbers is a list of ints
spotNumbers = range(1,15)

violationThresh = 1200

config_fname = '../cfg/cam_config.json'

toForce = ['test@test.com']
toErr = ['test@test.com']
toSpam = ['test@test.com']

os.environ['TZ'] = 'US/Eastern'

##########################################
##########################################
##########################################

time.tzset()

# Create the spots
spots = {num:Spot(num) for num in spotNumbers}

# Read config file 
with open(config_fname) as f:
    camConfig = jl(f)

# Initialize the cameras (and spot info) from config
#cams = {cam['number']:Camera(spots,cam) for c, cam in camConfig.iteritems()}
cams = {}
for c, cam in camConfig.iteritems():
    tc = Camera( spots, cam )
    cams[cam['number']] = tc


# Read api config, pass to Payment for initialization
payLog = os.path.join(os.getcwd(),'pmAPI.log')
apiConfigFname = '../cfg/apiConfig.json'
with open(apiConfigFname) as f:
    apiConfig = jl(f)
payment = Payment( payLog, apiConfig, toErr )


# When getting the latest image, move it to a directory
# for processing... then delete it when done.
wd = os.path.join( data_dir, 'images_being_processed' )
if not os.path.exists(wd):
    os.makedirs(wd)

cd = os.path.join( data_dir, 'current_images' )
if not os.path.exists(cd):
    os.makedirs(cd)

vd = os.path.join( data_dir, 'images_of_violations' )
if not os.path.exists(vd):
    os.makedirs(vd)

ud = os.path.join( data_dir, 'images_of_undetections' )
if not os.path.exists(ud):
    os.makedirs(ud)

# Put spot logs in their own dir
sld, cld, csd = log.setupDirs( data_dir )

######################################
######################################
######################################

# BEGIN THE LOOP

######################################
######################################
######################################

#for index in range(0,3):
while True:
    
    try:
        
        # Update spots info from cameras
        for c, cam in cams.iteritems():
            cam.analyze(spots)

        # Update presence
        for s in spots.iteritems():
            s.update_occupation()

        # Get spot payment status
        payment.update(spots)

        # Determine violation
        for s in spots.iteritems():
            s.update_status()
        
        # Update table
        table.write(spots)

        # Log spot data
        for s in spots.iteritems():
            log.logSpot(now,s,cld)

    except Exception, e:
        tb = traceback.format_exc()
        msg = """
        %s
        Catch is going offline due to user error !
        Check my error logs for details...
        
        Exception:
        %s
        
        Traceback:
        %s""" % (time.asctime(),str(e),tb)
        print "%s\n\n%s" % (msg, str(e))
        sm('Error',msg,toErr)
        sys.exit()

    # Do it all over again, after some rest
    time.sleep(sleepytime)


