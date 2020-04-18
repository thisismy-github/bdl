import os, subprocess, time, shutil
from zipfile import ZipFile

time.sleep(1)   # sleep to allow bdl time to close

try:
    with ZipFile('bdl.zip', 'r') as bdlZip:
       bdlZip.extractall()
    for file in os.listdir('bdl'):
        if file != 'res': shutil.move('bdl/'+file, file)
    for file in os.listdir('bdl/res'):
        shutil.move('bdl/res/'+file, 'res/'+file)
    os.removedirs('bdl')
    os.remove('bdl.zip')

except Exception as error:
    with open('UPDATEFAILED.TXT', 'w') as errorFile:
        errorFile.write(str(error))
    os.removedirs('bdl')
    os.remove('bdl.zip')

#subprocess.Popen('bdl.exe')    # soon... soon.
subprocess.Popen('python window_main.py')