# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:15:01 2020

@author: harsh
"""

import cv2
import datetime

def scan_read():
    
    # initalize the cam
    cap = cv2.VideoCapture(0)
    # initialize the cv2 QRCode detector
    detector = cv2.QRCodeDetector()
    from luhn import bits_ip
    while True:
        _, img = cap.read()
        # detect and decode
        data, bbox, _ = detector.detectAndDecode(img)
        # check if there is a QRCode in the image
        if bbox is not None:
            # display the image with lines
            for i in range(len(bbox)):
                # draw all lines
                cv2.line(img, tuple(bbox[i][0]), tuple(bbox[(i+1) % len(bbox)][0]), color=(255, 0, 0), thickness=2)
            if data:
                #print("[+] QR Code detected, data:", data)
                cno = data[0:14]
                card_from_date = data[16:21]
                card_exp_date = data[23:28]
                cfd = datetime.datetime.strptime(card_from_date, '%m/%y').date()
                ced = datetime.datetime.strptime(card_exp_date, '%m/%y').date() 
                cur = datetime.datetime.today().date() 
                
                if cur > ced:
                    print("Card expired. Contact your bank")
                else:
                    bits_ip(cno)
                break
        # display the result
        cv2.imshow("img", img)    
        if cv2.waitKey(1) == ord("q"):
            break
    #print(data)
    cap.release()
    cv2.destroyAllWindows()

#scan_read() 