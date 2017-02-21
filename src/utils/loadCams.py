import numpy as np

def loadCameras( time=0, threshSurf=400, edgeLims=[100,200], t2occ=60 ):
    
    camera1 = {
        'number': 1,
        'port': 9001,
        'im_ts': time,
        'nFails': 0,
        'spots': [
            {
                'number': 1,
                'center': [   0,  40],
                'sTresh': 100,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 2,
                'center': [  10,  40],
                'sTresh': 100,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera2 = {
        'number': 2,
        'port': 9002,
        'im_ts': time,
        'nFails': 0,
        'spots': [
            {
                'number': 3,
                'center': [   0,  40],
                'sTresh': 100,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 4,
                'center': [  10,  40],
                'sTresh': 100,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    cameras = {1: camera1,
               2: camera2}
    
    return cameras
