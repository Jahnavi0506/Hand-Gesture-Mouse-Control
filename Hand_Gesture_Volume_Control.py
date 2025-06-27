import cv2 as cv
import mediapipe as mp
import pyautogui

cam=cv.VideoCapture(0)
myhands=mp.solutions.hands
drawing_utils=mp.solutions.drawing_utils

x1=y1=x2=y2=0

screen_width,screen_height=pyautogui.size()

while True:
    success,img=cam.read()
    img=cv.flip(img,1)
    rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
    output=myhands.Hands().process(rgb)
    hands=output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(img,hand,myhands.HAND_CONNECTIONS)
            one_hand_landmarks=hand.landmark
            for Id,lm in enumerate(one_hand_landmarks):
                h,w,c=img.shape
                X=int(lm.x*w)
                Y=int(lm.y*h)
                #print(Id,X,Y)
                if Id==8:
                    mouse_x=int(screen_width*(X/w))
                    mouse_y=int(screen_height*(Y/h))
                    cv.circle(img,(X,Y),10,(255,0,255),-1,cv.FILLED)
                    x1=X
                    y1=Y
                    pyautogui.moveTo(mouse_x, mouse_y)

                if Id==4:
                    cv.circle(img,(X,Y),10,(255,255,0),-1,cv.FILLED)
                    x2=X
                    y2=Y
        #distance=((x2-x1)**2+(y2-y1)**2)**0.5
        distance=y2-y1   
        print(distance)
        if distance<30:
            pyautogui.click()
            cv.putText(img,"Clicking",(50,50),cv.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    cv.imshow("Hand Gesture Mouse Control", img)
    key=cv.waitKey(100) & 0xFF
    if key == ord('s'):
        break
cam.release()
cv.destroyAllWindows()

