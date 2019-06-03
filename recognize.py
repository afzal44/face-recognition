import ctypes
import time
import numpy as np
import cv2
import updateDabase as fl

class recogn:
    def recog(self):
        cam = cv2.VideoCapture(0)
        face_cas = cv2.CascadeClassifier('./haarcascade_frontalface_default.xml')


        font = cv2.FONT_HERSHEY_SIMPLEX


        a = np.load('./database/1.npy').reshape((20, 50*50*3))
        b = np.load('./database/2.npy').reshape((20, 50*50*3))
        c = np.load('./database/3.npy').reshape((20, 50*50*3))
        d = np.load('./database/4.npy').reshape((20, 50*50*3))
        e = np.load('./database/5.npy').reshape((20, 50*50*3))
        f = np.load('./database/6.npy').reshape((20, 50*50*3))
        g = np.load('./database/7.npy').reshape((20, 50*50*3))
        h = np.load('./database/8.npy').reshape((20, 50*50*3))
        i = np.load('./database/9.npy').reshape((20, 50*50*3))
        j = np.load('./database/10.npy').reshape((20, 50*50*3))

        names = [
            'ROLL:1',
            'ROLL:2',
            'ROLL:3',
            'ROLL:4',
            'ROLL:5',
            'ROLL:6',
            'ROLL:7',
            'ROLL:8',
            'ROLL:9',
            'ROLL:10',
            ]


        labels = np.zeros((600, 1))
        labels[:20, :] = 0.0
        labels[20:40, :] = 1.0
        labels[40:, :] = 2.0


        data = np.concatenate([a, b, c, d, e, f, g, h, i])	# (60, 7500)
        print (data.shape, labels.shape)	# (60, 1)


        def distance(x1, x2):
            return np.sqrt(((x1-x2)**2).sum())

        def knn(x, train, targets, k=5):
            m = train.shape[0]
            dist = []
            for ix in range(m):

                dist.append(distance(x, train[ix]))
            dist = np.asarray(dist)
            indx = np.argsort(dist)
            sorted_labels = labels[indx][:k]
            counts = np.unique(sorted_labels, return_counts=True)
            return counts[0][np.argmax(counts[1])]

        while True:

            ret, frame = cam.read()

            if ret == True:

                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = face_cas.detectMultiScale(gray, 1.3, 5)

                # for each face
                for (x, y, w, h) in faces:
                    face_component = frame[y:y+h, x:x+w, :]
                    fc = cv2.resize(face_component, (50, 50))

                    lab = knn(fc.flatten(), data, labels)
                    text = names[int(lab)]
                    print(text)

                    #===================================================================================================
                    #ctypes.windll.user32.MessageBoxW(0, "Nex Student", "Face Matching", 1)
                    #time.sleep(60)

                    # ===================================================================================================
                    # display the name
                    cv2.putText(frame, text, (x, y), font, 1, (255, 255, 0), 2)

                    # draw a rectangle over the face
                    cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                    cv2.imshow('face recognition', frame)


                if cv2.waitKey(1) == 27:
                    #break
                    #time.sleep(1)
        #===================================================================================================
                    x = text.split(":")
                    fl.updateDabase1(x[1])
                    time.sleep(5)
                    cv2.destroyAllWindows()
                    break
        # ===================================================================================================

            else:
                print('Error')


