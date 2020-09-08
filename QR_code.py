#import essential libraries
import cv2
import qrcode

def QR_maker(data):
    #name of your qr code
    output="your_QRcode.png"
    #create qr code
    img=qrcode.make(data)
    #save the qr code
    img.save(output)

def QR_decoder (data):
    #read the image
    img=cv2.imread(data)
    #decoding qr code
    detector = cv2.QRCodeDetector()
    data, box, straight_qrc = detector.detectAndDecode(img)
    print(data)


print(
     "QR CODE \n"
      "Enter 1 to Create QR Code \n"
      "Enter 2 to Decode QR Code with png Format \n"
      )

select=int(input("Enter 1 or 2 ..."))

#call suitable function
if select==1:
    #enter a value to make qr code
    data=input("Enter Your Info to Make QR Code ...")
    QR_maker(data)

elif select==2:
    #enter the name of you image with png format ====> "your_qr_image.png"
    data=str(input("Enter Name of Your QR Code Image With Format : your_qr_image.png ...\n"))
    QR_decoder(data)

else:
    print("Wrong Value !!! ")
