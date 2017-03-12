from json import load as jl

import notifications as notify
import files

from sys import exit as quit

from cv2 import imwrite
import os

###################
###################
###################

class Spot:
    vertices = []
    base_nEdges = 0
    monthly = 0
    handicap = 0
    nEdges = 0
    imageTimeStamp = 0
    tPresent = 0
    presenceStartTime = 0
    occupied = 0
    timeOccupied = 0
    occupationStartTime = 0
    occupationEndTime = 0
    occupationThresh = 0
    paid = 0
    payStartTime = ''
    payEndTime = ''
    lps = ''
    lpn = ''
    violation = 0
    failedDetection = 0
    image = []
    ffname = []
    faultyCamera = False

    def __init__(self,n):
        self.number = n
        self.nEdges = 0
        self.image = []
        self.ffname = []
        self.faultyCamera = False

    def init( self, spot_dict, t2occ=60 ):
        if self.number is not spot_dict['number']:
            quit()
        self.vertices = spot_dict['vertices']
        self.base_nEdges = spot_dict['base_nEdges']
        self.monthly = spot_dict['monthly']
        self.handicap = spot_dict['handicap']


    def update_occupation( self, now=None ):
        
        # Allow image timestamp to be provided
        # Default to the member value
        if now is None:
            now = self.imageTimeStamp

        # No updates of any sort if monthly or handicapped
        if self.monthly or self.handicap:
            return
        
        # Update the time since presence was detected in spot
        self.timePresent(now)

        # If presence is long enough, mark as occupied
        self.evaluate_occupation(now)

        
    def evaluate_occupation( self, now ):
        
        # Present longer than thresh?
        if self.tPresent > self.occupationThresh:
            if not self.occupied:
                self.occupied = True
                self.occupationStartTime = now

            self.timeOccupied = now - self.occupationStartTime
        
        # Was occupied, but no longer present
        elif self.occupied:
            self.occupationEndTime = now
            self.occupied = False
        
        # Was not occupied, not present
        else:
            self.occupied = False
            
        
    def timePresent( self, now ):
        if self.presenceStartTime is 0:
            self.presenceStartTime = now

        if self.presence():
            self.tPresent = now - self.presenceStartTime
        else:
            self.tPresent = 0
            self.presenceStartTime = now


    def presence(self):
        # Edge based presence only
        return self.nEdges > self.base_nEdges


    def update_status( self, freeTime, imdir='.', vdir='.', udir='.' ):
        
        # Write spot image to directory
        fname = 'spot%d.jpg' % self.number
        self.ffname = os.path.join(imdir,fname)
        imwrite(self.ffname,self.image)

        # If monthly, nothing to do
        if self.monthly:
            return
        
        # Occupied too long, not paid --> violator !
        if self.timeOccupied > freeTime and not self.paid:
            if not self.violation:

                self.violation = True
                
                lt = time.localtime(self.occupationStartTime)
                tss = time.strftime('%Y%m%dT%H%M%S',lt)
                
                vfname = 'spot%d_%s.jpg' % (ss,tss)
                vfname = os.path.join( vdir, vfname )
                copied = try_copy( ffname, vfname ) 
                if copied:
                    send_image = vfname
                else:
                    send_image = fname
                sub = "Violation"
                msg = """
                %s
                Spot %d in VIOLATION
                """ % (time.asctime(lt), s)
                notify.send_msg_with_jpg( sub, msg, send_image, team )
        else:
            self.violation = False
            
            if self.paid == 1 and self.tPresent == 0:
                pst = self.payStartTime
                pet = self.payEndTime
                
                oet = self.occupationEndTime

                if oet < pst :
                    if not self.failedDetection:
                        self.failedDetection = True

                        tss = self.payStartTime
                        pstt = time.localtime(tss)
                        pss = time.strftime('%Y%m%dT%H%M%S',pstt)
                        
                        ufname = 'spot%d_%s.jpg' % (ss,pss)
                        ufname = os.path.join( udir, ufname )
                        copied = try_copy( ffname, ufname ) 
                        if copied:
                            send_image = ufname
                        else:
                            send_image = fname
                        sub = "Failed Detection?"
                        msg = """
                        %s
                        Spot %d Detection Failed, or ...
                        Person left spot within pay period
                        """ % (pss, s)
                        notify.send_msg_with_jpg( sub, msg, send_image, to )
                else:
                    self.failedDetection = False
            else:
                self.failedDetection = False

        return

