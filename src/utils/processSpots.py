import time

import os, sys
sys.path.append("..")
import notifications as notify



def judge( spots, freeTime, monthlies, to, team, imdir, vdir, udir ):

    for s, spot in spots.iteritems():
        
        if s in monthlies:
            continue

        if spot['timeOccupied'] > freeTime and not spot['paid']:
            if not spot['violation']:

                spot['violation'] = True
                
                lt = time.localtime(spot['occupationStartTime'])
                tss = time.strftime('%Y%m%dT%H%M%S',lt)
                
                ss = str(s)
                fname = 'spot' + ss + '.jpg'
                fname = os.path.join( imdir, fname )
                vfname = 'spot' + ss + '_' + tss + '.jpg'
                vfname = os.path.join( vdir, vfname )
                copied = try_copy( fname, vfname ) 
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
            spot['violation'] = False
            
            if spot['paid'] == 1 and spot['timePresent'] == 0:
                pst = spot['payStartTime']
                pet = spot['payEndTime']
                
                oet = spot['occupationEndTime']

                if oet < pst :
                    if not spot['failedDetection']:
                        spot['failedDetection'] = True

                        tss = spot['payStartTime']
                        pstt = time.localtime(tss)
                        pss = time.strftime('%Y%m%dT%H%M%S',pstt)
                        

                        ss = str(s)
                        fname = 'spot' + ss + '.jpg'
                        fname = os.path.join( imdir, fname )
                        ufname = 'spot' + ss + '_' + pss + '.jpg'
                        ufname = os.path.join( udir, ufname )
                        copied = try_copy( fname, ufname ) 
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
                    spot['failedDetection'] = False
            else:
                spot['failedDetection'] = False

    return
