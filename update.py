#
# Contains all update-related functions and classes.
#

from PyQt5 import QtWidgets
import os, subprocess, urllib.request
from datetime import datetime

class UpdateDoubleCheckFailed(Exception):
    ''' Raised when update() returns False for canUpdate.  '''
    def __str__(self):
        return 'UpdateDoubleCheckFailed: update invalidated or no longer available. restart BDL or try again later.'


def checkUpdateSuccess(bdl):
    if os.path.exists('UPDATEFAILED.TXT'):
        try:
            with open('UPDATEFAILED.TXT', 'r') as errorFile:
                error = errorFile.read()
            os.remove('UPDATEFAILED.TXT')
            bdl.showPopup(title='Update failed',
                            text='An unexpected error occured while\n'
                                'installing your update. Refer to\n'
                                'the error below for more information.',
                            textDetailed=error,
                            textDetailedAutoOpen=True,
                            icon=QtWidgets.QMessageBox.Critical)
        except Exception as error:
            print(error)
    if os.path.exists('bdlUpdateUtility.py'): os.remove('bdlUpdateUtility.py')


def checkUpdate(bdl, noChanges=False):
    print('checking for updates')
    try:
        with urllib.request.urlopen('https://thisismywebsite.net/bdlversion.txt') as response:
            latestVersionStr = response.read().decode("utf-8")  # returns byte string -> decode
            latestVersion = int(''.join(latestVersionStr[:5].split('.')))
            print(latestVersionStr)
        if latestVersion > bdl.bdlVersion:     # update found
            if noChanges: return True, latestVersionStr
            bdl.ui.tabWidget.setTabText(3, 'bdl (!)')
            bdl.ui.bdlUpdateButton.setToolTip(f'Current version: {bdl.bdlVersionStr}\nLatest version: {" ".join(latestVersionStr.split()[:2])}')
            bdl.ui.bdlUpdateButton.setEnabled(True)
        else:
            if noChanges: return False, None
            bdl.ui.tabWidget.setTabText(3, 'bdl')
            bdl.ui.bdlUpdateButton.setToolTip('No update available.')
            bdl.ui.bdlUpdateButton.setEnabled(False)
    except Exception as error:
        print(error)
        if noChanges: return False, None
    date = datetime.now()
    bdl.ui.bdlUpdateLastCheckLabel.setText(f'Last check: {date.month:02d}/{date.day:02d}/{str(date.year)[2:]}')



def update(bdl):
    try:
        canUpdate, latestVersionStr = checkUpdate(bdl, noChanges=True)
        if canUpdate:
            updaterUrl, latestVersionUrl = latestVersionStr.split('\n')[1:]

            bdl.ui.bdlUpdateCheckNowButton.setEnabled(False)
            bdl.ui.bdlUpdateButton.setEnabled(False)
            bdl.ui.bdlDownloadLabel.show()
            bdl.ui.bdlDownloadProgress.show()
            bdl.ui.tabWidget.setTabEnabled(0, False)
            bdl.ui.tabWidget.setTabEnabled(1, False)
            bdl.ui.tabWidget.setTabEnabled(2, False)

            urllib.request.urlretrieve(updaterUrl, 'bdlUpdateUtility.py')
            urllib.request.urlretrieve(latestVersionUrl, 'bdl.zip')
            subprocess.Popen('python bdlUpdateUtility.py')
            bdl.window.close()
        else:
            raise UpdateDoubleCheckFailed
    except Exception as error:
        # undo all changes from checkUpdate() and update()
        bdl.ui.bdlUpdateCheckNowButton.setEnabled(True)
        bdl.ui.bdlUpdateButton.setEnabled(False)  # keep update button disabled
        bdl.ui.bdlDownloadLabel.hide()
        bdl.ui.bdlDownloadProgress.hide()
        bdl.ui.tabWidget.setTabEnabled(0, True)
        bdl.ui.tabWidget.setTabEnabled(1, True)
        bdl.ui.tabWidget.setTabEnabled(2, True)
        bdl.ui.tabWidget.setTabText(3, 'bdl')
        bdl.ui.bdlUpdateButton.setToolTip('An update was found, but failed to install.')
        bdl.showPopup(title='Update failed',
                        text='An unexpected error occured while\n'
                            'downloading your update. Refer to\n'
                            'the error below for more information.',
                        textDetailed=str(error),
                        textDetailedAutoOpen=True,
                        icon=QtWidgets.QMessageBox.Critical)