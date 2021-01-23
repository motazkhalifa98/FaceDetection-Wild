###############
#Author: Motaz Khalifa
#CSE 473 Project 3 Part 1
#Citations:
#	https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html
#	https://docs.opencv.org/3.3.0/d7/d8b/tutorial_py_face_detection.html
#	https://www.newbedev.com/python/howto/how-to-iterate-over-files-in-a-given-directory/
###############
import numpy as np
import cv2
import os
import json
import sys



if __name__ == "__main__":

    inputDirectory = sys.argv[1]

    json_list = []


    for filename in os.listdir(inputDirectory):
        if filename.endswith(".jpg"):

            imgname = os.path.join(inputDirectory,filename)
            img = cv2.imread(imgname)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
            eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

            faces = face_cascade.detectMultiScale(gray, 1.21, 3)

            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                element = {"iname": filename, "bbox": [int(x), int(y), int(w), int(h)]} #first element in json file
                json_list.append(element)                           #adding element to list
                roi_gray = gray[y:y+h, x:x+w]
                roi_color = img[y:y+h, x:x+w]
                eyes = eye_cascade.detectMultiScale(roi_gray)
                for (ex,ey,ew,eh) in eyes:
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)



            continue
        else:
            continue

    #the result json file name to test folder
    output_json_test_folder = inputDirectory + r'\results.json'
    #dump json_list to result.json
    with open(output_json_test_folder, 'w') as f:
        json.dump(json_list, f)
