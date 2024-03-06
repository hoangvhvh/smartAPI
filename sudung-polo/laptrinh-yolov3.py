#Buoc 1: Su dung thu vien
import os
from imageai.Detection import  ObjectDetection

folder = 'E:/HMUD/smartAPI/models'
print("Bắt đầu tải mô hình YOLO v3 vào bộ nhớ")
detector = ObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(folder, "yolov3.pt"))
try:
    detector.loadModel()
except FileNotFoundError:
    print("Model file not found. Please check the path.")
print("Hoàn thành tải mô hình vào bộ nhớ")

#Nhận dạng vật thể trong ảnh
#đường dẫn ảnh
img_folder = "E:/HMUD/smartAPI/images"
img_name = "car.jpg"
detections = detector.detectObjectsFromImage(input_image=os.path.join(img_folder, img_name),
                                             output_image_path=os.path.join(img_folder, "car-new.jpg"),
                                             minimum_percentage_probability=30)

for eachObject in detections:
    print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
    print("--------------------------------")