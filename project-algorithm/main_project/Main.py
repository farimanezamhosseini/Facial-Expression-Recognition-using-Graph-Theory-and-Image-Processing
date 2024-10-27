import cv2
import dlib

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

img = cv2.imread('p3.jpg', 1)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces_in_image = detector(img_gray, 0)

for face in faces_in_image:

    landmarks = predictor(img_gray, face)

    landmarks_list = []
    for i in range(0, landmarks.num_parts):
        landmarks_list.append((landmarks.part(i).x, landmarks.part(i).y))

    lx = -1
    ly = -1
    j = 1
    for landmark_num, xy in enumerate(landmarks_list, start = 1):
        cv2.circle(img, (xy[0], xy[1]), 4, (168, 0, 20), -1)
        if lx != -1 and j != 18 and j != 28 and j != 37 and j != 43 and j != 49:
            cv2.line(img, (lx, ly), (xy[0], xy[1]), (168, 0, 20), 2)
        lx = xy[0]
        ly = xy[1]
        j+=1

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
