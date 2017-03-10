import cv2
from numpy import zeros, where, shape

###################
###################
###################

class Cam:
    
    number = 0
    imageLocation = "."
    spots = []
    edgeLimLo = 100
    edgeLimHi = 200
    
    def __init__(self, s, cams):
        self.init( s, cams )
        return

    def init( self, sl, cam_dict ):
        self.number = cam_dict['number']
        self.image_location = cam_dict['im_full_path']
        self.spots = []
        for s in cam_dict['spots']:
            
            # Init spot class with config vals
            n = s['number']
            sl[s['number']].init( s )
            
            # Add spot number to list of cameras children spots
            self.spots.append(n)
        
        print "cam number  ", self.number
        print "    spots ", self.spots
        return

    def analyze( self, Spots, image=None ):
        
        if image is None:
            image = self.imageLocation

	# Allow for image to be a filename or CV2 object
	if isinstance(image, basestring):
	    im = cv2.imread(image)
	else:
	    im = image

        # Get edges in image (use mask later)
        edges = cv2.Canny( im, self.edgeLimLo, self.edgeLimHi )
	
        # Loop over spots, writing number of edges for each
        for sn in Spots:
            
            # Get the polygon vertices for the spot
            verts = Spots[sn].vertices
            
            # Make (boolean) mask for spot
            mask = zeros((im.shape[0],im.shape[1]))
            cv2.fillConvexPoly(mask,verts,1)
            bMask = mask.astype(bool)
            
            # Make integer mask for surfing
            iMask = bMask.astype('uint8')
            
            ### Get number of edges
            spotEdges = edges[bMask]
            edgeInds = where(spotEdges == 255)
            Spots[sn].nEdges = shape(edgeInds)[1]
            
        return



