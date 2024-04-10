global intial
mp_drawing = mp.solutions.drawing_utils
global intialtime

import cv2 
import pyautogui
import mediapipe as mp
import time
from math import sqrt,pow
screen_width,screen_height = pyautogui.size()

mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
intial = None
intialtime = time.time()
global switchappmenu
switchappmenu = None
def mediapipe_detection(image, model):
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # COLOR CONVERSION BGR 2 RGB
    image.flags.writeable = False                  # Image is no longer writeable
    results = model.process(image)                 # Make prediction
    image.flags.writeable = True                   # Image is now writeable 
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR) # COLOR COVERSION RGB 2 BGR
    return image, results

def mousecondtion(landmarks,h):
    # middlefingertip = landmarks[12].x + landmarks[12].y
    ringfingertip =  landmarks[16].y*h
    pinkyfingertip =  landmarks[20].y*h
    # middlefingerbase = landmarks[9].x + landmarks[9].y
    ringfingerbase = landmarks[13].y*h
    pinkyfingerbase = landmarks[17].y*h
    indexfingertip = landmarks[8].y*h
    indexfingermiddle =  landmarks[6].y*h
    # ringfingertip = landmarks[16].x + landmarks[16].y
    # pinkyfingertip = landmarks[20].x + landmarks[20].y
    # # middlefingerbase = landmarks[9].x + landmarks[9].y
    # ringfingerbase = landmarks[13].x + landmarks[13].y
    # pinkyfingerbase = landmarks[17].x + landmarks[17].y
    # indexfingertip = landmarks[8].x + landmarks[8].y
    # indexfingermiddle = landmarks[6].x + landmarks[6].y
    if ringfingerbase < ringfingertip  and pinkyfingerbase < pinkyfingertip and indexfingermiddle > indexfingertip:
        return True
    else:
        return False


def parallel_lines(line1:list,line2:list):
    slope1 = (line1[1][1] - line1[0][1] ) / (line1[1][0] - line1[0][0])
    slope2 = (line2[1][1] - line2[0][1] ) / (line2[1][0] - line2[0][0])
    if slope1==slope2:
        return True
    else:
        return False

def switchapps(landmarks,h):
    # middlefingertip = (int(landmarks[12].x*w) ,int(landmarks[12].y*h))
    # ringfingertip = (int(landmarks[16].x*w) ,int(landmarks[16].y*h))
    # pinkyfingertip =  (int(landmarks[20].x*w),int(landmarks[20].y*h))
    # middlefingerbase = (int(landmarks[9].x*w),int(landmarks[9].y*h))
    # ringfingerbase = (int(landmarks[13].x*w),int(landmarks[13].y*h))
    # pinkyfingerbase = (int(landmarks[17].x*w),int(landmarks[17].y*h))
    # indexfingertip = (int(landmarks[8].x*w),int(landmarks[8].y*h))
    # # indexfingermiddle = landmarks[6].x + landmarks[6].y
    # indexfingerbase = (int(landmarks[5].x*w) + int(landmarks[5].y*h))
    middlefingertip = landmarks[12].y*h
    ringfingertip = landmarks[16].y*h
    pinkyfingertip =  landmarks[20].y*h
    middlefingerbase = landmarks[9].y*h
    ringfingerbase = landmarks[13].y*h
    pinkyfingerbase = landmarks[17].y*h
    indexfingertip = landmarks[8].y*h
    # indexfingermiddle = landmarks[6].x + landmarks[6].y
    indexfingerbase = landmarks[5].y*h
    if middlefingerbase < middlefingertip and ringfingerbase < ringfingertip and pinkyfingerbase > pinkyfingertip and indexfingerbase > indexfingertip:
        return True
    else:
        return False
    
