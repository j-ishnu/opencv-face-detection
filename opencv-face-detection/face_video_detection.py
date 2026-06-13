# -----------------------------------------------------------
# OpenCV Face Detection in Video
#
# Author: ZeroTrace
#
# Disclaimer:
# This project is created for educational and learning purposes.
# Face detection is performed using OpenCV's Haar Cascade
# Classifier and may not detect all faces accurately in every
# video. Detection results can vary depending on video quality,
# lighting conditions, face orientation, distance from the
# camera, and parameter settings.
#
# The reported face count is based on detections made by the
# algorithm and should not be considered an exact count of
# unique individuals.
# -----------------------------------------------------------
import cv2
face_cascade=cv2.CascadeClassifier(
	"haarcascade_frontalface_default.xml"
)
vid=cv2.VideoCapture("")# <-- Add your video file path  
n=0
check=input("Want to watch the video?(y/n):")
if check=="n":
	print("\nwait while the program checks the no. of faces.......")
	print("\nIf the video is longer it may take more time.")
while True:
	ret,frame=vid.read()
	if ret==False:
		break
	if ret==True:
		gray=cv2.cvtColor(
			frame,
			cv2.COLOR_BGR2GRAY
		)
		faces=face_cascade.detectMultiScale(
			gray,
			scaleFactor=1.3,
			minNeighbors=8                   #3-5 For more faces but more false positive 8-12 for strict positives (few faces may miss) 
		)
		for x,y,w,h in faces:
			cx=(x+x+w)//2
			cy=(y+y+h)//2
			cv2.rectangle(
				frame,
				(cx,cy),
				(x+w,y+h),
				(10,255,0),
				2
			)
		if len(faces)>n:
			n=n+len(faces)
		else:
			n=n+0	
		if check=="y":
			cv2.imshow("Video",frame)
			if cv2.waitKey(1)==ord("q"):
				break
		elif check=="n":
			continue
		else:
			print("\nTry again and Enter y/n")	
			break
vid.release()
cv2.destroyAllWindows()
if n!=0:									
	print("\nNo .of faces detected:",n)				
else:
	print("\nCouldn't detect faces")

