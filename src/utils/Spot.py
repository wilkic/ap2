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
    presenceStartTime = 0,
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
    
    def __init__(self, s, t2occ=60):
        init( s, t2occ )

    def init( self, spot_dict, t2occ=60 ):
        number = spot_dict['number']
        vertices = spot_dict['vertices']
        base_nEdges = spot_dict['base_nEdgesr']
        monthly = spot_dict['monthly']
        handicap = spot_dict['handicap']

    def update_occupation():
        
        if monthly or handicap:
            return

        tP = timePresent()
        evaluate_occupation( tP )

        
    def evaluate_occupation(tP):
        
        # Present longer than thresh?
        if tP > occupationThresh:
            if not occupied:
                occupied = True
                occupationStartTime = now

            timeOccupied = now - occupationStartTime
        
        # Was occupied, but no longer present
        elif occupied:
            occupationEndTime = now
            occupied = False
        
        # Was not occupied, not present
        else:
            occupied = False
            
        
    def timePresent():
        if presence():
            tPresent = now - presenceStartTime
        else
            tPresent = 0
            presenceStartTime = now
        return tPresent

    def presence():
        # Edge based presence only
        if nEdges > base_nEdges:
            return True
        else
            return False



    def update_status():
        
