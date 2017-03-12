
import requests
import time
from pprint import pprint as pp
from notifications import send_msg as sm


class Payment:
    nFails = 0
    url = 'https://api.parkmobile.us/nforceapi/parkingrights/zone/3125?format=json'
    usr = ''
    pwd = ''
    log = ''
    notification_reception = ''

    
    def __init__(self, logfname, apicfg, to='' ):
        self.log = logfname
        self.pwd = apicfg['pwd']
        self.usr = apicfg['usr']
        self.url = apicfg['url']
        self.notification_reception = to


    def update( self, spots ):

        i = 0
        while True:
            try:
                resp = requests.get(self.url,
                                    auth=(self.usr,self.pwd),
                                    verify=True)
                break
            except Exception, e:
                i += 1
                print 'BAD NEWS PARKMOBILE!'
                print 'Error number %d' % (i)
                if i==5:
                    msg = """
                    %s
                    Park Mobile API is not responding!
                    """ % time.asctime()
                    sm('Error',msg,to)
                    nFails += 1
                    if nFails == 5:
                        raise

        # Populate spots based on response
        if resp.status_code != 404:
            try:
                # Read data
                data = resp.json()
                
                # Log it
                with open(self.log,'a') as out:
                    print >> out, time.asctime()
                    pp( data, stream=out )
                
                # Write it to spot object
                assign( data, spots )

            except Exception, e:
                print "PM API returning crap JSON?"
                print "Exception: \n%s" % str(e)
                print "Response: \n%s" % resp.text

        return




    def assign( self, data, spots ):
        
        if 'parkingRights' in data:
            paid = []
            for i in data['parkingRights']:
                
                # Get space number
                sn = int( i['spaceNumber'] )

                # Make sure space number is a valid spot
                if sn > len(spots):
                    continue
                if not spots[sn]:
                    continue

                spots[ sn ].lpn = str(i['lpn'])
                spots[ sn ].lps = str(i['lpnState'])
                
                psstr = str(i['startDateLocal'])
                pestr = str(i['endDateLocal'])
                
                if psstr:
                    pstt = time.strptime(psstr[0:19],"%Y-%m-%dT%H:%M:%S")
                    pst = time.mktime(pstt)
                    spots[ sn ].payStartTime = pst
                if pestr:
                    pett = time.strptime(pestr[0:19],"%Y-%m-%dT%H:%M:%S")
                    pet = time.mktime(pett)
                    spots[ sn ].payEndTime = pet
                
                # Mark as paid if currently within paid window
                now = time.time()
                if now > spots[sn].payStartTime:
                    
                    if now < spots[sn].payEndTime:
                        spots[ sn ]['paid'] = 1
                        paid += [sn]
            
            for s,spot in spots.iteritems():
                if s not in paid and not spot.monthly:
                    spot.paid = 0

        return

