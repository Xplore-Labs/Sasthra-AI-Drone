import dropbox
from imageai.Detection import ObjectDetection
import os
global i
global j
i=0
j=0
execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()
while 1:
     try:
        x=str(i)+".jpg"
        file_name=x
        dropbox_path='/drone/'
        dbx=dropbox.Dropbox('RsX-jbaVX9AAAAAAAAAAHHIzoAHauC0FAO_BVFO3K4efN90u2uBs_GzbXB4NbvzV')
        dbx.files_download_to_file(str(x),dropbox_path+file_name)
        print("Downloaded %s"%(x))
        detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path ,x), output_image_path=os.path.join(r'C:\Users\Rishi\Desktop\drones\output' , "{0}.jpg".format(i)))
        for eachObject in detections:
              print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
              if eachObject["name"]=="person":
                  j=j+1              
        print("There are totally " + str(j) + " people in the locality" )
        i=i+1
     except dropbox.exceptions.ApiError:
        print("Error in downloading %s"%(i))
