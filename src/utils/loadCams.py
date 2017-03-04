from json import load as jl

def initCams( config_fname, t2occ=60 ):
    
    # Read spot config file
    with open(config_fname) as f:
        cams = jl(f)
    
    default = {
            'nEdges': 0,
            'timePresent': 0,
            'timeOccupied': 0,
            'occupationStartTime': 0,
            'occupationEndTime': 0,
            'occupationThresh': t2occ
    }
    
    for i, c in cams.iteritems():
        for s in c['spots']:
            s.update(default)

    return cams


