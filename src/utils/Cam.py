import cv2
from numpy import zeros, where, shape, array
from files import parse_ts

###################
###################
###################

class Cam:
    
    number = 0
    imageLocation = '.'
    tsLocation = '.'
    spots = []
    edgeLimLo = 100
    edgeLimHi = 200
    
    def __init__(self, s, cams):
        self.init( s, cams )
        return

    def init( self, sl, cam_dict ):
        self.number = cam_dict['number']
        self.imageLocation = cam_dict['im_full_path']
        self.tsLocation = cam_dict['ts_full_path']
        self.spots = []
        for s in cam_dict['spots']:
            
            # Init spot class with config vals
            n = s['number']
            sl[s['number']].init( s )
            
            # Add spot number to list of cameras children spots
            self.spots.append(n)
        
        #print "cam number  ", self.number
        #print "    spots ", self.spots
        return

    def analyze( self, Spots, image=None, ts=None ):
        
        if image is None:
            image = self.imageLocation

	# Allow for image to be a filename or CV2 object
	if isinstance(image, basestring):
	    im = cv2.imread(image)
	else:
	    im = image
        
        # If the image is empty, do nothing
        if im is None:
            return

        # Allow for timestamp to be a filename or value
        if ts is None:
            ts = self.tsLocation
	if isinstance(ts, basestring):
            ts = parse_ts( ts )
                
         
        # Get edges in image (use mask later)
        edges = cv2.Canny( im, self.edgeLimLo, self.edgeLimHi )
	
        # Loop over this cameras spots,
        # writing number of edges for each
        for sn in self.spots:
            
            # Grab reference to the spot from Spot dictionary 
            # based on lookup of key (spot number)
            # from the spot number list for this camera
            spot = Spots[sn]

            # Log the image timestamp to each spot
            spot.imageTimeStamp = ts
            
            # Get the polygon vertices for the spot
            verts = array( spot.vertices ).astype('int32')
            
            # Make (boolean) mask for spot
            mask = zeros((im.shape[0],im.shape[1]))
            
            cv2.fillConvexPoly(mask,verts,1)
            bMask = mask.astype(bool)
            
            # Make integer mask for surfing
            iMask = bMask.astype('uint8')
            
            ### Get number of edges
            spotEdges = edges[bMask]
            edgeInds = where(spotEdges == 255)
            spot.nEdges = shape(edgeInds)[1]

            # Write spot image with edges/outline to itself
            imc = im.copy()
            v = verts.astype('int32')
            cv2.polylines(imc,[verts],True,(0,255,255))
            spot.image = imc

        return



