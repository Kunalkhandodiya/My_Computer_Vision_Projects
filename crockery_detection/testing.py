from ultralytics import YOLO
from PIL import Image
import cv2
#model =YOLO('C:/Users/Admin/PycharmProjects/pythonProject3/crockery_detection.pt')
model=YOLO('C:/Users/Admin/Downloads/invoice1.pt')
results=model("C:/Users/Admin/Downloads/hd/2.jpg",show=True)
#results=model("D:/YOLO v8/Crockery_images/platek1.jpg",show=True)
cv2.waitKey(0)
