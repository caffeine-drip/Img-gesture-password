import cv2
import numpy as np
import math
import time
def chk():
    cheek=0
    fob=open('D:\pass.txt','r')
    str1=fob.readline()
    str2=""
    cap = cv2.VideoCapture(0)
    faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    palm = cv2.CascadeClassifier('palm.xml')#BOAST ABOUT IT!!
    ii=0
    while(ii<5):
        
        time.sleep(1)
        print "Enter "+str(ii+1)+"th number"
        #D Count BLOCK!!
        co1=0
        co=0
        count1=0
        count2=0
        count3=0
        count4=0
        count5=0
        bb=0
        aa=0
        count=0
        

        while(cap.isOpened()):
            count=count+1
            #time.sleep(1)
            bb=aa
            
            ret, img = cap.read()
            img=cv2.flip(img,1)
           
            cv2.rectangle(img,(400,100),(600,300),(0,255,0),0)
            crop_img = img[100:300, 400:600]
            #print crop_img
            grey = cv2.cvtColor(crop_img, cv2.COLOR_BGR2GRAY)
            gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            value = (35, 35)
            blurred = cv2.GaussianBlur(grey, value, 0)
           

            
            _, thresh1 = cv2.threshold(blurred, 127, 255,
                                       cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
            cv2.imshow('Thresholded', thresh1)
            immg,contours, hierarchy = cv2.findContours(thresh1.copy(),cv2.RETR_TREE, \
                    cv2.CHAIN_APPROX_SIMPLE)

            faces = faceCascade.detectMultiScale(gray,1.1,5)

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
                co=co+1

            palm1=palm.detectMultiScale(grey,1.1,5)
            for (x1,y1,w1,h1) in palm1:
                cv2.putText(img,"Palm detected",(300,300),cv2.FONT_HERSHEY_DUPLEX,1,1)
                co1=co1+1
                #cv2.rectangle(img,(x1,y1),(x1+w1,y1+h1),(255,0,0),2)


            
            max_area = -1
            for i in range(len(contours)):
                cnt=contours[i]
                area = cv2.contourArea(cnt)
                if(area>max_area):
                    max_area=area
                    ci=i
            cnt=contours[ci]
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(crop_img,(x,y),(x+w,y+h),(0,0,255),0)
            hull = cv2.convexHull(cnt)
            drawing = np.zeros(crop_img.shape,np.uint8)
            cv2.drawContours(drawing,[cnt],0,(0,255,0),0)
            cv2.drawContours(drawing,[hull],0,(0,0,255),0)
            hull = cv2.convexHull(cnt,returnPoints = False)
            defects = cv2.convexityDefects(cnt,hull)
            count_defects = 0
            cv2.drawContours(thresh1, contours, -1, (0,255,0), 3)
            for i in range(defects.shape[0]):
                s,e,f,d = defects[i,0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                a = math.sqrt((end[0] - start[0])**2 + (end[1] - start[1])**2)
                b = math.sqrt((far[0] - start[0])**2 + (far[1] - start[1])**2)
                c = math.sqrt((end[0] - far[0])**2 + (end[1] - far[1])**2)
                angle = math.acos((b**2 + c**2 - a**2)/(2*b*c)) * 57
                if angle <= 90:
                    count_defects += 1
                    cv2.circle(crop_img,far,1,[0,0,255],-1)
                #dist = cv2.pointPolygonTest(cnt,far,True)
                cv2.line(crop_img,start,end,[0,255,0],2)
                cv2.circle(crop_img,far,5,[0,0,255],-1)
            if count_defects == 1 and co!=0 and co1!=0:
                cv2.putText(img,"1", (50,50), cv2.FONT_HERSHEY_DUPLEX, 2, 2)
                aa=1
                
            elif count_defects == 2 and co!=0 and co1!=0:
                cv2.putText(img, "2", (50,50), cv2.FONT_HERSHEY_DUPLEX, 2, 2)
                aa=2
            elif count_defects == 3 and co!=0 and co1!=0:
                cv2.putText(img,"3", (50,50), cv2.FONT_HERSHEY_DUPLEX, 2, 2)
                aa=3
                
            elif count_defects == 4 and co!=0 and co1!=0:
                cv2.putText(img,"4", (50,50), cv2.FONT_HERSHEY_DUPLEX, 2, 2)
                aa=4
            elif count_defects ==5 and co!=0 and co1!=0:
                cv2.putText(img,"5",(50,50) ,cv2.FONT_HERSHEY_DUPLEX,2,2)
                aa=5
            else:
                cv2.putText(img,"Enter "+str(ii+1)+"th number", (50,50),\
                            cv2.FONT_HERSHEY_DUPLEX, 2, 2)
            if aa==1:
                count1=count1+1
                if count1==15:
                    bb==aa
                    break
            elif aa==2:
                count2=count2+1
                if count2==25:
                    bb==aa
                    break
            elif aa==3:
                count3=count3+1
                if count3==25:
                    bb==aa
                    break
            elif aa==4:
                count4=count4+1
                if count4==25:
                    bb==aa
                    break
            elif aa==5:
                count5=count5+1
                if count5==25:
                    bb==aa
                    break
            cv2.putText(img,str(count),(580,440),cv2.FONT_HERSHEY_DUPLEX,1,1)
                
            k = cv2.waitKey(10)
            if k == 32:
                ii=0
            cv2.imshow('Gesture', img)
            all_img = np.hstack((drawing, crop_img))
            cv2.imshow('Contours', all_img)
           
            
            if count>=150: #and co!=0 and co1!=0:
                break
            
        str2=str2+str(bb)+""
        ii=ii+1
        if count>=150:
            ii=0
    cv2.destroyWindow('Gesture')

    while(1):
        ret1,img1=cap.read()
        if str2==str1:
                cv2.putText(img1,"ACCESS GRANTED!!",(0,50),cv2.FONT_HERSHEY_DUPLEX,1,1)
                cheek=1
        else:
            
            cv2.putText(img1,"ACCESS DENIED!!",(0,50),cv2.FONT_HERSHEY_DUPLEX,1,1)
            cv2.putText(img1,"YOU ENTERED-"+str2,(50,100),cv2.FONT_HERSHEY_DUPLEX,1,1)
            cheek=0
        cv2.putText(img1,"Press 'ESC' to exit...",(10,400),cv2.FONT_HERSHEY_DUPLEX,1,1)
        cv2.imshow('Gesture', img1)
        if cv2.waitKey(10)==27:
            break


        
    cap.release()
    fob.close()
    cv2.destroyAllWindows()
    return cheek

