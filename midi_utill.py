def test(val):
    print(val)

def isMidiFile(file):
    import re
    pattern = '(\w|\W)*.mid'
    repattern = re.compile(pattern)
    return repattern.match(file)


def getMidiFileNames(fileDir):
    import glob
    import re
    import os
    import mido
    
    midiFiles = []
    fileDirs = []
    fileDirs.append(fileDir + '/**/*.mid')
    fileDirs.append(fileDir + '/**/*.MID')
    
    for pattern in fileDirs:
        for result in glob.glob(pattern, recursive=True):
            midiFiles.append(result)
        
    return midiFiles

# 本当はmidifileのチェックがisMidiFile()で出来るならやるべきなんだが、拡張子しかみてない様子、、
#     
#     for midiFile in glob.glob(fileDir, recursive=True):
#         if isMidiFile(midiFile):
#             midiFiles.append(midiFile)
            
#     return midiFiles

#     return glob.glob(fileDir, recursive=True)
    
def getDirList(fileDir):
    import glob
    import re
    import os
    
    fileDir = fileDir + '/**/' 
    return glob.glob(fileDir)
    

# def isMidiFileName(files):
        
#     midiFiles = []
    
#     for file in files:
#         result = isMidiFile(file)
#         if result:
#             midiFiles.append(file)
            
#     return midiFiles

def getMidiHexData(midifilename):
    import mido
    midi = mido.MidiFile(midifilename)
    MidiData = []
    for i in range(len(midi.tracks)):
        for msg in midi.tracks[i]:
#             print(msg.hex())
            MidiData.append(msg.hex())
    
    return MidiData

def isGM(midifilename):
    import re
    pattern = 'F0 7E \w\w 09'
    repattern = re.compile(pattern)
    
    for hexData in getMidiHexData(midifilename):
        if repattern.match(hexData):
            return True
            break
    
    return False
    
    

def isGS(midifilename):
    import re
    pattern = 'F0 41 \w\w 42'
    repattern = re.compile(pattern)
    
    for hexData in getMidiHexData(midifilename):
        if repattern.match(hexData):
            return True
            break
    
    return False

def isXG(midifilename):
    import re
    pattern = 'F0 43 \w\w 4C'
    repattern = re.compile(pattern)
    
    for hexData in getMidiHexData(midifilename):
        if repattern.match(hexData):
            return True
            break
            
    return False

def isGMGSXG(midifilename):
    if isGM(midifilename):
        return True
    elif isGS(midifilename):
        return True
    elif isXG(midifilename):
        return True
    else:
        return False
        


def escapeChar(char):
    char = char.translate(str.maketrans({'[': '[[]', ']': '[]]', '*': '[*]', '?': '[?]'}))
    return char

