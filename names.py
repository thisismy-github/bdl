# TODO: ACTUAL map names... feelsbadman
mapsDoomShareware = (1,'E1M1','E1M2','E1M3','E1M4','E1M5','E1M6','E1M7','E1M8','E1M9')

mapsDoomRegistered = (2,'E1M1','E1M2','E1M3','E1M4','E1M5','E1M6','E1M7','E1M8','E1M9',
                        'E2M1','E2M2','E2M3','E2M4','E2M5','E2M6','E2M7','E2M8','E2M9',
                        'E3M1','E3M2','E3M3','E3M4','E3M5','E3M6','E3M7','E3M8','E3M9')

mapsDoomUltimate = (3,'E1M1','E1M2','E1M3','E1M4','E1M5','E1M6','E1M7','E1M8','E1M9',
                      'E2M1','E2M2','E2M3','E2M4','E2M5','E2M6','E2M7','E2M8','E2M9',
                      'E3M1','E3M2','E3M3','E3M4','E3M5','E3M6','E3M7','E3M8','E3M9',
                      'E4M1','E4M2','E4M3','E4M4','E4M5','E4M6','E4M7','E4M8','E4M9')

mapsDoom2 = (4,'MAP01','MAP02','MAP03','MAP04','MAP05','MAP06','MAP07','MAP08',
               'MAP09','MAP10','MAP11','MAP12','MAP13','MAP14','MAP15','MAP16',
               'MAP17','MAP18','MAP19','MAP20','MAP21','MAP22','MAP23','MAP24',
               'MAP25','MAP26','MAP27','MAP28','MAP29','MAP30','MAP31','MAP32')

mapsHeretic = (5,'E1M1','E1M2','E1M3','E1M4','E1M5','E1M6','E1M7','E1M8','E1M9',
                 'E2M1','E2M2','E2M3','E2M4','E2M5','E2M6','E2M7','E2M8','E2M9',
                 'E3M1','E3M2','E3M3','E3M4','E3M5','E3M6','E3M7','E3M8','E3M9',
                 'E4M1','E4M2','E4M3','E4M4','E4M5','E4M6','E4M7','E4M8','E4M9',
                 'E5M1','E5M2','E5M3','E5M4','E5M5','E5M6','E5M7','E5M8','E5M9',
                 'E6M1','E6M2','E6M3')

mapNumberStyles = (None,mapsDoomShareware,mapsDoomRegistered,mapsDoomUltimate,mapsDoom2,mapsHeretic)

# TODO: chocolate-doom-setup.exe? doom 64 ex launcher.exe? zdaemon zlauncher.exe? normal prboom?
# TODO: more ports + exceptions (ZDL, Doom Builder, etc.)?
# TODO: ordereddicts?
portNames = {'prboom-plus.exe':'PrBoom+',
             'glboom-plus.exe':'GLBoom+',
             'chocolate-doom.exe':'Chocolate Doom',
             'chocolate-heretic.exe':'Chocolate Heretic',
             'chocolate-hexen.exe':'Chocolate Hexen',
             'chocolate-strife.exe':'Chocolate Strife',
             'crispy-doom.exe':'Crispy Doom',
             'crispy-heretic.exe':'Crispy Heretic',
             'crispy-hexen.exe':'Crispy Hexen',
             'crispy-strife.exe':'Crispy Strife',
             'cndoom.exe':'Competition Doom',
             'cnheretic.exe':'Competition Heretic',
             'cnhexen.exe':'Competition Hexen',
             'cnstrife.exe':'Competition Strife',
             'doomretro.exe':'Doom Retro',
             'dosbox.exe':'DOSBox Doom',
             'DOOM64.EXE':'Doom 64 EX',
             'bd64.exe':'Brutal Doom 64',
             'zdoom.exe':'ZDoom',
             'gzdoom.exe':'GZDoom',
             'qzdoom.exe':'QZDoom',
             'zandronum.exe':'Zandronum',
             'doomseeker.exe':'Doomseeker',
             'odamex.exe':'Odamex',
             'odalaunch.exe':'Odamex Launcher',
             'zdaemon.exe':'ZDaemon',
             'zlauncher.exe':'ZDaemon Launcher',
             'skulltag.exe':'Skulltag'
             }

