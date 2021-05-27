# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'front.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot
from bnk_options import Ui_bnkScrn
import datetime, math, os, cv2, glob, dlib, pyttsx3, face_recognition
from PIL import Image
import numpy as np
from keras.models import model_from_json
from scipy.ndimage import imread
from scipy.misc import imresize, imsave
from tqdm import tqdm
from collections import defaultdict
from imutils.video import VideoStream
from tensorflow.keras.models import load_model
import mysql.connector

IMG_SIZE = 24

#setting speech lines
l0 = "QR code reader initialized..."
l1 = "Please hold the QR Code in front of the camera."
l2 = "Card expired. Please contact your bank."
l3 = "Card verified. Please proceed."
l4 = "Spoof detection system initialized..."
l5 = "Please hold your face still in the camera."
l6 = "Face verified. Please proceed with the transaction."
l7 = "Spoof detected. This account will be blocked."
l8 = "Face detection and recognition system initialized..."
l9 = "Multiple faces detected. Aborting transaction"

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(959, 639)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 960, 640))
        self.frame_2.setStyleSheet("background-color: rgb(33, 170, 229);\n"
"background-color: rgb(173, 127, 168);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.topLabel = QtWidgets.QTextBrowser(self.frame_2)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 961, 111))
        self.topLabel.setStyleSheet("background-color: rgb(225, 255, 253);")
        self.topLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.topLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.topLabel.setLineWidth(3)
        self.topLabel.setObjectName("topLabel")
        self.welcomeText = QtWidgets.QTextBrowser(self.frame_2)
        self.welcomeText.setGeometry(QtCore.QRect(100, 200, 781, 221))
        self.welcomeText.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.welcomeText.setObjectName("welcomeText")
        self.startBtn = QtWidgets.QPushButton(self.frame_2)
        self.startBtn.setGeometry(QtCore.QRect(160, 470, 651, 41))
        self.startBtn.setToolTip("")
        self.startBtn.setToolTipDuration(2)
        self.startBtn.setStyleSheet("background-color: rgb(224, 255, 253);")
        self.startBtn.setObjectName("startBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.retranslateUi(MainWindow)
        self.startBtn.clicked.connect(self.tp)
        QtCore.QMetaObject.connectSlotsByName(MainWindow) 
    
    
    def tp(self):
        
        self.init_cam()
    
        
    def say(self, line):
        engine = pyttsx3.init()
        engine.say(line)
        engine.runAndWait()
        
    def init_cam(self):
        # initalize the cam
        self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        print("Webcam started")
        self.QRscan_read(self.cap)
        #face_det(cap)
        #go(cap)
        #closeDB(con)
        self.terminate(self.cap)
        
    def collect(self, c_no, cap):
        
        global c_nmber
        c_nmber = c_no
        self.conDB(c_no, cap)
        
    def conDB(self, c_no, cap):
        global mydb
        mydb = mysql.connector.connect(host='localhost', user='root', passwd='', db='atm')
        l = "DB connection established"
        #self.say(l)
        print(l)
        self.getAcc(mydb, c_no, cap) 
    
    def getAcc(self, con, c_no, cap):
        
        curs = con.cursor()
        sql = f"SELECT first_name FROM custs WHERE card_no = {c_no}"
        curs.execute(sql)
        res = curs.fetchone()
        fname = res[0]
        print(fname)
        
        sql1 = f"SELECT status FROM custs WHERE card_no = {c_no}"
        curs.execute(sql1)
        res1 = curs.fetchone()
        status = res1[0]
        
        if status == 'Active':
            self.face_det(cap, fname, c_no)
        else:
            l = "Account blocked. Please contact your bank"
            self.say(l)
            self.terminate(cap)
        self.closeDB(con)
        
    def blkAcc(self, con, c_no):
        
        curs = con.cursor()
        blk_sql = f"UPDATE custs SET status = 'Blocked' WHERE card_no = {c_no}"
        curs.execute(blk_sql)
        con.commit()
        self.closeDB(con)
        
    def closeDB(self, con):
        con.close()
        
    def QRscan_read(self, cap):
        
        self.say(l0)
        self.say(l1)
        
        # initialize the cv2 QRCode detector
        detector = cv2.QRCodeDetector()
        
        while True:
            _, self.img = self.cap.read()
            
            # detect and decode
            data, bbox, _ = detector.detectAndDecode(self.img)
            # check if there is a QRCode in the image
            if bbox is not None:
                # display the image with lines
                for i in range(len(bbox)):
                    # draw all lines
                    cv2.line(self.img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
                if data:
                    #print("[+] QR Code detected, data:", data)
                    cno = data[0:15]                          
                    card_from_date = data[17:22]              
                    card_exp_date = data[24:29]               
                    cfd = datetime.datetime.strptime(card_from_date, '%m/%y').date()
                    ced = datetime.datetime.strptime(card_exp_date, '%m/%y').date() 
                    cur = datetime.datetime.today().date() 
                    
                    if cur > ced:
                        #print("Card expired. Contact your bank")
                        self.say(l2)
                        self.terminate(cap)
                        break
                    else:
                        #print("Card good")
                        #say(l3)
                        self.luhn_algo(cno, cap)
                        break
                    
            # display the result
            self.display(self.img, cap)
            
    # luhn algo
    def luhn_algo(self, cno, cap):
        c = str(cno)
        bits = list(map(int, c))           # a list to store every bit of the card number as individual elements
        odd_sum = 0
        even_sum = 0
        total = 0           # sum of odd and even bits
        
        for i in range(0, len(bits)):
            if i == 0 or i % 2 == 0:
                even = bits[i] * 2
                if even > 9:
                    even1 = even % 10
                    even2 = math.trunc(even / 10) 
                    add = even2 + even1
                    even_sum += add
                else:
                    even_sum += even 
            else:
                odd_sum += bits[i]    
    
        total = odd_sum + even_sum
    
    # validation and calulation of the checksum     
        pre_check = total % 10
        if pre_check == 0:
            luhn_bit = 0
        else:
            luhn_bit = 10 - pre_check
    #    print("luhn_bit = ", luhn_bit) 
        
        if (pre_check + luhn_bit) != 10:
            print("something went wrong, check your QR code and try again")
            exit()
        else:
            l = str(luhn_bit)
            n = cno
            
            c_num = n + l
            #print("complete number =", c_num) 
            self.collect(c_num, cap)
    
        
    def face_det(self, cap, fname, c_no):
        
        self.say(l8)
        self.say(l5)
        
        detector = dlib.get_frontal_face_detector()
      
        # Capture frames continuously
        while cap.isOpened():
          
            # Capture frame-by-frame
            _, self.frame = self.cap.read()
            #frame = cv2.flip(frame, 1)
          
            # RGB to grayscale
            gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
            faces = detector(gray)
          
            # Iterator to count faces
            i = 0
            for face in faces:
          
                # Get the coordinates of faces
                x, y = face.left(), face.top()
                x1, y1 = face.right(), face.bottom()
                cv2.rectangle(self.frame, (x, y), (x1, y1), (0, 255, 0), 2)
          
                # Increment iterator for each face in faces
                i = i+1
          
            #cv2.waitKey(5000)
            if i > 1:
                #print("More than one face detected")
                self.say(l9)
                self.terminate(cap)
                self.blkAcc(mydb, c_no)
            else:
                self.face_rec(cap, fname, c_no)
                #print("1 face only")
          
            # Display the resulting frame
            self.display(self.frame, cap)
            
    def face_rec(self, cap, fname, c_no):
        
        faces_encodings = []
        faces_names = []
        
        cur_direc = os.getcwd()
        path = os.path.join(cur_direc, 'faces\\')
        
        list_of_files = [f for f in glob.glob(path+'*.jpg')]
        number_files = len(list_of_files)
        names = list_of_files.copy()
        
        for i in range(number_files):
            globals()['image_{}'.format(i)] = face_recognition.load_image_file(list_of_files[i])
            globals()['image_encoding_{}'.format(i)] = face_recognition.face_encodings(globals()['image_{}'.format(i)])[0]
            faces_encodings.append(globals()['image_encoding_{}'.format(i)])
        # Create array of known names
            names[i] = names[i].replace(cur_direc, "")  
            faces_names.append(names[i])
            
        # main block starts here
            
        face_locations = []
        face_encodings = []
        face_names = []
        process_this_frame = True
        
        video_capture = cap
        
        while cap.isOpened():
            _, self.frame = video_capture.read()
            small_frame = cv2.resize(self.frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = small_frame[:, :, ::-1]
            
            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
                face_names = []
                
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(faces_encodings, face_encoding)
                    name = "Unknown"
                    face_distances = face_recognition.face_distance(faces_encodings, face_encoding)
                    best_match_index = np.argmin(face_distances)
                    
                    if matches[best_match_index]:
                        name = faces_names[best_match_index]
                        
                    face_names.append(name)
                    
            process_this_frame = not process_this_frame
                        
        # Display the results
            for (top, right, bottom, left), name in zip(face_locations, face_names):
                top *= 4
                right *= 4
                bottom *= 4
                left *= 4
                
            # Draw a rectangle around the face
                cv2.rectangle(self.frame, (left, top), (right, bottom), (0, 255, 0), 2)
                name = name.replace('.jpg', '')
                name = name[7:]
                
                if name == fname:
                    l = "Face verified :"
                    #say(l)
                    print(l, fname)
                    self.go(cap)
                    # Input text label with a name below the face
                    #cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
                    font = cv2.FONT_HERSHEY_DUPLEX
                    cv2.putText(self.frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)
                    break
                else:
                    l = "Face change noticed. Aborting transaction"
                    self.say(l)
                    self.terminate(cap)
                
            self.display(self.frame, cap)
            break
            
    
    def load_pretrained_model(self):
        model = load_model('eye_status_classifier0.h5')
        return model
    
    def predict(self, img, model):
    	img = Image.fromarray(img, 'RGB').convert('L')
    	img = imresize(img, (IMG_SIZE,IMG_SIZE)).astype('float32')
    	img /= 255
    	img = img.reshape(1,IMG_SIZE,IMG_SIZE,1)
    	prediction = model.predict(img)
    	if prediction < 0.1:
    		prediction = 'closed'
    	elif prediction > 0.90:
    		prediction = 'open'
    	else:
    		prediction = 'idk'
    	return prediction
    
    def init(self):
        face_cascPath = 'haarcascade_frontalface_alt.xml'
        #face_cascPath = 'lbpcascade_frontalface.xml'
    
        open_eye_cascPath = 'haarcascade_eye_tree_eyeglasses.xml'
        left_eye_cascPath = 'haarcascade_lefteye_2splits.xml'
        right_eye_cascPath ='haarcascade_righteye_2splits.xml'
        dataset = 'faces'
    
        face_detector = cv2.CascadeClassifier(face_cascPath)
        open_eyes_detector = cv2.CascadeClassifier(open_eye_cascPath)
        left_eye_detector = cv2.CascadeClassifier(left_eye_cascPath)
        right_eye_detector = cv2.CascadeClassifier(right_eye_cascPath)
    
        model = self.load_pretrained_model()
    
        print("[LOG] Collecting images ...")
        images = []
        for direc, _, files in tqdm(os.walk(dataset)):
            for file in files:
                if file.endswith("jpg"):
                    images.append(os.path.join(direc,file))
        return (model,face_detector, open_eyes_detector, left_eye_detector,right_eye_detector, images)
    
    def process_and_encode(self, images):
        # initialize the list of known encodings and known names
        known_encodings = []
        known_names = []
        #print("[LOG] Encoding faces ...")
    
        for image_path in tqdm(images):
            # Load image
            image = cv2.imread(image_path)
            # Convert it from BGR to RGB
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
         
            # detect face in the image and get its location (square boxes coordinates)
            boxes = face_recognition.face_locations(image, model='cnn')
    
            # Encode the face into a 128-d embeddings vector
            encoding = face_recognition.face_encodings(image, boxes)
    
            # the person's name is the name of the folder where the image comes from
            name = image_path.split(os.path.sep)[-2]
    
            if len(encoding) > 0 : 
                known_encodings.append(encoding[0])
                known_names.append(name)
    
            encodings = {"encodings": known_encodings, "names": known_names}
            np.save('encodings.npy', encodings) 
    
        return encodings
    
    def isBlinking(self, history, maxFrames):
        """ @history: A string containing the history of eyes status 
             where a '1' means that the eyes were closed and '0' open.
            @maxFrames: The maximal number of successive frames where an eye is closed """
        for i in range(maxFrames):
            pattern = '1' + '0'*(i+1) + '1'
            if pattern in history:
                return True
        return False
    
    def detect_and_display(self, model, video_capture, face_detector, open_eyes_detector, left_eye_detector, right_eye_detector, data, eyes_detected):
            _, self.frame = video_capture.read()
            # resize the frame
            frame = cv2.resize(self.frame, (0, 0), fx=0.9, fy=0.9)
    
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Detect faces
            faces = face_detector.detectMultiScale(
                gray,
                scaleFactor=1.2,
                minNeighbors=5,
                minSize=(50, 50),
                flags=cv2.CASCADE_SCALE_IMAGE
            )
    
            # for each detected face
            for (x,y,w,h) in faces:
                # Encode the face into a 128-d embeddings vector
                encoding = face_recognition.face_encodings(rgb, [(y, x+w, y+h, x)])[0]
    
                # For now we don't know the person name
                name = "Unknown"
    
                face = frame[y:y+h,x:x+w]
                gray_face = gray[y:y+h,x:x+w]
    
                eyes = []
                
                # Eyes detection
                # check first if eyes are open (with glasses taking into account)
                open_eyes_glasses = open_eyes_detector.detectMultiScale(
                    gray_face,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    flags = cv2.CASCADE_SCALE_IMAGE
                )
                # if open_eyes_glasses detect eyes then they are open 
                if len(open_eyes_glasses) == 2:
                    eyes_detected[name]+='1'
                    for (ex,ey,ew,eh) in open_eyes_glasses:
                        cv2.rectangle(face,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                
                # otherwise try detecting eyes using left and right_eye_detector
                # which can detect open and closed eyes                
                else:
                    # separate the face into left and right sides
                    left_face = frame[y:y+h, x+int(w/2):x+w]
                    left_face_gray = gray[y:y+h, x+int(w/2):x+w]
    
                    right_face = frame[y:y+h, x:x+int(w/2)]
                    right_face_gray = gray[y:y+h, x:x+int(w/2)]
    
                    # Detect the left eye
                    left_eye = left_eye_detector.detectMultiScale(
                        left_face_gray,
                        scaleFactor=1.1,
                        minNeighbors=5,
                        minSize=(30, 30),
                        flags = cv2.CASCADE_SCALE_IMAGE
                    )
    
                    # Detect the right eye
                    right_eye = right_eye_detector.detectMultiScale(
                        right_face_gray,
                        scaleFactor=1.1,
                        minNeighbors=5,
                        minSize=(30, 30),
                        flags = cv2.CASCADE_SCALE_IMAGE
                    )
    
                    eye_status = '1' # we suppose the eyes are open
    
                    # For each eye check wether the eye is closed.
                    # If one is closed we conclude the eyes are closed
                    for (ex,ey,ew,eh) in right_eye:
                        color = (0,255,0)
                        pred = self.predict(right_face[ey:ey+eh,ex:ex+ew], model)
                        if pred == 'closed':
                            eye_status='0'
                            color = (0,0,255)
                        cv2.rectangle(right_face,(ex,ey),(ex+ew,ey+eh),color,2)
                    for (ex,ey,ew,eh) in left_eye:
                        color = (0,255,0)
                        pred = self.predict(left_face[ey:ey+eh,ex:ex+ew], model)
                        if pred == 'closed':
                            eye_status='0'
                            color = (0,0,255)
                        cv2.rectangle(left_face,(ex,ey),(ex+ew,ey+eh),color,2)
                    eyes_detected[name] += eye_status
    
                if self.isBlinking(eyes_detected[name],3):
                    cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                    # Display name
                    y = y - 15 if y - 15 > 15 else y + 15
                    cv2.putText(self.frame, 'Real', (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 255, 0), 2)
                    print("Spoof detection result: Real")
                    self.say(l6)
                    self.terminate(video_capture)
                    self.bnk_opsWindow()
                    break
                    # eyes_detected[name] = '111'
                else:
                    if len(eyes_detected[name]) > 20:
                        cv2.rectangle(self.frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                        # Display name
                        y = y - 15 if y - 15 > 15 else y + 15
                        cv2.putText(self.frame, 'Fake', (x, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 0, 255), 2)
                        print("Spoof detection result: Fake")
                        self.say(l7)
                        
                        self.terminate(video_capture)
                        self.blkAcc(mydb, c_nmber)
                        break
                    break
                break
    
    
            return frame
    
    def go(self, cap):
        
        #print("Spoof detector initialized")
        self.say(l4)
        #say(l5)
        
        (model, face_detector, open_eyes_detector, left_eye_detector, right_eye_detector, images) = self.init()
        
        #data = process_and_encode(images)
        data = np.load('encodings.npy',allow_pickle='TRUE').item()
        #print(known_names)
        
        video_capture = cap
        
        eyes_detected = defaultdict(str)
        while cap.isOpened():
          frame = self.detect_and_display(model, video_capture, face_detector, open_eyes_detector,left_eye_detector,right_eye_detector, data, eyes_detected)
          
          self.display(frame, cap)
        
    def display(self, img, cap):
        img = cv2.resize(img, (960, 640))
        cv2.imshow("Webcam", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            self.terminate(cap)
            
    def terminate(self, cap):
        cv2.destroyAllWindows()
        cap.release()
         
    
    #@pyqtSlot()
    def bnk_opsWindow(self):
        bnkScrn = QtWidgets.QDialog()
        ui = Ui_bnkScrn(c_nmber, mydb)
        ui.setupUi(bnkScrn)
        bnkScrn.show()
        QtCore.QTimer.singleShot(9000, bnkScrn.close)
        bnkScrn.exec_() 

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.topLabel.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; color:#000000;\">ENHANCED ATM - For Cardless and Secure Transactions</span></p></body></html>"))
        self.welcomeText.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt;\">WELCOME</span></p></body></html>"))
        self.startBtn.setText(_translate("MainWindow", "Start"))

#import splash_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