def draw_styled_landmarks(image, results):
    # print(intial)
    global intial,intialtime,switchappmenu
    if results.multi_hand_landmarks:
        # count = 0
        # thumb = results.multi_hand_landmarks[0][4]
        # cv2.putText(image,"thumb",(thumb.x,thumb.y),cv2.FONT_HERSHEY_SIMPLEX ,1,(255,0,225))
        for hand_landmarks in results.multi_hand_landmarks:
            l = hand_landmarks.landmark
            # print(l[4].x)
            # if count == 4:
            h,w,_ = image.shape
            cv2.putText(image,"thumb",(int(l[4].x*w),int(l[4].y*h)),cv2.FONT_HERSHEY_SIMPLEX ,1,(255,0,225))
            # cv2.line(image,(int(l[4].x*w),int(l[4].y*h)),(int(l[8].x*w),int(l[8].y*h)),(255,0,245),10)
            # if intial is None:
            #     intial = (int(l[8].x*w),int(l[8].y*h))
            # distance = sqrt(pow(l[8].x*w - intial[0],2)+pow(l[8].y*h-intial[1],2))
            # if distance>=w/2:
            #     print("distance : ",distance)
            #     if intial>(int(l[8].x*w),int(l[8].y*h)):
            #         print("swaping left")
            #         swipe_right()
            #     if intial<(int(l[8].x*w),int(l[8].y*h)):
            #         print("swaping right")
            #         swipe_right()
            # cv2.line(image,intial,(int(l[8].x*w),int(l[8].y*h)),(255,0,245),10)
            # intial = (int(l[8].x*w),int(l[8].y*h))
            thumb = (int(l[4].x*w),int(l[4].y*h))
            indexfinger = (int(l[5].x*w),int(l[5].y*h))
            pinkyfinger = (int(l[17].x*w),int(l[17].y*h))
            middlefingertip = l[12].y*h
            middlefingerbase =  l[9].y*h
            if mousecondtion(l,h):
                # if  thumb>indexfinger  and thumb < pinkyfinger:    
                #     pass
                if switchappmenu:
                    switchappmenu = False
                if middlefingerbase>middlefingertip:
                        pyautogui.rightClick()
                        time.sleep(0.2)
                else:
                    # print(thumb,indexfinger,pinkyfinger)
                    if  thumb>indexfinger:    
                        pass
                    else:
                        if int(time.time()-intialtime) < 1 :
                            pyautogui.doubleClick()
                            intialtime = time.time()
                        else:
                            print("click")
                            pyautogui.click()
                            intialtime = time.time()
                pyautogui.moveTo(screen_width*l[8].x,screen_height*l[8].y)
            elif switchapps(l,h):
                # print("switchapp condition")
                if switchappmenu:
                    if intial is None:
                        intial = (int(l[8].x*w),int(l[8].y*h))
                    distance = sqrt(pow(l[8].x*w - intial[0],2)+pow(l[8].y*h-intial[1],2))
                    if abs(intial[1] - int(l[8].y*h)) < h/8 and distance >= w/8:
                        if intial[0] > int(l[8].x*w):
                            pyautogui.press('left')
                            intial = (int(l[8].x*w),int(l[8].y*h))
                        elif intial[0] < int(l[8].x*w):
                            pyautogui.press('right')
                            intial =  (int(l[8].x*w),int(l[8].y*h))
                    elif not (thumb>indexfinger ):
                            pyautogui.keyUp('alt')
                            switchappmenu = False
                            intial = (int(l[8].x*w),int(l[8].y*h))
                            time.sleep(1)    
                    else:
                        pass
                else:
                    pyautogui.keyDown('alt')
                    pyautogui.press('tab')
                    switchappmenu = True
            else:
                # print("not mouse ")
                switchappmenu = False
                if intial is None:
                    intial = (int(l[8].x*w),int(l[8].y*h))
                distance = sqrt(pow(l[8].x*w - intial[0],2)+pow(l[8].y*h-intial[1],2))
                if distance>=w/2 and abs(intial[1] - int(l[8].y*h)) < h/8:
                    print("distance : ",distance)
                    if intial[0]>int(l[8].x*w):
                        print("swaping left")
                        # swipe_right()
                    if intial[0]<int(l[8].x*w):
                        print("swaping right")
                        # swipe_right()
                elif distance >=h/4 and abs(intial[0] - int(l[8].x*w)) < w/8:
                    print("distance: - ",distance)
                    if intial[1]>int(l[8].y*h):
                        print("swip up")
                        pyautogui.hotkey('win','shift','m')
                        # swipe_right()
                    if intial[1]<int(l[8].y*h):
                        print("swaping down")
                        pyautogui.hotkey('win','m')
                        # swipe_right()
                cv2.line(image,intial,(int(l[8].x*w),int(l[8].y*h)),(255,0,245),10)
                intial = (int(l[8].x*w),int(l[8].y*h))
                
            mp_drawing.draw_landmarks(
                image,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_drawing_styles.get_default_hand_landmarks_style(),
                mp_drawing_styles.get_default_hand_connections_style())



hands = mp_hands.Hands(
    model_complexity=1,
    min_detection_confidence=0.95,
    min_tracking_confidence=0.8)

# im = cv2.imread("image.jpeg")
# image,result = mediapipe_detection(im,hands)
# draw_styled_landmarks(image,result)
# cv2.imshow("image",image)
# cv2.waitKey(0)

webcam = cv2.VideoCapture(0)
while True:
    _,frame = webcam.read()
    frame = cv2.flip(frame,1)
    frame,results = mediapipe_detection(frame,hands)
    draw_styled_landmarks(frame,results)
    cv2.imshow("hath",frame)
    cv2.waitKey(27)
    
