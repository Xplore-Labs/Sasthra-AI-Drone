import dropbox
import os
dbx=dropbox.Dropbox('RsX-jbaVX9AAAAAAAAAAHHIzoAHauC0FAO_BVFO3K4efN90u2uBs_GzbXB4NbvzV')
dbx.files_delete_v2('/drone')
while 1:
    for i in range(100):
        os.system("sudo raspistill -n -rot 0 -v -br 60 -q 20 -o {0}.jpg".format(i))
        x=str(i)+".jpg"
        file_name=x
        dropbox_path='/drone/'
        with open(file_name, 'rb') as f:
            dbx.files_upload(f.read(),dropbox_path+file_name,mute=True)
        print("Uploaded %s"%(x))
