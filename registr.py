import numpy as np
import cv2
import random

class regist:
	def record_face(self,im):
		cam = cv2.VideoCapture(0)
		face_cas = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')
		eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
		data=[]
		ix = 0

		while True:
			ret, frame = cam.read()
			if ret == True:
				gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
				faces = face_cas.detectMultiScale(gray, 1.3, 5)
				for (x, y, w, h) in faces:
					face_component = frame[y:y+h, x:x+w, :]
					fc = cv2.resize(face_component, (50, 50))
					if ix%10 == 0 and len(data) < 20:
						data.append(fc)
					cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
					roi_gray = gray[y:y+h, x:x+w]
					roi_color = frame[y:y+h, x:x+w]
					eyes = eye_cascade.detectMultiScale(roi_gray)
					for (ex,ey,ew,eh) in eyes:
						cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
				ix += 1
				cv2.imshow('frame', frame)
				if cv2.waitKey(1) == 27 or len(data) >= 20:
					break
			else:
				print ("error")
		cv2.destroyAllWindows()
		data = np.asarray(data)
		print (data.shape)
		ss = str(im) + '.png'
		print(ss)
		np.save('database/' + str(im), data)
		cv2.imwrite('database/' + ss, fc)
		#np.save('database/face_03', data)
