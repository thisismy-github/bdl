#
# Contains all config-related functions, including loading and saving
# configs, running a first time setup, and detecting pre-existing IWADs.
#

import os, platform, shutil, configparser

def loadConfig(bdl, file="bdl.ini"):
    if not os.path.exists(file):
        firstTimeSetup(bdl)
    else:
        config = configparser.ConfigParser()
        config.read(file)

        # load saved pwads/iwads/ports
        # TODO add if file != "bdl.ini" for performance here?
        if 'bdl.iwads' in config:
            if config.items('bdl.pwads'):
                bdl.clearListWidgetItems(bdl.ui.iwadList)
                index = 0
                while config['bdl.iwads'].get(f'iwadpath{index}'):
                    try:
                        bdl.addFileFromConfig(bdl.ui.iwadList,
                                              path=config['bdl.iwads'].get(f'iwadpath{index}'),
                                              name=config['bdl.iwads'].get(f'iwadname{index}'),  # TODO: fallback=?
                                              warpStyle=config['bdl.iwads'].get(f'iwadwarp{index}'))
                    except Exception as error:
                        print("iwad:",error)   # TODO: clean up error stuff here
                    index+=1

        if 'bdl.pwads' in config:
            if config.items('bdl.pwads'):
                bdl.clearListWidgetItems(bdl.ui.pwadList)
                index = 0
                while config['bdl.pwads'].get(f'pwadpath{index}'):
                    try:
                        bdl.addFileFromConfig(bdl.ui.pwadList,
                                              path=config['bdl.pwads'].get(f'pwadpath{index}'),
                                              name=None,
                                              checked=config['bdl.pwads'].getboolean(f'pwadchecked{index}'))
                    except Exception as error:
                        print("pwad:",error)
                    index+=1
        if 'bdl.ports' in config:
            if config.items('bdl.ports'):
                bdl.clearPorts(showWarning=False)
                index = 0
                while config['bdl.ports'].get(f'portpath{index}'):
                    try:
                        bdl.addFileFromConfig(bdl.ui.portCombo,
                                              path=config['bdl.ports'].get(f'portpath{index}'),
                                              name=config['bdl.ports'].get(f'portname{index}'))
                    except Exception as error:
                        print("port:",error)
                    index+=1

        # set window size/pos, splitter sizes, other settings
        if 'bdl.general' in config:
            if file == "bdl.ini":   # don't move window when loading custom configs
                windowSizeX, windowSizeY = config['bdl.general'].get('windowsize',fallback='225,247').split(",")
                bdl.window.resize(int(windowSizeX), int(windowSizeY))
                windowPosX, windowPosY = config['bdl.general'].get('windowpos',fallback='350,250').split(",")
                bdl.window.move(int(windowPosX), int(windowPosY))

            # each setting is wrapped in a try-except block to restore it to the default
            # set in Qt designer when the UI was created in case of user tampering.
            # indexes are done in two lines: first line sets invalid
            # values to -1, second line changes index if it's -1.
            general = config['bdl.general']
            try: bdl.ui.splitter.setSizes(list(int(size) for size in general.get('lastsplittersize').split(',')))
            except Exception as e: print(e)
            try: bdl.lastDir = general.get('lastdir', fallback='.')
            except Exception as e: print(e)
            try: bdl.ui.bdlAutoClose.setChecked(general.getboolean('autoclose', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.bdlCapitalization.setChecked(general.getboolean('capilization', fallback=True))
            except Exception as e: print(e)
            try:
                bdl.ui.bdlCapitalizationCombo.setCurrentIndex(general.getint('capilizationindex', fallback=0))
                bdl.ui.bdlCapitalizationCombo.setCurrentIndex(max(bdl.ui.bdlCapitalizationCombo.currentIndex(), 0))
            except Exception as e: print(e)
            try: bdl.ui.bdlDetectIWADs.setChecked(general.getboolean('detectiwads', fallback=True))
            except Exception as e: print(e)
            try: bdl.ui.bdlRejectBadIWADs.setChecked(general.getboolean('rejectbadiwads', fallback=True))
            except Exception as e: print(e)
            try: bdl.ui.bdlPWADsCheckable.setChecked(general.getboolean('pwadscheckable', fallback=True))
            except Exception as e: print(e)
            try: bdl.ui.bdlAutoUpdateCheck.setChecked(general.getboolean('autocheckupdates', fallback=True))
            except Exception as e: print(e)
            try: bdl.ui.bdlUpdateLastCheckLabel.setText(general.get('lastupdatecheck', fallback='Last check: N/A'))
            except Exception as e: print(e)
            if file == "bdl.ini":   # don't queue updates from custom configs
                try: bdl.updateReady = general.getboolean('updateready', fallback=False)
                except Exception as e: print(e)

        if 'bdl.save' in config:
            save = config['bdl.save']
            try: bdl.ui.parameterLineEdit.setText(save.get('extra', fallback=''))
            except Exception as e: print(e)
            try:
                bdl.ui.portCombo.setCurrentIndex(save.getint('portindex', fallback=0))
                bdl.ui.portCombo.setCurrentIndex(max(bdl.ui.portCombo.currentIndex(), 0))
            except Exception as e: print(e)
            try:
                bdl.ui.iwadList.setCurrentRow(save.getint('iwadindex', fallback=0))
                bdl.ui.iwadList.setCurrentRow(max(bdl.ui.iwadList.currentRow(), 0))
            except Exception as e: print(e)
            try:
                bdl.ui.complevelCombo.setCurrentIndex(save.getint('complevelindex', fallback=0))
                bdl.ui.complevelCombo.setCurrentIndex(max(bdl.ui.complevelCombo.currentIndex(), 0))
            except Exception as e: print(e)

            try: bdl.ui.demoGroup.setChecked(save.getboolean('demoenabled', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.demoRecordRadio.setChecked(save.getboolean('demorecord', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.demoRecordNameLineEdit.setText(save.get('demorecordname', fallback=''))
            except Exception as e: print(e)
            try: bdl.ui.demoPlayRadio.setChecked(save.getboolean('demoplay', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.demoPlayPathLineEdit.setText(save.get('demoplaypath', fallback=''))
            except Exception as e: print(e)
            try: bdl.ui.demoAutoRecordCheck.setChecked(save.getboolean('demoautorecord', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.demoLongTicsCheck.setChecked(save.getboolean('demolongtics', fallback=False))
            except Exception as e: print(e)

            try: bdl.ui.warpGroup.setChecked(save.getboolean('warpenabled', fallback=False))
            except Exception as e: print(e)
            # fill map warp dropdown here, or else it will try to setCurrentIndex on an empty dropdown
            bdl.fillWarpMapCombo(bdl.ui.iwadList.currentItem())
            try:
                bdl.ui.warpMapCombo.setCurrentIndex(save.getint('warp', fallback=0))
                bdl.ui.warpMapCombo.setCurrentIndex(max(bdl.ui.warpMapCombo.currentIndex(), 0))
            except Exception as e: print(e)
            # skill config is 1-5 instead of index (0-4) to match up with how doom reads the -skill parameter
            try:
                bdl.ui.warpSkillCombo.setCurrentIndex((save.getint('skill', fallback=4))-1)
                bdl.ui.warpSkillCombo.setCurrentIndex(max(bdl.ui.warpSkillCombo.currentIndex(), 1))
            except Exception as e: print(e)

        if 'bdl.moreparameters' in config:
            params = config['bdl.moreparameters']
            try: bdl.ui.paramGroup.setChecked(params.getboolean('showmoreparameters', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.paramFast.setChecked(params.getboolean('fast', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.paramRespawn.setChecked(params.getboolean('respawn', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.paramSoloNet.setChecked(params.getboolean('solo-net', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.paramLevelStat.setChecked(params.getboolean('levelstat', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.paramNoSound.setChecked(params.getboolean('nosound', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.paramNoMonsters.setChecked(params.getboolean('nomonsters', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.paramNoMusic.setChecked(params.getboolean('nomusic', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.paramNoSFX.setChecked(params.getboolean('nosfx', fallback=False))
            except Exception as e: print(e)
            try: bdl.ui.paramTurboSpin.setValue(params.getint('turbo', fallback=100))
            except Exception as e: print(e)
            if bdl.ui.paramTurboSpin.value() != 100:
                bdl.ui.paramTurboCheck.setChecked(True)



def saveConfig(bdl, file="bdl.ini"):       # TODO: add md5 check here? might not save time
    config = configparser.ConfigParser()
    config['bdl.general'] = {}
    general = config['bdl.general']
    general['lastdir'] = bdl.lastDir
    general['autoclose'] = str(bdl.ui.bdlAutoClose.isChecked())
    general['capilization'] = str(bdl.ui.bdlCapitalization.isChecked())
    general['capilizationindex'] = str(bdl.ui.bdlCapitalizationCombo.currentIndex())
    general['detectiwads'] = str(bdl.ui.bdlDetectIWADs.isChecked())
    general['rejectbadiwads'] = str(bdl.ui.bdlRejectBadIWADs.isChecked())
    general['pwadscheckable'] = str(bdl.ui.bdlPWADsCheckable.isChecked())
    general['autocheckupdates'] = str(bdl.ui.bdlAutoUpdateCheck.isChecked())
    general['lastupdatecheck'] = bdl.ui.bdlUpdateLastCheckLabel.text()
    general['updateready'] = str(bdl.ui.bdlUpdateButton.isEnabled())

    general['windowpos'] = str(bdl.window.x()-1) + ',' + str(bdl.window.y()-31)   # -1 and -31 due to strage offset
    general['windowsize'] = str(bdl.ui.centralwidget.frameGeometry().width()) + ',' + str(bdl.ui.centralwidget.frameGeometry().height())
    general['lastsplittersize'] = ','.join(str(size) for size in bdl.ui.splitter.sizes())

    config['bdl.save'] = {}
    save = config['bdl.save']
    save['extra'] = bdl.ui.parameterLineEdit.text()
    save['portindex'] = str(bdl.ui.portCombo.currentIndex())
    save['iwadindex'] = str(bdl.ui.iwadList.currentRow())
    save['complevelindex'] = str(bdl.ui.complevelCombo.currentIndex())
    save['demoenabled'] = str(bdl.ui.demoGroup.isChecked())
    save['demorecord'] = str(bdl.ui.demoRecordRadio.isChecked())
    save['demorecordname'] = bdl.ui.demoRecordNameLineEdit.text()
    save['demoplay'] = str(bdl.ui.demoPlayRadio.isChecked())
    save['demoplaypath'] = bdl.ui.demoPlayPathLineEdit.text()
    save['demoautorecord'] = str(bdl.ui.demoAutoRecordCheck.isChecked())
    save['demolongtics'] = str(bdl.ui.demoLongTicsCheck.isChecked())
    save['warpenabled'] = str(bdl.ui.warpGroup.isChecked())
    save['warp'] = str(bdl.ui.warpMapCombo.currentIndex())
    save['skill'] = str(bdl.ui.warpSkillCombo.currentIndex()+1)   # +1 to negate the -1 in loadConfig()

    config['bdl.moreparameters'] = {}
    params = config['bdl.moreparameters']
    params['showmoreparameters'] = str(bdl.ui.paramGroup.isChecked())
    params['fast'] = str(bdl.ui.paramFast.isChecked())
    params['respawn'] = str(bdl.ui.paramRespawn.isChecked())
    params['solo-net'] = str(bdl.ui.paramSoloNet.isChecked())
    params['levelstat'] = str(bdl.ui.paramLevelStat.isChecked())
    params['nomonsters'] = str(bdl.ui.paramNoMonsters.isChecked())
    params['nosound'] = str(bdl.ui.paramNoSound.isChecked())
    params['nomusic'] = str(bdl.ui.paramNoMusic.isChecked())
    params['nosfx'] = str(bdl.ui.paramNoSFX.isChecked())
    params['turbo'] = str(bdl.ui.paramTurboSpin.value())

    # loop through file widgets and save all wads/ports and their properties
    config['bdl.iwads'] = {}
    config['bdl.pwads'] = {}
    config['bdl.ports'] = {}
    for i, iwad in enumerate(bdl.getListWidgetItems(bdl.ui.iwadList)):
        config['bdl.iwads'][f'iwadname{i}'] = iwad.text()
        config['bdl.iwads'][f'iwadpath{i}'] = iwad.data(3)
        config['bdl.iwads'][f'iwadwarp{i}'] = str(iwad.data(4)[0])
    for i, pwad in enumerate(bdl.getListWidgetItems(bdl.ui.pwadList)):
        config['bdl.pwads'][f'pwadchecked{i}'] = 'True' if pwad.checkState() == 2 else 'False'
        config['bdl.pwads'][f'pwadpath{i}'] = pwad.data(3)
    for i in range(bdl.ui.portCombo.count()):
        config['bdl.ports'][f'portname{i}'] = bdl.ui.portCombo.itemText(i)
        config['bdl.ports'][f'portpath{i}'] = bdl.ui.portCombo.itemData(i,3)

    # Save ini file
    with open(file, 'w') as ini:
        config.write(ini)



def findSteamIWADs(bdl):
        # TODO: add heretic, hexen, strife
        # TODO: move 64-bit check + OS check to ini file
        # TODO: cross-platform support
        currentOS = platform.system()
        is64bit = platform.machine().endswith("64")

        if currentOS != 'Windows':  # don't even bother if not on windows, this won't work yet
            return

        # 64/32-bit Windows paths to each of the main Doom IWADs
        programFilesDir = "%PROGRAMFILES(X86)%" if is64bit else "%PROGRAMFILES%"
        steamIWADPaths = (programFilesDir + r"\Steam\steamapps\common\Ultimate Doom\base\DOOM.WAD",
                        programFilesDir + r"\Steam\steamapps\common\Doom 2\base\DOOM2.WAD",
                        programFilesDir + r"\Steam\steamapps\common\Final Doom\base\TNT.WAD",
                        programFilesDir + r"\Steam\steamapps\common\Final Doom\base\PLUTONIA.WAD",)

        try: os.mkdir(r".\IWADs")       # attempt to create IWADs directory
        except FileExistsError: pass

        # attempt to copy Master Levels wads to separate directory inside IWADs
        # NOTE: if the directory already exists and is not empty, no wads will be copied.
        if not os.path.isdir(r".\IWADs\Master Levels"):
            try: shutil.copytree(os.path.expandvars(programFilesDir + r"\Steam\steamapps\common\Master Levels of Doom\master\wads"),
                                r".\IWADs\Master Levels")
            except FileNotFoundError: pass

        for path in steamIWADPaths:         # attempts to find and copy each IWAD to IWADs folder
            wad = path.split("\\")[-1]      # wad's filename -> DOOM2.WAD, TNT.WAD, etc.
            if not os.path.exists(f".\\IWADs\\{wad}"):      # only copy if file is not present
                try: shutil.copy(os.path.expandvars(path), r".\IWADs")
                except: continue

        # TODO: master levels check
        # adds each found iwad to iwad list

        # if iwads not empty, sort .wad files from ultimate doom to plutonia, then add each
        iwadDir = os.listdir(r".\IWADs")
        if iwadDir:
            # create list of absolute paths to each file in .\IWADs that ends in .wad (to ignore Master Levels)
            files = list(os.path.abspath(r".\IWADs") + "\\" + file for file in iwadDir if file.lower().endswith(".wad"))
            sortedFiles = []
            wadPriority = ('DOOM.WAD', 'DOOM2.WAD', 'TNT.WAD', 'PLUTONIA.WAD')
            for wad in wadPriority:
                wadPath = os.path.abspath(r".\IWADs") + "\\" + wad
                if wadPath in files:
                    sortedFiles.append(wadPath.replace("\\", "/"))
            bdl.addFile(bdl.ui.iwadList, files=sortedFiles)
        else:
            os.rmdir(r".\IWADs")    # delete directory if it's empty
        bdl.ui.iwadList.setCurrentRow(0)     # selects first iwad (usually ultimate doom)


def firstTimeSetup(bdl):
    #if os.path.exists("%APPDATA%\\Vectec Software\\qZDL.ini"):
    #    pass        # TODO: s t e a l ZDL's config
    findSteamIWADs(bdl)