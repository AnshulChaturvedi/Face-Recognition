from sklearn.neighbors import KNeighborsClassifier
import pickle as pk
import numpy as np
import cv2
import os
import xlwt
import time
from datetime import datetime
import pyttsx3, openpyxl

video = cv2.VideoCapture(0)
faces = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

with open('Data/names.pkl','rb') as f:
        LABELS = pk.load(f)

with open('Data/face_data.pkl','rb') as f:
        FACES = pk.load(f)


knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)
img_bg = cv2.imread('background.png')


COL_NAMES = ['NAME', 'TIME']

while True:
    ret, frame = video.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    f_detect = faces.detectMultiScale(gray, 1.3 ,5)
    L = []
    for (x,y,w,h)in f_detect:
        croped_img = frame[y:y+h, x:x+w, :]
        resize = cv2.resize(croped_img, (50,50)).flatten().reshape(1,-1)
        output = knn.predict(resize)
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M:%S")
        file_exists = os.path.isfile("Attendance/Attedance_"+date+".csv")
        cv2.putText(frame, str(output[0]), (x,y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255),1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255),1)
        attendance = [str(output[0]), str(timestamp)]
        cv2.imshow('Taking Shot!',frame)
        k = cv2.waitKey(1)     
    if k==ord('q'):
          book = openpyxl.load_workbook('Attendance\Attendance.xlsx')
          sheet = book.active
          L1 = []
          for row in sheet['1']:  
              L1.append(row.value)

          if date not in L1:
            sheet.cell(row=1,column = len(sheet['1'])+1).value = date
            book.save('Attendance\Attendance.xlsx')

          L2= []
          for column in sheet['A']:
            L2.append(column.value)
        #   print(L2)
          if int(output[0]) in L2:
                x = L2.index(int(output[0]))+1
                sheet.cell(row=x,column=len(sheet[str(x)])).value = 'p'
                book.save('Attendance\Attendance.xlsx')
                # print('yes')
                bot = pyttsx3.init()
                statement = 'Attendance Taken!'
                bot.setProperty('rate',120)
                bot.say(statement)
                bot.runAndWait()
    book = openpyxl.load_workbook('Attendance\Attendance.xlsx') 
    sheet = book.active
    L3 = []
    col = sheet['1']
    len_col = len(col)
    x = openpyxl.utils.cell.get_column_letter(len_col)
#     print(x)
    for column in sheet[x]:
        L3.append(column.value)
#     print(L3)
    for i in range(len(L3)):
        if L3[i]==date or L3[i]=='p':
            pass
        elif L3[i]==None:
            sheet.cell(row=i+1, column = len_col).value = 'a'
            book.save('Attendance\Attendance.xlsx')
        #     print('done')oo
    if k==ord('o'):
        video.release()
        cv2.destroyAllWindows()

