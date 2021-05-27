import cv2
import dropbox
import time
import random
start = time.time()
def pic ():
    number = random.randint(0,100)
    cap = cv2.VideoCapture(0)
    result = True
    while (result):
        ret,frame = cap.read()
        img = "New"+str(number)+".png"
        cv2.imwrite(img,frame)
        start = time.time()
        result = False
        return img
    cap.release()
    cv2.destroyAllWindows()

def upload (img) :
    access_token = 'q2vzry6jFoIAAAAAAAAAAf8QnH5mEU1E1DuyTSxEQgqaCUVu3R9MvFy_ATSVdgKT'
    file = img 
    file_from = file
    file_to = "/test/"+ (img)
    dbx = dropbox.Dropbox(access_token)
    with open (file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode= dropbox.files.WriteMode.overwrite)
def main () :
    while (True):
        if ((time.time()-start)>=5):
            name = pic()
            upload (name)
main()