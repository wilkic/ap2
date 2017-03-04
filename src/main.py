#!/usr/bin/env python

import utils.cams as Cams
import utils.dataRecording as log

##########################################
##########################################
##########################################


sleepytime = 900

data_dir = os.getcwd()

nSpots = 14
monthlies = []
handicaps = []

timePresentBeforeOccupied = 60
violationThresh = 1200

ip = "108.45.109.111"

toForce = ['test@test.com']
toErr = ['test@test.com']
toSpam = ['test@test.com']

os.environ['TZ'] = 'US/Eastern'
time.tzset()

# Read config file 
with open(config_fname) as f:
    camConfig = jl(f)

# Initialize the cameras
cams = {}
for c, cam in camConfig.iteritems():
    cams[cam['number']] = Camera( cam )


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
dirs = {'sld':sld,'cld':cld,'csd':csd,'wd':wd,'cd':cd}

# Create the list of spots
spots = processSpots.create(nSpots,monthlies,handicaps,cameras,ip)

#for index in range(0,3):
while True:
    
    try:
        
        # Get edges per spot
        cams.analyze()

        # Determine presence based on edges
        cams.determine_all_presence()

        # Evaluate if presence persistence merits occupation
        cams.

        # Get spot payment status

        # Determine violation

        # Update table

        # Log all data

        processCameras.processCameras( cameras, dirs, toErr, toSpam )
        
        processSpots.write( cameras, spots )
        
        processApi.processApi( data_dir, spots, monthlies, toErr )
        
        processSpots.judge( spots, violationThresh, monthlies, toErr, toForce, cd, vd, ud )

        writeTable.writeTable( spots )
        writeDemo.writeTable( spots )

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
        notify.send_msg('Error',msg,toErr)
        sys.exit()

    # Do it all over again, after some rest
    time.sleep(sleepytime)


