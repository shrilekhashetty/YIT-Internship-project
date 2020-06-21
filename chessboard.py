import numpy as np
import cv2
b = np.zeros([400,400],dtype = 'uint8')
for j in range(50,400,100):
        for i in range (50,400,100):   
            b[j-50:j,i-50:i] = 255
            b[j:j+50,i:i+50] = 255 
cv2.imshow('checker board 8*8',b)
cv2.waitKey(0)
cv2.destroyAllWindows()
