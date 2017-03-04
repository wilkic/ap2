from json import load as jl

from sys import exit as quit

###################
###################
###################

class Cam:
    
    number = 0
    image_location = "."
    spots = []
    
    def __init__(self, c)
        init( c )

    def init( self, cam_dict ):
        number = cam_dict['number']
        image_location = cam_dict['im_full_path']
        for s in cam_dict['spots']:
            
            # Init spot class with config vals
            spot = Spot( s )

            # Add it to the list
            spots.append(spot)

    def 

    def init( self, config_fname, t2occ=60 ):
        
        # Read spot config file
        with open(config_fname) as f:
            cams = jl(f)
        
        spotProperties = {
                'nEdges': 0,
                'timePresent': 0,
                'timeOccupied': 0,
        `        'occupationStartTime': 0,
                'occupationEndTime': 0,
                'occupationThresh': t2occ,
                'paid': 0,
                'payStartTime': '',
                'payEndTime': '',
                'lps': '',
                'lpn': '',
                'monthly': 0,
                'handicap': 0,
                'violation': 0,
                'failedDetection': 0
        }
        
        for i, c in cams.iteritems():
            for s in c['spots']:
                s.update(spotProperties)

        return cams


###################
###################
###################

def setSpotProp( cams, spotNum, prop, val ):

    for c, cam in cams:
        
        for s in cam['spots']:
            
            if s['number'] is spotNum:
                s[prop] = val
                return
    
    msg = 'Property %s not found in spots in cams' % prop
    print msg
    quit()
    #notify.send_msg('Error',msg,toErr)



