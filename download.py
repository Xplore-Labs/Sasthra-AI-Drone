from imageai.Detection import ObjectDetection
import dropbox
import os
dbx=dropbox.Dropbox('RsX-jbaVX9AAAAAAAAAAHHIzoAHauC0FAO_BVFO3K4efN90u2uBs_GzbXB4NbvzV')
execution_path = os.getcwd()
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_weights_tf_dim_ordering_tf_kernels.h5"))
detector.loadModel()

while 1:
    for i in range(100):
        x=str(i)+".jpg"
        file_name=x
        dropbox_path='/drone/'
        with open(file_name, 'rb') as f:
            dbx.files_download(f.read(),dropbox_path+file_name,mute=True)
            detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "{0}.jpg".format(i)), output_image_path=os.path.join(execution_path , "imagenew.jpg"))

            for eachObject in detections:
                print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
        print("Downloaded %s"%(x))
