from json import load as jl

from sys import exit as quit

###################
###################
###################

class Spot:
    number = 0,
    vertices = []
    base_nEdges = 0,
    monthly = 0,
    handicap = 0,
    nEdges = 0,
    timePresent = 0,
    timeOccupied = 0,
    occupationStartTime = 0,
    occupationEndTime = 0,
    occupationThresh = 0,
    paid = 0,
    payStartTime = '',
    payEndTime = '',
    lps = '',
    lpn = '',
    violation = 0,
    failedDetection = 0
    
    def __init__(self, s, t2occ=60)
        init( s, t2occ )

    def init( self, spot_dict, t2occ=60 ):
        number = spot_dict['number']
        vertices = spot_dict['vertices']
        base_nEdges = spot_dict['base_nEdgesr']
        monthly = spot_dict['monthly']
        handicap = spot_dict['handicap']


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



