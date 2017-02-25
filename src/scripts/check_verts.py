
import os

import numpy as np
import matplotlib.pyplot as plt
import cv2

import json
import pprint as pp

import ipdb



plt.close("all")

def onclick(event):
    print('button=%d, x=%d, y=%d, xdata=%f, ydata=%f' %
          (event.button, event.x, event.y, event.xdata, event.ydata))


camera1 = {
    'number': 1,
    'im_full_path': '/home/acp/work/ggp/bpark/imgs/cam1.jpg',
    'spots': [
        {
            'number': 1,
            'vertices': np.array(
                        [[   0, 130],
                         [  56, 132],
                         [  22, 200],
                         [   0, 200]]),
            'base_nEdges': 0,
        },
        {
            'number': 2,
            'vertices': np.array(
                        [[  70, 135],
                         [ 145, 140],
                         [ 140, 210],
                         [  40, 200]]),
            'base_nEdges': 0,
        },
        {
            'number': 3,
            'vertices': np.array(
                        [[ 160, 145],
                         [ 240, 145],
                         [ 260, 205],
                         [ 155, 210]]),
            'base_nEdges': 0,
        },
    ]
}

camera2 = {
    'number': 2,
    'im_full_path': '/home/acp/work/ggp/bpark/imgs/cam2.jpg',
    'spots': [
        {
            'number': 4,
            'vertices': np.array(
                        [[ 220,   0],
                         [ 400, 100],
                         [ 400, 224],
                         [ 220, 224]]),
            'base_nEdges': 6,
        },
        {
            'number': 5,
            'vertices': np.array(
                        [[  40,  50],
                         [ 175, 224],
                         [   0, 224],
                         [   0, 180]]),
            'base_nEdges': 0,
        },
    ]
}

camera3 = {
    'number': 3,
    'im_full_path': '/home/acp/work/ggp/bpark/imgs/cam3.jpg',
    'spots': [
        {
            'number': 1,
            'vertices': np.array(
                        [[   0, 130],
                         [  56, 132],
                         [  22, 200],
                         [   0, 200]]),
            'base_nEdges': 0,
        },
        {
            'number': 2,
            'vertices': np.array(
                        [[  70, 135],
                         [ 145, 140],
                         [ 140, 210],
                         [  40, 200]]),
            'base_nEdges': 0,
        },
        {
            'number': 3,
            'vertices': np.array(
                        [[ 160, 145],
                         [ 240, 145],
                         [ 260, 205],
                         [ 155, 210]]),
            'base_nEdges': 0,
        },
        {
            'number': 4,
            'vertices': np.array(
                        [[ 255, 145],
                         [ 320, 145],
                         [ 340, 174],
                         [ 262, 170]]),
            'base_nEdges': 0,
        },
        {
            'number': 5,
            'vertices': np.array(
                        [[ 333, 150],
                         [ 379, 150],
                         [ 392, 166],
                         [ 345, 166]]),
            'base_nEdges': 0,
        },
        {
            'number': 6,
            'vertices': np.array(
			[[49, 38],
			 [78, 38],
			 [65, 48],
			 [31, 50]]),
            'base_nEdges': 0,
        },
        {
            'number': 7,
            'vertices': np.array(
			[[90, 39],
			 [124, 39],
			 [114, 49],
			 [79, 50]]),
            'base_nEdges': 0,
        },
        {
            'number': 8,
            'vertices': np.array(
			[[134, 40],
			 [167, 41],
			 [165, 54],
			 [125, 52]]),
            'base_nEdges': 0,
        },
        {
            'number': 9,
            'vertices': np.array(
			[[176, 42],
			 [206, 45],
			 [213, 58],
			 [176, 54]]),
            'base_nEdges': 0,
        },
        {
            'number': 10,
            'vertices': np.array(
			[[218, 47],
			 [247, 50],
			 [258, 65],
			 [224, 61]]),
            'base_nEdges': 0,
        },
        {
            'number': 11,
            'vertices': np.array(
			[[260, 52],
			 [282, 55],
			 [303, 72],
			 [273, 66]]),
            'base_nEdges': 0,
        },
        {
            'number': 12,
            'vertices': np.array(
			[[300, 59],
			 [316, 61],
			 [338, 79],
			 [316, 74]]),
            'base_nEdges': 0,
        },
        {
            'number': 13,
            'vertices': np.array(
			[[333, 64],
			 [348, 68],
			 [373, 87],
			 [354, 83]]),
            'base_nEdges': 0,
        },
        {
            'number': 14,
            'vertices': np.array(
			[[362, 70],
			 [373, 73],
			 [396, 91],
			[ 384, 88]]),
            'base_nEdges': 0,
        },

    ]
}

camera = camera3

_plot = True

fname = camera['im_full_path']

im = cv2.imread(fname)

#im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny( im, 100, 200 )

if _plot is True:
    #plt.ion()
    imc = np.copy(im)
    imc[:,:,0] = edges
    fig = plt.figure(figsize=(10,6))
#    plt.imshow(imc)
    
    cid = fig.canvas.mpl_connect('button_press_event', onclick)

for spot in camera['spots']:

    verts = spot['vertices']
    verts.astype('int32')
    cv2.polylines(imc,[verts],True,(0,255,255))

plt.imshow(imc)
plt.show()


for spot in camera['spots']:
    
#    if spot['number'] != 38:
#        continue
    
    verts = spot['vertices']
    
    mask = np.zeros((im.shape[0],im.shape[1]))
    cv2.fillConvexPoly(mask,verts,1)
    bMask = mask.astype(bool)
    
    spotEdges = edges[bMask]
    edgeInds = np.where(spotEdges == 255)
    spot['base_nEdges'] = np.shape(edgeInds)[1]

#
#    imm = np.zeros_like(im).astype('uint8')
#
#    
#    if _plot is True:
#        
#        for color in range(0,3):
#            imm[bMask,color] = im[bMask,color]
#        imm[bMask,0] = edges[bMask]
#        ims = np.copy(imm)
#        sfig = plt.figure(figsize=(10,6))
#        plt.imshow(ims)
#
#    if _plot is True: 
#        plt.show()

if _plot is True:
    plt.figure()
    plt.ioff()
    plt.close()


for spot in camera['spots']:
    pp.pprint(spot)


