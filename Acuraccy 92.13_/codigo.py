import cv2 as cv
import numpy as np
import time
import os
cap = cv.VideoCapture(0, cv.CAP_V4L )
whT = 416
confThreshold =0.5
nmsThreshold= 0.3

classNames = ['verde','rojo']
modelConfiguration = "yolov4-tiny5.cfg"
modelWeights = "yolov4-tiny5.weights"
net = cv.dnn.readNetFromDarknet(modelConfiguration, modelWeights)
net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

def findObjects(outputs,img):
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []
    for output in outputs:
        for det in output:
            scores = det[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > confThreshold:
                w,h = int(det[2]*wT) , int(det[3]*hT)
                x,y = int((det[0]*wT)-w/2) , int((det[1]*hT)-h/2)
                bbox.append([x,y,w,h])
                classIds.append(classId)
                confs.append(float(confidence))

    indices = cv.dnn.NMSBoxes(bbox, confs, confThreshold, nmsThreshold)
    
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        if x>wT/2:
            leetexto("lado izquierda" + classNames[classIds[i]])
        else:
            leetexto("lado derecha " + classNames[classIds[i]])

def leetexto(texto):
    scommand='espeak -ves+f5'+ ' "' + texto + '"'
    os.system(scommand)
while True:
    success, img = cap.read()
    blob = cv.dnn.blobFromImage(img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
    net.setInput(blob)
    layersNames = net.getLayerNames()
    outputNames = [(layersNames[i[0] - 1]) for i in net.getUnconnectedOutLayers()]
    outputs = net.forward(outputNames)
    findObjects(outputs,img)
    time.sleep(4)