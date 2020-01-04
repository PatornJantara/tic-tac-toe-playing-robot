# import module
# to install open command prompt and then type tis command "-pip install (module name)" example : -pip install numpy
# close serial monitor in arduino

#-------------------------------------------------------------------------------------------------

import numpy as np  # for working on array
import cv2          # (OpenCV) for image processing
import time         
import serial       # for sending Serial command to arduino
import random       # for random pattern

#-------------------------------------------------------------------------------------------------

arduino=serial.Serial('com9',9600)  # to select port com arduino and buard rate

cap = cv2.VideoCapture(1)  # open camera // cv2.VideoCapture(X) , X = 0,1,2,.

set_time = 30  # count = set_time then capture

# Game parameter

count_1 = 0  # has blue ball in area count + 1
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0

red_1 = 0  # computer place red = 1
red_2 = 0
red_3 = 0
red_4 = 0
red_5 = 0
red_6 = 0
red_7 = 0
red_8 = 0
red_9 = 0

blue_1 = 0 # player place blue = 1
blue_2 = 0
blue_3 = 0
blue_4 = 0
blue_5 = 0
blue_6 = 0
blue_7 = 0
blue_8 = 0
blue_9 = 0

winner = 0 

# define ROI (region of interest) coordinate in rectangular

upper_left_1 = (150, 40)     
bottom_right_1 = (240, 130) 
upper_left_2 = (150, 190)   
bottom_right_2 = (240, 280)  
upper_left_3 = (150, 330)
bottom_right_3 = (240, 420) 
upper_left_4 = (300, 40)
bottom_right_4 = (380, 130)  
upper_left_5 = (300, 190)
bottom_right_5 = (380, 280) 
upper_left_6 = (300, 330)
bottom_right_6 = (380, 420)
upper_left_7 = (440, 40)
bottom_right_7 = (520, 130)  
upper_left_8 = (440, 190)
bottom_right_8 = (520, 280)
upper_left_9 = (440, 330)
bottom_right_9 = (520, 420) 

#---------------------------------------------------------------------------------------------------

while(True):

    # Capture frame by frame
    ret, frame = cap.read()  # main frame
    
#----------------------------------------------------------------------------------------------------   
    # Draw and crop ROI 
    r1 = cv2.rectangle(frame, upper_left_1, bottom_right_1, (0, 255, 0), 2)   # Draw rectangle in main image
    area_detect_1 = frame[upper_left_1[1] : bottom_right_1[1], upper_left_1[0] : bottom_right_1[0]]  # crop ROI from coordinate
    r2 = cv2.rectangle(frame, upper_left_2, bottom_right_2, (0, 255, 0), 2)
    area_detect_2 = frame[upper_left_2[1] : bottom_right_2[1], upper_left_2[0] : bottom_right_2[0]]
    r3 = cv2.rectangle(frame, upper_left_3, bottom_right_3, (0, 255, 0), 2)
    area_detect_3 = frame[upper_left_3[1] : bottom_right_3[1], upper_left_3[0] : bottom_right_3[0]]
    r4 = cv2.rectangle(frame, upper_left_4, bottom_right_4, (0, 255, 0), 2)
    area_detect_4 = frame[upper_left_4[1] : bottom_right_4[1], upper_left_4[0] : bottom_right_4[0]]
    r5 = cv2.rectangle(frame, upper_left_5, bottom_right_5, (0, 255, 0), 2)
    area_detect_5 = frame[upper_left_5[1] : bottom_right_5[1], upper_left_5[0] : bottom_right_5[0]]
    r6 = cv2.rectangle(frame, upper_left_6, bottom_right_6, (0, 255, 0), 2)
    area_detect_6 = frame[upper_left_6[1] : bottom_right_6[1], upper_left_6[0] : bottom_right_6[0]]
    r7 = cv2.rectangle(frame, upper_left_7, bottom_right_7, (0, 255, 0), 2)
    area_detect_7= frame[upper_left_7[1] : bottom_right_7[1], upper_left_7[0] : bottom_right_7[0]]
    r8 = cv2.rectangle(frame, upper_left_8, bottom_right_8, (0, 255, 0), 2)
    area_detect_8 = frame[upper_left_8[1] : bottom_right_8[1], upper_left_8[0] : bottom_right_8[0]]
    r9 = cv2.rectangle(frame, upper_left_9, bottom_right_9, (0, 255, 0), 2)
    area_detect_9 = frame[upper_left_9[1] : bottom_right_9[1], upper_left_9[0] : bottom_right_9[0]]

