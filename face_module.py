import cv2 #for capturing webcam images
from deepface import DeepFace #for face comparison
from datetime import datetime #to get current date and time
import pickle #for saving and loading data
import os #to create folders if they don't exist

os.makedirs("images",exist_ok=True) #This will create a folder called images 
                                    #if it doesn’t already exist. we save user images here.

def train_visitor(visitor_id,name,contact,height,weight,med_hist):
    data={}
    entry=[name,contact,height,weight,med_hist] #This entry list will contain everything we save:
                                 #[name, contact,height,weight,med_hist,date_time, img1, img2, img3]
    now=datetime.now() #adding current date and time
    dt_string=now.strftime("%d/%m/%Y %H:%M:%S") #We store this to know when they first visited.
    entry.append(dt_string)
    cam=cv2.VideoCapture(0) #open the webcam
    #capturing two images
    for i in range(2):
        filename=f"images/f{visitor_id}_{i}.png"
        print("Capturing image...Press Q when ready")
        while True:
            ret,frame=cam.read()
            cv2.imshow(f"{name}_{i}",frame)
            if cv2.waitKey(20) & 0xFF==ord('q'):
                break
        cv2.imwrite(filename,frame)
        cv2.destroyWindow(f"{name}_{i}")
        entry.append(filename)
    data[visitor_id]=entry
    f=open("visitor_data.dat","ab")
    pickle.dump(data,f)
    f.close()
    cam.release()
    return {"status": "success", "visitor_id": visitor_id}


def recognize_visitor():
    try:
        cam = cv2.VideoCapture(0)
        print("Capturing visitor image... Press Q when ready.")
        while True:
           ret, frame = cam.read()
           cv2.imshow("Visitor", frame)
           if cv2.waitKey(20) & 0xFF == ord('q'):
            break
        cv2.imwrite("Visitor.png", frame) #it saves the image as "Visitor.png".
        cv2.destroyWindow("Visitor")
        cam.release()
        img1=frame #the newly captured image
        recognized=False #flag to check if the match is found
        f=open("visitor_data.dat", "rb")
        try:
             while True:
                record = pickle.load(f)
                for k, v in record.items():
                    for i in range(2):  # 2 images per visitor
                        img2 = cv2.imread(v[6 + i])
                        result = DeepFace.verify(img1, img2, enforce_detection=False)
                        if result['distance'] < 0.3:
                            recognized = True
                            return {
                                "Status": "Known",
                                "Name": v[0],
                                "Contact": v[1],
                                "Last_visit": v[2],
                                "Height": v[3],
                                "Weight" : v[4],
                                "Medical_History" : v[5]
                            }
        except EOFError:
               f.close()
        return {"status": "new"}

    
    except FileNotFoundError:
        return {"status": "error", "message": "No data file found"}

'''File Format after saving will look like:
{
  "101": ["Alice", "1234567890", "5.4", "60", "No allergies", "10/06/2025 21:30:10", "images/f101_0.png", "images/f101_1.png"]
}'''
 



