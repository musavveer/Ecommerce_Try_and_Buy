# Importing all necessary libraries
import cv2
import os

# Read the video from specified path
#changes

def extract():
    vids = []
    for root, directories, file in os.walk(os.getcwd() + '\static\images'):
            for file in file:
                if(file.endswith(".mp4")):
                    print(os.path.join(root,file))
                    vids.append(os.path.join(root,file))



    vidcap = cv2.VideoCapture(vids[0])

    totalframecount= int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))

    print("The total number of frames in this video is ", totalframecount)

    try:
        # creating a folder named data
        if not os.path.exists('data'):
            os.makedirs('data')

    except OSError:
        print('Error: Creating directory of data')

    def getFrame(sec):
        vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
        hasFrames,image = vidcap.read()
        if hasFrames:
            cv2.imwrite("static/images/Frames/frame" + str(count) + ".jpg", image)     # save frame as JPG file
        return hasFrames



    sec = 0
    frameRate = 1 #//it will capture image in each 0.5 second
    count = 1
    success = getFrame(sec)
    while success:
        count = count + 1
        sec = sec + frameRate
        sec = round(sec, 2)
        success = getFrame(sec)



    # Release all space and windows once done
    vidcap.release()
    cv2.destroyAllWindows()