#----------------------------------------------------------------------------
    
    # create text in image frame
    
    cv2.line(frame,(0,0),(0,480),(0,0,0),250)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'R',(30,60), font,2,(0,200,0),2,cv2.LINE_AA)
    cv2.putText(frame,'O',(30,110), font,2,(0,200,0),2,cv2.LINE_AA)
    cv2.putText(frame,'B',(30,160), font,2,(0,200,0),2,cv2.LINE_AA)
    cv2.putText(frame,'O',(30,210), font,2,(0,200,0),2,cv2.LINE_AA)
    cv2.putText(frame,'T',(38,260), font,2,(0,200,0),2,cv2.LINE_AA)
    cv2.putText(frame,'A',(38,330), font,2,(0,200,0),2,cv2.LINE_AA)
    cv2.putText(frame,'R',(38,380), font,2,(0,200,0),2,cv2.LINE_AA)
    cv2.putText(frame,'M',(38,430), font,2,(0,200,0),2,cv2.LINE_AA)
    
    cv2.putText(area_detect_1,'(1)',(0,15), font,0.5,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(area_detect_2,'(2)',(0,15), font,0.5,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(area_detect_3,'(3)',(0,15), font,0.5,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(area_detect_4,'(4)',(0,15), font,0.5,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(area_detect_5,'(5)',(0,15), font,0.5,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(area_detect_6,'(6)',(0,15), font,0.5,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(area_detect_7,'(7)',(0,15), font,0.5,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(area_detect_8,'(8)',(0,15), font,0.5,(0,255,0),1,cv2.LINE_AA)
    cv2.putText(area_detect_9,'(9)',(0,15), font,0.5,(0,255,0),1,cv2.LINE_AA)
#--------------------------------------------------------------------------------------------------
    
    # create sub image from selected ROI
    cv2.imwrite('1.png', area_detect_1)
    cv2.imwrite('2.png', area_detect_2)
    cv2.imwrite('3.png', area_detect_3)
    cv2.imwrite('4.png', area_detect_4)
    cv2.imwrite('5.png', area_detect_5)
    cv2.imwrite('6.png', area_detect_6)
    cv2.imwrite('7.png', area_detect_7)
    cv2.imwrite('8.png', area_detect_8)
    cv2.imwrite('9.png', area_detect_9)

#----------------------------------------------------------------------------------------------------
    # read sub image
    pic_1 = cv2.imread('1.png')
    pic_2 = cv2.imread('2.png')
    pic_3 = cv2.imread('3.png')
    pic_4 = cv2.imread('4.png')
    pic_5 = cv2.imread('5.png')
    pic_6 = cv2.imread('6.png')
    pic_7 = cv2.imread('7.png')
    pic_8 = cv2.imread('8.png')
    pic_9 = cv2.imread('9.png')
    
#----------------------------------------------------------------------------------------------------

    # read in grayscale image for Hough method
    pic_1_gray = cv2.imread('1.png',0)
    pic_2_gray = cv2.imread('2.png',0)
    pic_3_gray = cv2.imread('3.png',0)
    pic_4_gray = cv2.imread('4.png',0)
    pic_5_gray = cv2.imread('5.png',0)
    pic_6_gray = cv2.imread('6.png',0)
    pic_7_gray = cv2.imread('7.png',0)
    pic_8_gray = cv2.imread('8.png',0)
    pic_9_gray = cv2.imread('9.png',0)

#----------------------------------------------------------------------------------------------------    
    # Read average BGR ( summation BGR of all pixel in picture )
    # resize picture to 1 pixel to consider (BGR element)
    
    #1       
    color_1 = np.average(pic_1, axis=0)     
    avg_1 = np.average(color_1, axis=0)    

    #2
    color_2 = np.average(pic_2, axis=0)
    avg_2 = np.average(color_2, axis=0)

    #3
    color_3 = np.average(pic_3, axis=0)
    avg_3 = np.average(color_3, axis=0)

    #4
    color_4 = np.average(pic_4, axis=0)
    avg_4 = np.average(color_4, axis=0)

    #5
    color_5 = np.average(pic_5, axis=0)
    avg_5 = np.average(color_5, axis=0)

    #6
    color_6 = np.average(pic_6, axis=0)
    avg_6 = np.average(color_6, axis=0)

    #7
    color_7 = np.average(pic_7, axis=0)
    avg_7 = np.average(color_7, axis=0)

    #8
    color_8 = np.average(pic_8, axis=0)
    avg_8 = np.average(color_8, axis=0)

    #9
    color_9 = np.average(pic_9, axis=0)
    avg_9 = np.average(color_9, axis=0)

#--------------------------------------------------------------------------------------------------

# apply canny edge for obviouse object shape

    canny_1 = cv2.Canny(pic_1_gray,100,180)
    canny_2 = cv2.Canny(pic_2_gray,100,180)
    canny_3 = cv2.Canny(pic_3_gray,100,180)
    canny_4 = cv2.Canny(pic_4_gray,100,180)
    canny_5 = cv2.Canny(pic_5_gray,100,180)
    canny_6 = cv2.Canny(pic_6_gray,100,180)
    canny_7 = cv2.Canny(pic_7_gray,100,180)
    canny_8 = cv2.Canny(pic_8_gray,100,180)
    canny_9 = cv2.Canny(pic_9_gray,100,180)

#--------------------------------------------------------------------------------------------------

# apply Hough transform  for find circle
# thus function will return location and dimension if found circle and return None if not found

    circle_1 = cv2.HoughCircles(canny_1,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)  
    circle_2 = cv2.HoughCircles(canny_2,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)
    circle_3 = cv2.HoughCircles(canny_3,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)
    circle_4 = cv2.HoughCircles(canny_4,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)
    circle_5 = cv2.HoughCircles(canny_5,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)
    circle_6 = cv2.HoughCircles(canny_6,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)
    circle_7 = cv2.HoughCircles(canny_7,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)
    circle_8 = cv2.HoughCircles(canny_8,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)
    circle_9 = cv2.HoughCircles(canny_9,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=20,maxRadius=100)

#--------------------------------------------------------------------------------------------------    
    # Create a Board game display
    board_img = np.zeros((480,300,3), np.uint8)
    board_img.fill(255)
    cv2.line(board_img,(0,0),(299,0),(0,0,0),5)
    cv2.line(board_img,(99,0),(99,300),(0,0,0),5)
    cv2.line(board_img,(199,0),(199,300),(0,0,0),5)
    cv2.line(board_img,(0,99),(300,99),(0,0,0),5)
    cv2.line(board_img,(0,199),(300,199),(0,0,0),5)
    cv2.line(board_img,(0,299),(300,299),(0,0,0),5) 
#---------------------------------------------------------------------------------------------------

    
    contrast = 50  #  blue index - red index  
    
    # ROI 1
    if ((avg_1[0]-avg_1[2] >= contrast and circle_1 is not None) or blue_1 == 1 ):
        cv2.circle(board_img,(50,50), 20, (255,0,0), -1)
        count_1=count_1+1
    if ((avg_1[2]-avg_1[0] >= contrast and circle_1 is not None) or red_1 == 1):
        cv2.circle(board_img,(50,50), 20, (0,0,255), -1)
    # ROI 2
    if ((avg_2[0]-avg_2[2] >= contrast and circle_2 is not None)or blue_2 == 1):
        cv2.circle(board_img,(50,150), 20, (255,0,0), -1)
        count_2=count_2+1
    if ((avg_2[2]-avg_2[0] >= contrast and circle_2 is not None)or red_2 == 1):
        cv2.circle(board_img,(50,150), 20, (0,0,255), -1)
    
    # ROI 3
    if ((avg_3[0]-avg_3[2] >= contrast and circle_3 is not None) or blue_3 == 1 ):
        cv2.circle(board_img,(50,250), 20, (255,0,0), -1)
        count_3=count_3+1
    if ((avg_3[2]-avg_3[0] >= contrast and circle_3 is not None) or red_3 == 1):
        cv2.circle(board_img,(50,250), 20, (0,0,255), -1)
        
    # ROI 4
    if ((avg_4[0]-avg_4[2] >= contrast and circle_4 is not None) or blue_4 == 1):
        cv2.circle(board_img,(150,50), 20, (255,0,0), -1)
        count_4=count_4+1
    if ((avg_4[2]-avg_4[0] >= contrast and circle_4 is not None) or red_4 == 1):
        cv2.circle(board_img,(150,50), 20, (0,0,255), -1)
    # ROI 5
    if ((avg_5[0]-avg_5[2] >= contrast and circle_5 is not None) or blue_5 == 1 ):
        cv2.circle(board_img,(150,150), 20, (255,0,0), -1)
        count_5=count_5+1
    if ((avg_5[2]-avg_5[0] >= contrast and circle_5 is not None) or red_5 == 1 ):
        cv2.circle(board_img,(150,150), 20, (0,0,255), -1)
    # ROI 6
    if ((avg_6[0]-avg_6[2] >= contrast and circle_6 is not None) or blue_6 == 1 ):
        cv2.circle(board_img,(150,250), 20, (255,0,0), -1)
        count_6=count_6+1
    if ((avg_6[2]-avg_6[0] >= contrast and circle_6 is not None) or red_6 == 1 ):
        cv2.circle(board_img,(150,250), 20, (0,0,255), -1)

    # ROI 7
    if ((avg_7[0]-avg_7[2] >= contrast and circle_7 is not None) or blue_7 == 1 ):
        cv2.circle(board_img,(250,50), 20, (255,0,0), -1)
        count_7=count_7+1
    if ((avg_7[2]-avg_7[0] >= contrast and circle_7 is not None) or red_7 == 1 ):
        cv2.circle(board_img,(250,50), 20, (0,0,255), -1)
    # ROI 8
    if ((avg_8[0]-avg_8[2] >= contrast and circle_8 is not None) or blue_8 == 1):
        cv2.circle(board_img,(250,150), 20, (255,0,0), -1)
        count_8=count_8+1
    if ((avg_8[2]-avg_8[0] >= contrast and circle_8 is not None) or red_8 == 1):
        cv2.circle(board_img,(250,150), 20, (0,0,255), -1)

    # ROI 9
    if ((avg_9[0]-avg_9[2] >= contrast and circle_9 is not None) or blue_9 == 1):
        cv2.circle(board_img,(250,250), 20, (255,0,0), -1)
        count_9=count_9+1
    if ((avg_9[2]-avg_9[0] >= contrast and circle_9 is not None) or red_9 == 1):
        cv2.circle(board_img,(250,250), 20, (0,0,255), -1)
#-----------------------------------------------------------------------------------------------------
 # Exit Key  
    k = cv2.waitKey(1)

    if  k%256 == 27:
        arduino.write(b'0')
        time.sleep(1)
        # Q pressed to exit
        break

#-----------------------------------------------------------------------------------------------------       

    # limit count
    if (count_1 >= 35):
        count_1 = 35
    if (count_2 >= 35):
        count_2 = 35
    if (count_3 >= 35):
        count_3 = 35
    if (count_4 >= 35):
        count_4 = 35
    if (count_5 >= 35):
        count_5 = 35
    if (count_6 >= 35):
        count_6 = 35
    if (count_7 >= 35):
        count_7 = 35
    if (count_8 >= 35):
        count_8 = 35    
    if (count_9 >= 35):
        count_9 = 35    


#----------------------------------------------------------------------------------------------------
    # main frame and game window
    
    game = np.hstack((frame,board_img))    # camera & virtual game display
    cv2.imshow('Tic Tac Toe',game)         # show game window

#---------------------------------------------------------------------------------------------------

# trig
    
    if (count_1 == set_time or count_2 == set_time or count_3 == set_time
        or count_4 == set_time or count_5 == set_time or count_6 == set_time
        or count_7 == set_time or count_8 == set_time or count_9 == set_time ):  # when counter is trigged start below operation
        
#---------------------------------------------------------------------------------------------------

# cap sub image        
        cv2.imwrite('cap_1.png', area_detect_1)
        cv2.imwrite('cap_2.png', area_detect_2)
        cv2.imwrite('cap_3.png', area_detect_3)
        cv2.imwrite('cap_4.png', area_detect_4)
        cv2.imwrite('cap_5.png', area_detect_5)
        cv2.imwrite('cap_6.png', area_detect_6)
        cv2.imwrite('cap_7.png', area_detect_7)
        cv2.imwrite('cap_8.png', area_detect_8)
        cv2.imwrite('cap_9.png', area_detect_9)
#----------------------------------------------------------------------------------------------------

# read average RGB of sub image

        #1_cap
        pic_1_cap = cv2.imread('cap_1.png')
        color_1_cap = np.average(pic_1_cap, axis=0)
        avg_1_cap = np.average(color_1_cap, axis=0)

        #2_cap
        pic_2_cap = cv2.imread('cap_2.png')
        color_2_cap = np.average(pic_2_cap, axis=0)
        avg_2_cap = np.average(color_2_cap, axis=0)

        #3_cap
        pic_3_cap = cv2.imread('cap_3.png')
        color_3_cap = np.average(pic_3_cap, axis=0)
        avg_3_cap = np.average(color_3_cap, axis=0)

        #4_cap
        pic_4_cap = cv2.imread('cap_4.png')
        color_4_cap = np.average(pic_4_cap, axis=0)
        avg_4_cap = np.average(color_4_cap, axis=0)

        #5_cap
        pic_5_cap = cv2.imread('cap_5.png')
        color_5_cap = np.average(pic_5_cap, axis=0)
        avg_5_cap = np.average(color_5_cap, axis=0)

        #6_cap
        pic_6_cap = cv2.imread('cap_6.png')
        color_6_cap = np.average(pic_6_cap, axis=0)
        avg_6_cap = np.average(color_6_cap, axis=0)

        #7_cap
        pic_7_cap = cv2.imread('cap_7.png')
        color_7_cap = np.average(pic_7_cap, axis=0)
        avg_7_cap = np.average(color_7_cap, axis=0)

        #8_cap
        pic_8_cap = cv2.imread('cap_8.png')
        color_8_cap = np.average(pic_8_cap, axis=0)
        avg_8_cap = np.average(color_8_cap, axis=0)

        #9_cap
        pic_9_cap = cv2.imread('cap_9.png')
        color_9_cap = np.average(pic_9_cap, axis=0)
        avg_9_cap = np.average(color_9_cap, axis=0) 
#-------------------------------------------------------------------------------------------------

        # create game array
        
        board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

        board_1=board[0][0]  # for ROI 1
        board_2=board[1][0] 
        board_3=board[2][0]
        board_4=board[0][1]
        board_5=board[1][1]
        board_6=board[2][1]
        board_7=board[0][2]
        board_8=board[1][2] 
        board_9=board[2][2]  # for ROI 9
        
#--------------------------------------------------------------------------------------------------

        # define game piece

        # ROI 1
        if (avg_1_cap[0]-avg_1_cap[2] >= contrast):
            board_1='B'
            blue_1 = 1
        if (avg_1_cap[2]-avg_1_cap[0] >= contrast):
            board_1='R'
            red_1 = 1
        # ROI 2
        if (avg_2_cap[0]-avg_2_cap[2] >= contrast):
            board_2='B'
            blue_2 = 1
        if (avg_2_cap[2]-avg_2_cap[0] >= contrast):
            board_2='R'
            red_2 = 1
        # ROI 3
        if (avg_3_cap[0]-avg_3_cap[2] >= contrast):
            board_3='B'
            blue_3 = 1
        if (avg_3_cap[2]-avg_3_cap[0] >= contrast):
            board_3='R'
            red_3 = 1
        # ROI 4
        if (avg_4_cap[0]-avg_4_cap[2] >= contrast):
            board_4='B'
            blue_4 = 1
        if (avg_4_cap[2]-avg_4_cap[0] >= contrast):
            board_4='R'
            red_4 = 1
        # ROI 5
        if (avg_5_cap[0]-avg_5_cap[2] >= contrast):
            board_5='B'
            blue_5 = 1
        if (avg_5_cap[2]-avg_5_cap[0] >= contrast):
            board_5='R'
            red_5 = 1
        # ROI 6
        if (avg_6_cap[0]-avg_6_cap[2] >= contrast):
            board_6='B'
            blue_6 = 1
        if (avg_6_cap[2]-avg_6_cap[0] >= contrast):
            board_6='R'
            red_6 = 1
        # ROI 7
        if (avg_7_cap[0]-avg_7_cap[2] >= contrast):
            board_7='B'
            blue_7 = 1
        if (avg_7_cap[2]-avg_7_cap[0] >= contrast):
            board_7='R'
            red_7 = 1
        # ROI 8
        if (avg_8_cap[0]-avg_8_cap[2] >= contrast):
            board_8='B'
            blue_8 = 1
        if (avg_8_cap[2]-avg_8_cap[0] >= contrast):
            board_8='R'
            red_8 = 1
        # ROI 9
        if (avg_9_cap[0]-avg_9_cap[2] >= contrast):
            board_9='B'
            blue_9 = 1
        if (avg_9_cap[2]-avg_9_cap[0] >= contrast):
            board_9='R'
            red_9 = 1
#--------------------------------------------------------------------------------------------------

        # input game array

        print ('Game input')
        print (board_1, '|', board_4, '|', board_7)
        print ('----------')
        print (board_2, '|', board_5, '|', board_8)
        print ('----------')
        print (board_3, '|', board_6, '|', board_9)
        print ('          ')

#--------------------------------------------------------------------------------------------------        
        # Check winner ?

        # Plaeyer wins
        if ((board_1=='B'and board_2=='B'and board_3=='B')
            or (board_4=='B'and board_5=='B'and board_6=='B')
            or (board_7=='B'and board_8=='B'and board_9=='B')
            or (board_1=='B'and board_4=='B'and board_7=='B')
            or (board_2=='B'and board_5=='B'and board_8=='B')
            or (board_3=='B'and board_6=='B'and board_9=='B')
            or (board_1=='B'and board_5=='B'and board_9=='B')
            or (board_3=='B'and board_5=='B'and board_7=='B')):
            winner = 1
            print('Player Win')
            print(' ')
            
#-----------------------------------------------------------------------------------------------------
        # Draw
        if ( board_1 !=' 'and board_2 !=' 'and board_3 !=' '
             and board_4 !=' 'and board_5 !=' 'and board_6 !=' '
             and board_7 !=' 'and board_8 !=' 'and board_9 !=' ' and winner !=1):
            winner = 3
            print('Draw')
            print(' ')
#------------------------------------------------------------------------------------------------------
        
#------------------------------------------------------------------------------------------------------
        # Game Algorithm
        choose = [1,2,3,4,5,6,7,8,9]  # choice for random
#------------------------------------------------------------------------------------------------------

        # win choice  
 
        # R1
        
        if ( board_1 == 'R' and board_2 == 'R' and board_3 == ' ' and winner == 0):
            arduino.write(b'3')       # send serial = 3 to arduino
            print('computer choose : 3')
            board_3 = 'R'             # make board 3 = red piece
            red_3 = 1
        elif ( board_1 == 'R' and board_2 == ' ' and board_3 == 'R' and winner == 0):
            arduino.write(b'2')
            print('computer choose : 2')
            board_2 = 'R'
            red_2 = 1
        elif ( board_1 == 'R' and board_4 == 'R' and board_7 == ' ' and winner == 0):
            arduino.write(b'7')
            print('computer choose : 7')
            board_7 = 'R'
            red_7 = 1
        elif ( board_1 == 'R' and board_5 == 'R' and board_9 == ' ' and winner == 0):
            arduino.write(b'9')
            print('computer choose : 9')
            board_9 = 'R'
            red_9 = 1
        elif ( board_1 == 'R' and board_7 == 'R' and board_4 == ' ' and winner == 0):
            arduino.write(b'4')
            print('computer choose : 4')
            board_4 = 'R'
            red_4 = 1
        elif ( board_1 == 'R' and board_9 == 'R' and board_5 == ' ' and winner == 0):
            arduino.write(b'5')
            print('computer choose : 5')
            board_5 = 'R'
            red_5 = 1
#------------------------------------------------------------------------------------------------------
                
        # R2

        elif ( board_2 == 'R' and board_3 == 'R' and board_1 == ' ' and winner == 0):
            arduino.write(b'1')
            print('computer choose : 1')
            board_1 = 'R'
            red_1 = 1
        elif ( board_2 == 'R' and board_5 == 'R' and board_8 == ' ' and winner == 0):
            arduino.write(b'8')
            print('computer choose : 8')
            board_8 = 'R'
            red_8 = 1
        elif ( board_2 == 'R' and board_8 == 'R' and board_5 == ' ' and winner == 0):
            arduino.write(b'5')
            print('computer choose : 5')
            board_5 = 'R'
            red_5 = 1
#------------------------------------------------------------------------------------------------------

        # R3
        
        elif ( board_3 == 'R' and board_5 == 'R' and board_7 == ' ' and winner == 0):
            arduino.write(b'7')
            print('computer choose : 7')
            board_7 = 'R'
            red_7 = 1
        elif ( board_3 == 'R' and board_6 == 'R' and board_9 == ' ' and winner == 0):
            arduino.write(b'9')
            print('computer choose : 9')
            board_9 = 'R'
            red_9 = 1
        elif ( board_3 == 'R' and board_9 == 'R' and board_6 == ' ' and winner == 0):
            arduino.write(b'6')
            print('computer choose : 6')
            board_6 = 'R'
            red_6 = 1
#------------------------------------------------------------------------------------------------------

        # R4
        elif ( board_4 == 'R' and board_5 == 'R' and board_6 == ' ' and winner == 0):
            arduino.write(b'6')
            print('computer choose : 6')
            board_6 = 'R'
            red_6 = 1
        elif ( board_4 == 'R' and board_6 == 'R' and board_5 == ' ' and winner == 0):
            arduino.write(b'5')
            print('computer choose : 5')
            board_5 = 'R'
            red_5 = 1
        elif ( board_4 == 'R' and board_7 == 'R' and board_1 == ' ' and winner == 0):
            arduino.write(b'1')
            print('computer choose : 1')
            board_1 = 'R'
            red_1 = 1
#------------------------------------------------------------------------------------------------------

        # R5
        elif ( board_5 == 'R' and board_6 == 'R' and board_4 == ' ' and winner == 0):
            arduino.write(b'4')
            print('computer choose : 4')
            board_4 = 'R'
            red_4 = 1
        elif ( board_5 == 'R' and board_7 == 'R' and board_3 == ' ' and winner == 0):
            arduino.write(b'3')
            print('computer choose : 3')
            board_3 = 'R'
            red_3 = 1
        elif ( board_5 == 'R' and board_8 == 'R' and board_2 == ' ' and winner == 0):
            arduino.write(b'2')
            print('computer choose : 2')
            board_2 = 'R'
            red_2 = 1
        elif ( board_5 == 'R' and board_9 == 'R' and board_1 == ' ' and winner == 0):
            arduino.write(b'1')
            print('computer choose : 1')
            board_1 = 'R'
            red_1 = 1
#------------------------------------------------------------------------------------------------------

        # R6
        elif ( board_6 == 'R' and board_9 == 'R' and board_3 == ' ' and winner == 0):
            arduino.write(b'3')
            print('computer choose : 3')
            board_3 = 'R'
            red_3 = 1
#------------------------------------------------------------------------------------------------------

        # R7
        elif ( board_7 == 'R' and board_8 == 'R' and board_9 == ' ' and winner == 0):
            arduino.write(b'9')
            print('computer choose : 9')
            board_9 = 'R'
            red_9 =1
        elif ( board_7 == 'R' and board_9 == 'R' and board_8 == ' ' and winner == 0):
            arduino.write(b'8')
            print('computer choose : 8')
            board_8 = 'R'
            red_8 =1
#------------------------------------------------------------------------------------------------------
            
        # R8
        elif ( board_8 == 'R' and board_9 == 'R' and board_7 == ' ' and winner == 0):
            arduino.write(b'7')
            print('computer choose : 7')
            board_7 = 'R'
            red_7 = 1
#------------------------------------------------------------------------------------------------------
        # defense choice

        # B1
        
        elif ( board_1 == 'B' and board_2 == 'B' and board_3 == ' ' and winner == 0):
            arduino.write(b'3')
            print('computer choose : 3')
            board_3 = 'R'
            red_3 =1
        elif ( board_1 == 'B' and board_3 == 'B' and board_2 == ' ' and winner == 0):
            arduino.write(b'2')
            print('computer choose : 2')
            board_2 = 'R'
            red_2 =1
        elif ( board_1 == 'B' and board_4 == 'B' and board_7 == ' ' and winner == 0):
            arduino.write(b'7')
            print('computer choose : 7')
            board_7 = 'R'
            red_7 =1
        elif ( board_1 == 'B' and board_5 == 'B' and board_9 == ' ' and winner == 0):
            arduino.write(b'9')
            print('computer choose : 9')
            board_9 = 'R'
            red_9 =1
        elif ( board_1 == 'B' and board_7 == 'B' and board_4 == ' ' and winner == 0):
            arduino.write(b'4')
            print('computer choose : 4')
            board_4 = 'R'
            red_4 =1
        elif ( board_1 == 'B' and board_9 == 'B' and board_5 == ' ' and winner == 0):
            arduino.write(b'5')
            print('computer choose : 5')
            board_5 = 'R'
            red_5 = 1
#------------------------------------------------------------------------------------------------------
                
        # B2

        elif ( board_2 == 'B' and board_3 == 'B' and board_1 == ' ' and winner == 0):
            arduino.write(b'1')
            print('computer choose : 1')
            board_1 = 'R'
            red_1 =1
        elif ( board_2 == 'B' and board_5 == 'B' and board_8 == ' ' and winner == 0):
            arduino.write(b'8')
            print('computer choose : 8')
            board_8 = 'R'
            red_8 =1
        elif ( board_2 == 'B' and board_8 == 'B' and board_5 == ' ' and winner == 0):
            arduino.write(b'5')
            print('computer choose : 5')
            board_5 = 'R'
            red_5 =1
#------------------------------------------------------------------------------------------------------

        # B3
        
        elif ( board_3 == 'B' and board_5 == 'B' and board_7 == ' ' and winner == 0):
            arduino.write(b'7')
            print('computer choose : 7')
            board_7 = 'R'
            red_7 =1
        elif ( board_3 == 'B' and board_6 == 'B' and board_9 == ' ' and winner == 0):
            arduino.write(b'9')
            print('computer choose : 9')
            board_9 = 'R'
            red_9 =1
        elif ( board_3 == 'B' and board_7 == 'B' and board_5 == ' ' and winner == 0):
            arduino.write(b'5')
            print('computer choose : 5')
            board_5 = 'R'
            red_5 =1
        elif ( board_3 == 'B' and board_9 == 'B' and board_6 == ' ' and winner == 0):
            arduino.write(b'6')
            print('computer choose : 6')
            board_6 = 'R'
            red_6 =1
#------------------------------------------------------------------------------------------------------

        # B4
        elif ( board_4 == 'B' and board_5 == 'B' and board_6 == ' ' and winner == 0):
            arduino.write(b'6')
            print('computer choose : 6')
            board_6 = 'R'
            red_6 =1
        elif ( board_4 == 'B' and board_6 == 'B' and board_5 == ' ' and winner == 0):
            arduino.write(b'5')
            print('computer choose : 5')
            board_5 = 'R'
            red_5 =1
        elif ( board_4 == 'B' and board_7 == 'B' and board_1 == ' ' and winner == 0):
            arduino.write(b'1')
            print('computer choose : 1')
            board_1 = 'R'
            red_1 =1
#------------------------------------------------------------------------------------------------------

        # B5
        elif ( board_5 == 'B' and board_6 == 'B' and board_4 == ' ' and winner == 0):
            arduino.write(b'4')
            print('computer choose : 4')
            board_4 = 'R'
            red_4 =1
        elif ( board_5 == 'B' and board_7 == 'B' and board_3 == ' ' and winner == 0):
            arduino.write(b'3')
            print('computer choose : 3')
            board_3 = 'R'
            red_3 =1
        elif ( board_5 == 'B' and board_8 == 'B' and board_2 == ' ' and winner == 0):
            arduino.write(b'2')
            print('computer choose : 2')
            board_2 = 'R'
            red_2 =1
        elif ( board_5 == 'B' and board_9 == 'B' and board_1 == ' ' and winner == 0):
            arduino.write(b'1')
            print('computer choose : 1')
            board_1 = 'R'
            red_1 =1
#------------------------------------------------------------------------------------------------------

        # B6
        elif ( board_6 == 'B' and board_9 == 'B' and board_3 == ' ' and winner == 0):
            arduino.write(b'3')
            print('computer choose : 3')
            board_3 = 'R'
            red_3 =1

        # B7
        elif ( board_7 == 'B' and board_8 == 'B' and board_9 == ' ' and winner == 0):
            arduino.write(b'9')
            print('computer choose : 9')
            board_9 = 'R'
            red_9 =1
        elif ( board_7 == 'B' and board_9 == 'B' and board_8 == ' ' and winner == 0):
            arduino.write(b'8')
            print('computer choose : 8')
            board_8 = 'R'
            red_8 =1
#------------------------------------------------------------------------------------------------------
            
        # B8
        elif ( board_8 == 'B' and board_9 == 'B' and board_7 == ' ' and winner == 0):
            arduino.write(b'7')
            print('computer choose : 7')
            board_7 = 'R'
            red_7 =1
#------------------------------------------------------------------------------------------------------

        # Random choice    
        else :
            if (board_1 ==' ' or board_2 ==' ' or board_3 ==' ' or
                board_4 ==' ' or board_5 ==' ' or board_6 ==' ' or
                board_7 ==' ' or board_8 ==' ' or board_9 ==' ' and winner == 0):

         # remove choice where already has piece
     
                if (board_1 == 'B' or board_1 == 'R'):
                    choose.remove(1) 
                if (board_2 == 'B' or board_2 == 'R'):
                    choose.remove(2)    
                if (board_3 == 'B' or board_3 == 'R'):
                    choose.remove(3)
                if (board_4 == 'B' or board_4 == 'R'):
                    choose.remove(4)
                if (board_5 == 'B' or board_5 == 'R'):
                    choose.remove(5)
                if (board_6 == 'B' or board_6 == 'R'):
                    choose.remove(6)
                if (board_7 == 'B' or board_7 == 'R'):
                    choose.remove(7)
                if (board_8 == 'B' or board_8 == 'R'):
                    choose.remove(8)
                if (board_9 == 'B' or board_9 == 'R'):
                    choose.remove(9)
    #------------------------------------------------------------------------------------------------------
                
                pick = random.choice(choose)          # output from random
                print ('computer choose:',pick)
                print ('          ')
                if (pick == 1 and winner == 0):                       # compared random pick with arduino Serial
                    arduino.write(b'1')
                    board_1 ='R'
                    red_1 =1
                if (pick == 2 and winner == 0):
                    arduino.write(b'2')
                    board_2 ='R'
                    red_2 =1
                if (pick == 3 and winner == 0):
                    arduino.write(b'3')
                    board_3 ='R'
                    red_3 =1
                if (pick == 4 and winner == 0):
                    arduino.write(b'4')
                    board_4 ='R'
                    red_4 =1
                if (pick == 5 and winner == 0):
                    arduino.write(b'5')
                    board_5 ='R'
                    red_5 =1
                if (pick == 6 and winner == 0):
                    arduino.write(b'6')
                    board_6 ='R'
                    red_6 =1
                if (pick == 7 and winner == 0):
                    arduino.write(b'7')
                    board_7 ='R'
                    red_7 =1
                if (pick == 8 and winner == 0):
                    arduino.write(b'8')
                    board_8 ='R'
                    red_8 =1
                if (pick == 9 and winner == 0):
                    arduino.write(b'9')
                    board_9 ='R'
                    red_9 =1
#------------------------------------------------------------------------------------------------------

        # game output after computer place red piece
        
        print ('Game update')
        print (board_1, '|', board_4, '|', board_7)
        print ('----------')
        print (board_2, '|', board_5, '|', board_8)
        print ('----------')
        print (board_3, '|', board_6, '|', board_9)
        print ('          ')    
#------------------------------------------------------------------------------------------------------

        # Computer wins ?
        
        if ((board_1=='R'and board_2=='R'and board_3=='R')
            or (board_4=='R'and board_5=='R'and board_6=='R')
            or (board_7=='R'and board_8=='R'and board_9=='R')
            or (board_1=='R'and board_4=='R'and board_7=='R')
            or (board_2=='R'and board_5=='R'and board_8=='R')
            or (board_3=='R'and board_6=='R'and board_9=='R')
            or (board_1=='R'and board_5=='R'and board_9=='R')
            or (board_3=='R'and board_5=='R'and board_7=='R')):

            winner = 2
            print('Computer Win')
            print(' ')
#------------------------------------------------------------------------------------------------------
        # is game end ?
        # reset all parameter
        if ( winner > 0 ):
            print('Please clear board')
            play = input ("Do you want to play again ? (y/n)")  
            if (play == 'y'):
                for i in range (0,5) :
                     print(5-i)
                     time.sleep(1)
                     if(i==4):
                        print('ready')
                        count_1 = 0
                        count_2 = 0
                        count_3 = 0
                        count_4 = 0
                        count_5 = 0
                        count_6 = 0
                        count_7 = 0
                        count_8 = 0
                        count_9 = 0
                        red_1 = 0
                        red_2 = 0
                        red_3 = 0
                        red_4 = 0
                        red_5 = 0
                        red_6 = 0
                        red_7 = 0
                        red_8 = 0
                        red_9 = 0
                        winner = 0
                        blue_1 = 0 
                        blue_2 = 0
                        blue_3 = 0
                        blue_4 = 0
                        blue_5 = 0
                        blue_6 = 0
                        blue_7 = 0
                        blue_8 = 0
                        blue_9 = 0
                        arduino.write(b'0') 
            else :
                break
#-----------------------------------------------------------------------------------------------------------
            
cap.release()
cv2.destroyAllWindows()
