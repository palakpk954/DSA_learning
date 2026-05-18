import cv2
import boto3
from cvzone.HandTrackingModule import HandDetector

ec2 = boto3.client('ec2')
detector = HandDetector(maxHands=1)

cap = cv2.VideoCapture(0)
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)
    if hands:
        fingers = detector.fingersUp(hands[0])
        count = fingers.count(1)
        if count == 1:
            ec2.run_instances(ImageId='ami-xxxxxx', MinCount=1, MaxCount=1, InstanceType='t2.micro')
        elif count == 5:
            ec2.terminate_instances(InstanceIds=['i-xxxxxxx'])