# TODO: optional "extended" name search mode? swappable II and 2? "speed" mode? do something about strife VOICES.wad?
# add Doom 64 (if possible), freedoom 1 and 2, adventures of square,
# rise of the wool ball, strife VE (if different), and NRTFL!!!!!!!!!
iwadNames = {'f0cefca49926d00903cf57551d901abe':('Shareware Doom', mapsDoomShareware),
             '90facab21eede7981be10790e3f82da2':('Shareware Doom v1.0', mapsDoomShareware),
             'cea4989df52b65f4d481b706234a3dca':('Shareware Doom v1.1', mapsDoomShareware), # 12/15/93
             '52cbc8882f445573ce421fa5453513c1':('Shareware Doom v1.1', mapsDoomShareware), # 12/16/93
             '30aa5beb9e5ebfbbe1e1765561c08f38':('Shareware Doom v1.2', mapsDoomShareware),
             '17aebd6b5f2ed8ce07aa526a32af8d99':('Shareware Doom v1.25', mapsDoomShareware),
             'a21ae40c388cb6f2c3cc1b95589ee693':('Shareware Doom v1.4', mapsDoomShareware),
             'e280233d533dcc28c1acd6ccdc7742d4':('Shareware Doom v1.5', mapsDoomShareware),
             '762fd6d4b960d4b759730f01387a50a1':('Shareware Doom v1.6', mapsDoomShareware),
             'c428ea394dc52835f2580d5bfd50d76f':('Shareware Doom v1.666', mapsDoomShareware),
             '5f4eb849b1af12887dec04a2a12e5e62':('Shareware Doom v1.8', mapsDoomShareware),
             '1cd63c5ddff1bf8ce844237f580e9cf3':('Registered Doom', mapsDoomRegistered),
             '981b03e6d1dc033301aa3095acc437ce':('Registered Doom v1.1', mapsDoomRegistered),
             '792fd1fea023d61210857089a7c1e351':('Registered Doom v1.2', mapsDoomRegistered),
             '54978d12de87f162b9bcc011676cb3c0':('Registered Doom v1.666', mapsDoomRegistered),
             '11e1cd216801ea2657723abc86ecb01f':('Registered Doom v1.8', mapsDoomRegistered),
             'c4fe9fd920207691a9f493668e0a2083':('Ultimate Doom', mapsDoomUltimate),
             'fb35c4a5a9fd49ec29ab6e900572c524':('Ultimate Doom (BFG Edition)', mapsDoomUltimate),
             '7912931e44c7d56e021084a256659800':('Ultimate Doom (Xbox 360 BFG Edition)', mapsDoomUltimate),
             '72286ddc680d47b9138053dd944b2a3d':('Ultimate Doom (XBLA)', mapsDoomUltimate),
             '0c8758f102ccafe26a3040bee8ba5021':('Ultimate Doom (Xbox)', mapsDoomUltimate),
             'e4f120eab6fb410a5b6e11c947832357':('Ultimate Doom (PSN)', mapsDoomUltimate),
             '232a79f7121b22d7401905ee0ee1e487':('Ultimate Doom (Nintendo Switch)', mapsDoomUltimate),
             '3e410ecd27f61437d53fa5c279536e88':('Doom for Pocket PC',),
             '25e1459ca71d321525f84628f45ca8cd':('Doom II', mapsDoom2),
             '3cb02349b3df649c86290907eed64e7b':('Doom II Français', mapsDoom2),  # AKA v1.8f
             'c3bea40570c23e511a7ed3ebcd9865f7':('Doom II (BFG Edition)', mapsDoom2),
             'f617591a6c5d07037eb716dc4863e26b':('Doom II (Xbox 360 BFG Edition)', mapsDoom2),
             '43c2df32dc6c740cb11f34dc5ab693fa':('Doom II (XBLA)', mapsDoom2),
             'a793ebcdd790afad4a1f39cc39a893bd':('Doom II (Xbox)', mapsDoom2),
             '4c3db5f23b145fccd24c9b84aba3b7dd':('Doom II (PSN)', mapsDoom2),
             'e7395bd5e838d58627bd028871efbc14':('Doom II (Nintendo Switch)', mapsDoom2),
             '9640fc4b2c8447bbd28f2080725d5c51':('Doom II for the Tapwave Zodiac', mapsDoom2),
             'd9153ced9fd5b898b36cc5844e35b520':('Doom II v1.666g', mapsDoom2),
             '30e3c2d0350b67bfbf47271970b74b2f':('Doom II v1.666', mapsDoom2),
             'ea74a47a791fdef2e9f2ea8b8a9da13b':('Doom II v1.7', mapsDoom2),
             'd7a07e5d3f4625074312bc299d7ed33f':('Doom II v1.7a', mapsDoom2),
             'c236745bb01d89bbb866c8fed81b6f8c':('Doom II v1.8', mapsDoom2),
             '4e158d9953c79ccf97bd0663244cc6b6':('TNT: Evilution', mapsDoom2),   # original bugged map31 version TODO: add warning
             '1d39e405bf6ee3df69a8d2646c8d5c49':('TNT: Evilution', mapsDoom2),
             'be626c12b7c9d94b1dfb9c327566b4ff':('TNT: Evilution (PSN)', mapsDoom2),
             '75c8cf89566741fa9d22447604053bd7':('Plutonia Experiment', mapsDoom2),  # missing dm starts TODO: warning?
             '3493be7e1e2588bc9c8b31eab2587a04':('Plutonia Experiment', mapsDoom2),
             'b77ca6a809c4fae086162dad8e7a1335':('Plutonia Experiment (PSN)', mapsDoom2),
             'ae779722390ec32fa37b0d361f7d82f8':('Shareware Heretic', mapsDoomShareware),
             '023b52175d2f260c3bdc5528df5d0a8c':('Shareware Heretic v1.0', mapsDoomShareware),
             'fc7eab659f6ee522bb57acc1a946912f':('Shareware Heretic Beta', mapsDoomShareware),
             '66d686b1ed6d35ff103f15dbd30e0341':('Heretic', mapsHeretic),  # v1.3 -> shadow of the serpent riders),
             '3117e399cdb4298eaa3941625f4b2923':('Registered Heretic v1.0', mapsDoomRegistered),
             '1e4cb4ef075ad344dd63971637307e04':('Registered Heretic', mapsDoomRegistered),
             'abb033caf81e26f12a2103e1fa25453f':('Hexen',),
             'c88a2bb3d783e2ad7b599a8e301e099e':('Hexen Beta',),
             'b2543a03521365261d0a0f74d5dd90f0':('Hexen v1.0',),
             '876a5a44c7b68f04b3bb9bc7a5bd69d6':('Hexen Demo',),
             '9178a32a496ff5befebfe6c47dac106c':('Hexen Demo Beta',),
             'b68140a796f6fd7f3a5d3226a32b93be':('Hexen (Mac)',),
             '925f9f5000e17dc84b0a6a3bed3a6f31':('Hexen Demo (Mac)',),
            #'78d5898e99e220e4de64edaa0e479593':('Hexen: Deathkings of the Dark Citadel',),    # bugged steam version TODO: add warning
            #'1077432e2690d390c256ac908b5f4efa':('Hexen: Deathkings of the Dark Citadel v1.0',),   # NOT iwads TODO: add warning
             'bb545b9c4eca0ff92c14d466b3294023':('Strife Demo',),
             'de2c8dcad7cca206292294bdab524292':('Strife Demo v1.0',),
             '2fed2031a5b03892106e0f117f17901f':('Strife',),
             '8f2d3a6a289f5d2f2f9c1eec02b47299':('Strife v1.1',),
             '25485721882b050afa96a56e5758dd52':('Chex Quest',),
             'bce163d06521f9d15f9686786e64df13':('Chex Quest 3',),
             '59c985995db55cd2623c1893550d82b3':('Chex Quest 3 v1.0',),
             '65ed74d522bdf6649c2831b13b9e02b4':('Hacx',),
             'b7fd2f43f3382cf012dc6b097a3cb182':('Hacx v1.1',),
             '1511a7032ebc834a3884cf390d7f186e':('Hacx v1.0',),    # called "unverified" on wiki
             '402ca45bb90520bfef0dec6baac5889e':('Hacx v1.0',),    # called "verified" on wiki
             '793f07ebadb3d7353ee5b6b6429d9afa':('Hacx 2.0','Hacx 2'),
             }
# TODO: partial md5 for massive performance gain? maybe?


# TODO: Actual IWAD titles are unused currently. Only the map lists are used. Unfinished.
iwadNamesSimple = {
    'doom1.wad':('Shareware Doom', mapsDoomShareware),
    'doom.wad':('Ultimate Doom', mapsDoomUltimate),     # could also be registered doom
    'doomu.wad':('Ultimate Doom', mapsDoomUltimate),
    'doom2.wad':('Doom II', mapsDoom2),
    'doom2f.wad':('Doom II Français', mapsDoom2),
    'tnt.wad':('TNT: Evilution', mapsDoom2),
    'tnt31.wad':('TNT: Evilution', mapsDoom2),
    'plutonia.wad':('Plutonia Experiment', mapsDoom2),
    'heretic1.wad':('Shareware Heretic', mapsDoomShareware),
    'heretic.wad':('Heretic', mapsHeretic)
}