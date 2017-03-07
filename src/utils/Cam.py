
###################
###################
###################

class Cam:
    
    number = 0
    image_location = "."
    spots = []
    edgeLimLo = 100
    edgeLimHi = 200
    
    def __init__(self, spots, cams)
        init( spots, cams )
        return

    def init( self, Spots, cam_dict ):
        number = cam_dict['number']
        image_location = cam_dict['im_full_path']
        for s in cam_dict['spots']:
            
            # Init spot class with config vals
            spot = Spot( s )
            
            # Write the spot into the spots dict
            Spots[spot.number] = spot

            # Add spot number to list of cameras children spots
            spots.append(spot.number)

        return

    def analyze( Spots, image=image_location ):
        
	# Allow for image to be a filename or CV2 object
	if isinstance(image, basestring):
	    im = cv2.imread(image)
	else:
	    im = image

        # Get edges in image (use mask later)
        edges = cv2.Canny( im, edgeLimLo, edgeLimHi )
	
        # Loop over spots, writing number of edges for each
        for sn in spots:
            
            # Get the polygon vertices for the spot
            verts = Spots[sn].vertices
            
            # Make (boolean) mask for spot
            mask = np.zeros((im.shape[0],im.shape[1]))
            cv2.fillConvexPoly(mask,verts,1)
            bMask = mask.astype(bool)
            
            # Make integer mask for surfing
            iMask = bMask.astype('uint8')
            
            ### Get number of edges
            spotEdges = edges[bMask]
            edgeInds = np.where(spotEdges == 255)
            Spots[sn].nEdges = np.shape(edgeInds)[1]
            
        return



