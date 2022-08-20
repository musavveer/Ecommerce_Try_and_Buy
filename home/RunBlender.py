import  os

def runBlender():

    path_ = os.getcwd() + "\\home\\blenderScript.py"
    print(path_)

    #specify the path where the Blender.exe exists
    os.chdir("C:\\Users\\inish\\desktop\\DOC\\repo\\ps6_Team_Shannon\\Blender3.2")

    os.system('.\\blender -b --python ' + str(path_))
