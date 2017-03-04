from json import load as jl

def initCams( config_fname, t2occ=60 ):
    
    # Read spot config file
    with open(config_fname) as f:
        cams = jl(f)
    
    spotProperties = {
            'nEdges': 0,
            'timePresent': 0,
            'timeOccupied': 0,
            'occupationStartTime': 0,
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
            s.update(default)

    return cams


