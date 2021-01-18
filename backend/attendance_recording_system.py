import face_recognition
import os 
import cv2
import random
import numpy as np
import psycopg2
from datetime import datetime
import requests
from threading import Thread
import pickle
import time
from PIL import Image
from dotenv import load_dotenv
from tqdm import tqdm
load_dotenv()

KNOWN_FACES_DIR = 'known_faces_attendance'

def check(url):
    requests.get(url)

def check_and_forget(url):
    Thread(target=check, args=(url,)).start()

def turnOn():
    global AARS_ON
    AARS_ON = True
    
    cwd = os.getcwd()
    
    TOLERANCE = 0.2
    FRAME_THICKNESS = 1
    FONT_THICKNESS = 2
    RESIZE_SCALE = 0.3
    MODEL = "cnn"

    video_capture = cv2.VideoCapture(0)

    # print("loading known faces")

    known_face_encodings = []
    known_face_niks = []

    with tqdm(total=len(os.listdir(KNOWN_FACES_DIR)), desc='Loading known faces') as pbar:
        for nik in os.listdir(KNOWN_FACES_DIR):
            for filename in os.listdir(f"{KNOWN_FACES_DIR}/{nik}"):
                try:
                    image = face_recognition.load_image_file(f"{KNOWN_FACES_DIR}/{nik}/{filename}")
                    encoding = face_recognition.face_encodings(image)[0]
                    # encoding = pickle.load(open(f"{KNOWN_FACES_DIR}/{nik}/{filename}", "rb"))
                    known_face_encodings.append(encoding)
                    known_face_niks.append(nik)
                except:
                    pass
            pbar.update(1)    

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_niks = []
    process_this_frame = True

    while video_capture is not None and video_capture.isOpened():
        # if len(known_face_encodings) == 0:
        #     print("0")
        #     break
        
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=RESIZE_SCALE, fy=RESIZE_SCALE)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_niks = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                # print(matches)
                nik = "Unknown"

                # Or instead, use the known face with the smallest distance to the new face
                if len(known_face_encodings) > 0:
                    face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    if matches[best_match_index]:
                        nik = known_face_niks[best_match_index]
                        
                # Wajah dikenali
                if nik != "Unknown":
                    # Hey I Know You !
                    nik_nama = nik.split('-')[0]
                    nik_id = nik.split('-')[1]
                    check_and_forget(f'http://localhost:5000/check/{nik_id}')
                    # print(f"known face, {nik_id}")
                    face_niks.append(nik_nama)
                else:
                    face_niks.append(nik)

        process_this_frame = not process_this_frame


        # Display the results
        for (top, right, bottom, left), nik in zip(face_locations, face_niks):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            multiplicate = int(1/RESIZE_SCALE)
            top *= multiplicate
            right *= multiplicate
            bottom *= multiplicate
            left *= multiplicate

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, nik, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow("AARS | click video and press 'q' to stop", frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            AARS_ON = False
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()

def turnOff():
    video_capture.release()
    cv2.destroyAllWindows()
    AARS_ON = False
    AARS_READY = True
    return 'turning off aars'

def camera_is_being_used():
    cap = cv2.VideoCapture(0) 
    if cap is None or not cap.isOpened():
        return 'Warning: unable to open video'
    else:
        return 'camera ready'

if __name__ == "__main__":
    turnOn()
