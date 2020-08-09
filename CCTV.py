#!/usr/bin/env python
# coding: utf-8

# In[1]:





# In[1]:


import cv2
cap=cv2.VideoCapture('http://192.168.0.102:8080/video')
while True:
    status , photo =cap.read()
    cv2.imshow('mobile or cctv', photo)
    if cv2.waitKey(1)==27:
        break
        
cv2.destroyAllWindows()
cap.release()


# In[ ]:





# In[ ]:





# In[3]:


import cv2
cap=cv2.VideoCapture('http://192.168.0.101:8080/video')
while True:
    status , photo = cap.read()
    cv2.imshow('mobile or cctv', photo)
    if cv2.waitKey(1)==27:
        break
        
cv2.destroyAllWindows()
cap.release()


# In[ ]:




