import numpy as np

def loadCameras( time=0, threshSurf=400, edgeLims=[100,200], t2occ=60 ):

    camera1 = {
        'number': 1,
        'port': 9001,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 1,
                'vertices': np.array(
                            [[   0,   0],
                             [  30,   0],
                             [  60, 150],
                             [   0, 150]]),
                'base_means': [118,123,127],
                'base_nEdges': 404,
                'base_nKeys': 11,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'meanThresh': 15,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 2,
                'vertices': np.array(
                            [[  90,   0],
                             [ 290,   0],
                             [ 230, 224],
                             [ 110, 224]]),
                'base_means': [117,117,115],
                'base_nEdges': 419,
                'base_nKeys': 18,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 15,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 3,
                'vertices': np.array(
                            [[ 310,   0],
                             [ 400,   0],
                             [ 400, 224],
                             [ 250, 224]]),
                'base_means': [119,119,117],
                'base_nEdges': 479,
                'base_nKeys': 3,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 15,
                'edgeThresh': 200,
                'keyThresh': 20,
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
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 4,
                'vertices': np.array(
                            [[ 215,   0],
                             [ 370,   0],
                             [ 400, 100],
                             [ 400, 224],
                             [ 210, 224]]),
                'base_means': [126,126,125],
                'base_nEdges': 121,
                'base_nKeys': 4,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 5,
                'vertices': np.array(
                            [[  50,   0],
                             [ 200,   0],
                             [ 195, 224],
                             [   0, 224],
                             [   0, 170]]),
                'base_means': [130,130,131],
                'base_nEdges': 652,
                'base_nKeys': 35,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera3 = {
        'number': 3,
        'port': 9003,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 6,
                'vertices': np.array(
                            [[ 280,   0],
                             [ 380,   0],
                             [ 400,  35],
                             [ 400, 224],
                             [ 330, 224]]),
                'base_means': [102,102,101],
                'base_nEdges': 4,
                'base_nKeys': 1,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 7,
                'vertices': np.array(
                            [[ 130,   0],
                             [ 265,   0],
                             [ 310, 224],
                             [ 105, 224]]),
                'base_means': [122,123,121],
                'base_nEdges': 152,
                'base_nKeys': 11,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 8,
                'vertices': np.array(
                            [[  20,   0],
                             [ 115,   0],
                             [  85, 224],
                             [   0, 224],
                             [   0,  40]]),
                'base_means': [137,137,140],
                'base_nEdges': 730,
                'base_nKeys': 43,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera4 = {
        'number': 4,
        'port': 9004,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 9,
                'vertices': np.array(
                            [[ 325,  25],
                             [ 380,  25],
                             [ 400,  50],
                             [ 400, 220],
                             [ 385, 150]]),
                'base_means': [125,126,126],
                'base_nEdges': 425,
                'base_nKeys': 2,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 10,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 10,
                'vertices': np.array(
                            [[ 165,  30],
                             [ 260,  30],
                             [ 370, 224],
                             [ 240, 224]]),
                'base_means': [121,122,119],
                'base_nEdges': 67,
                'base_nKeys': 2,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 11,
                'vertices': np.array(
                            [[  40,  40],
                             [ 145,  40],
                             [ 210, 224],
                             [  40, 224]]),
                'base_means': [119,119,119],
                'base_nEdges': 63,
                'base_nKeys': 5,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera5 = {
        'number': 5,
        'port': 9005,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 12,
                'vertices': np.array(
                            [[ 310,   0],
                             [ 400,   0],
                             [ 400, 224],
                             [ 360, 224]]),
                'base_means': [99,101,103],
                'base_nEdges': 2,
                'base_nKeys': 1,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 13,
                'vertices': np.array(
                            [[ 135,   0],
                             [ 290,   0],
                             [ 330, 224],
                             [  85, 224]]),
                'base_means': [122,122,121],
                'base_nEdges': 405,
                'base_nKeys': 24,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 14,
                'vertices': np.array(
                            [[  20,   0],
                             [ 115,   0],
                             [  60, 224],
                             [   0, 224],
                             [   0,  30]]),
                'base_means': [119,119,121],
                'means': [0,0,0],
                'base_nEdges': 650,
                'base_nKeys': 25,
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }

    camera6 = {
        'number': 6,
        'port': 9006,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 15,
                'vertices': np.array(
                            [[   0,  40],
                             [  30,  40],
                             [ 100, 170],
                             [   0, 170]]),
                'base_means': [121,118,118],
                'base_nEdges': 187,
                'base_nKeys': 1,
                'base_means': [114,113,113],
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 16,
                'vertices': np.array(
                            [[  85,  20],
                             [ 290,  20],
                             [ 235, 170],
                             [ 140, 170]]),
                'base_means': [110,113,113],
                'base_nEdges': 115,
                'base_nKeys': 16,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 17,
                'vertices': np.array(
                            [[ 400,   0],
                             [ 400,  85],
                             [ 350, 150],
                             [ 300, 155]]),
                'base_means': [123,125,125],
                'base_nEdges': 28,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 22,
                'vertices': np.array(
                            [[ 150, 200],
                             [ 275, 200],
                             [ 255, 230],
                             [ 155, 225]]),
                'base_means': [166,163,163],
                'base_nEdges': 122,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
        ]
    }

    camera7 = {
        'number': 7,
        'port': 9007,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 18,
                'vertices': np.array(
                            [[   0,  40],
                             [  75,  40],
                             [ 120, 125],
                             [   0, 100]]),
                'base_means': [115,113,113],
                'base_nEdges': 53,
                'base_nKeys': 1,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 19,
                'vertices': np.array(
                            [[  90,  20],
                             [ 325,  20],
                             [ 265, 130],
                             [ 135, 130]]),
                'base_means': [110,113,113],
                'base_nEdges': 115,
                'base_nKeys': 16,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 20,
                'vertices': np.array(
                            [[ 355,   0],
                             [ 400,   0],
                             [ 400, 120],
                             [ 385, 135],
                             [ 280, 135]]),
                'base_means': [109,111,111],
                'base_nEdges': 58,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 23,
                'vertices': np.array(
                            [[ 110, 190],
                             [ 290, 200],
                             [ 280, 224],
                             [ 110, 224]]),
                'base_means': [166,163,163],
                'base_nEdges': 122,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
        ]
    }

    camera8 = {
        'number': 8,
        'port': 9008,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 21,
                'vertices': np.array(
                            [[  70,  25],
                             [ 169,  25],
                             [ 140, 224],
                             [   0, 224],
                             [   0, 130]]),
                'base_means': [105,105,105],
                'base_nEdges': 0,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
        ]
    }

    camera9 = {
        'number': 9,
        'port': 9009,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 24,
                'vertices': np.array(
                            [[  80,  40],
                             [ 155,  30],
                             [  95, 170],
                             [  35, 165],
                             [  15, 120]]),
                'base_means': [138,137,135],
                'base_nEdges': 31,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 25,
                'vertices': np.array(
                            [[ 172,  30],
                             [ 260,  30],
                             [ 290, 100],
                             [ 145, 100]]),
                'base_means': [112,112,112],
                'base_nEdges': 11,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 26,
                'vertices': np.array(
                            [[ 275,  30],
                             [ 350,  30],
                             [ 395,  70],
                             [ 390, 160],
                             [ 340, 165]]),
                'base_means': [136,135,134],
                'base_nEdges': 9,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
        ]
    }

    camera10 = {
        'number': 10,
        'port': 9010,
        'im_ts': time,
        'threshSurf': threshSurf,
        'edgeLims': edgeLims,       
        'spots': [
            {
                'number': 27,
                'vertices': np.array(
                            [[  60,  35],
                             [ 140,  35],
                             [ 105, 130],
                             [   0, 130],
                             [   0, 105]]),
                'base_means': [145,145,145],
                'base_nEdges': 0,
                'base_nKeys': 0,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            },
            {
                'number': 28,
                'vertices': np.array(
                            [[ 270,  40],
                             [ 345,  40],
                             [ 400, 105],
                             [ 400, 170],
                             [ 325, 190]]),
                'base_means': [135,135,135],
                'base_nEdges': 0,
                'base_nKeys': 4,
                'means': [0,0,0],
                'sigs': [0,0,0],
                'maxs': [0,0,0],
                'mins': [0,0,0],
                'mean': 0,
                'meanThresh': 10,
                'edgeThresh': 200,
                'keyThresh': 20,
                'timePresent': 0,
                'timeOccupied': 0,
                'occupationStartTime': time,
                'occupationEndTime': time,
                'occupationThresh': t2occ
            }
        ]
    }


    cameras = {1: camera1,
               2: camera2,
               3: camera3,
               4: camera4,
               5: camera5,
               6: camera6,
               7: camera7,
               8: camera8,
               9: camera9,
               10: camera10}
    
    return cameras
