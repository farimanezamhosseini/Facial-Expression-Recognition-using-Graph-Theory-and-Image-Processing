import cv2

emotions=['sad','happy','angry','neutral']
emotion_id=0

for emotion in emotions:

 with open(emotion+'.txt','r') as f:
    images = [line.strip() for line in f]

 face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

 count = 0
 

 for image in images:
    img = cv2.imread("dataset/"+emotion+"/"+image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(img, (x,y) , (x+w,y+h) , (255,0,0) , 2)     
        count += 1

        
        cv2.imwrite("dataset/User/"+ emotion+ '.' +str(emotion_id)+"."+ str(count) + ".jpg", gray[y:y+h,x:x+w])

 emotion_id+=1 
      

print("\n Done creating face data")