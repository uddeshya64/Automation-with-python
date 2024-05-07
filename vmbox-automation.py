import cv2#import opencv-python
import subprocess
import os
cap = cv2.VideoCapture(0)
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector()
while True:#using loop for creating video
    
    status, photo=cap.read()
    #cv2.imwrite("Uddeshya.jpg" , photo)#save the photo
    #Ai to CV(Computer Vision)
    #pip install cvzone
    #pip install mediapipe

    cv2.imshow("my photo" , photo)#to see the photo automatically

    if cv2.waitKey(250) == 13:
        break#keep the photo open for 0.05 second, if () left empty the photo will we open forever unless to click enter or any oter key in fast moving photos will become a video. by clik enter while loop will stop we can use 13 insted of enter as on our keybord ever key has its number.
   
    handphoto = detector.findHands(photo , draw = False)
   
    if handphoto:
        lmlist = handphoto[0]
        fingerstatus = detector.fingersUp(lmlist)

        if fingerstatus == [0,1,0,0,0]:
            #lmlist = handphoto[0]#lmlist or landmark list is list of landmark on our hand by which we can identify fingres
            #fingerstatus = detector.fingersUp(lmlist)#to detect fingrs up
            fingerstatus
            def launch_virtual_machine(vm_name):
                try:
                    # Construct the VBoxManage command to start the VM in headless mode
                    vboxmanage_cmd = [
            'VBoxManage', 'startvm', vm_name, '--type', 'headless'
                    ] 

                    # Run the VBoxManage command using subprocess
                    subprocess.run(vboxmanage_cmd, check=True)
                    print(f"Virtual machine '{vm_name}' has been started.")
                except subprocess.CalledProcessError as e:
                  print(f"An error occurred: {e}")

            if __name__ == "__main__":
             vm_name = "linuxMint" 
             launch_virtual_machine(vm_name)
            print("all up")          
        
        elif fingerstatus == [0,1,1,0,0]:
            print("index fingre up")
            def shutdown_virtual_machine(vm_name):
                try:
                    vboxmanage_cmd = [
            'VBoxManage', 'controlvm', vm_name, 'acpipowerbutton'
                    ]
                    subprocess.run(vboxmanage_cmd, check=True)
                    print(f"Virtual machine '{vm_name}' is being shut down.")
                except subprocess.CalledProcessError as e:
                    print(f"An error occurred: {e}")
            if __name__ == "__main__":
                vm_name = "linuxMint" 
                shutdown_virtual_machine(vm_name)   
       
        elif fingerstatus == [1,0,0,0,0]:
            os.system("firefox")
            print("have a good day")
            

cv2.destroyAllWindows()#after 0.5 second destroy\close the photo window
cap.release()

    