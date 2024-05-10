# Written By: Kolbe Mosher
# Purpose: Produces an Animated Gif of a turing
#          Machine passed as an arg when validating 
#          a string passed as an arg
# Usage:   python main.py [TMFile] [TestInput]

from convertToGif import convertToGif as CTG
from univTM import UniversalTuringMachine as UTM
from TMtoDot import TMtoDot as TD
from currentTime import currentTime
import sys
import os

def main() -> bool:
    # UnivTM props
    TMDestDir = f'InterMediateFiles/{currentTime()}'
    TMFile = sys.argv[1]
    TMInput = sys.argv[2]

    # Output from UnivTM
    TMOutput = None
    TMAccepted = None # Whether the TM accepted the input or not
    movesMade = None # List of moves made by the TM

    # 
    gifDestDir = f'Renders/animated'
    staticDestDir = f'Renders/static'

    # Mostly not necessary(bc destDir is based on time) 
    # but might help prevent runtime errors ¯\_(ツ)_/¯
    if not os.path.exists(TMDestDir):
        os.makedirs(TMDestDir)

    TM = UTM(TMFile)

    TMOutput = TM.accepts(TMInput)

    TMAccepted = TMOutput[0]
    movesMade = TMOutput[1]

    # Uncomment this line to generate a static version of the file
    # you can change the filetype to any Pillow supported type 
    # supported types: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html
    TD(movesMade[0][0], str(currentTime()), staticDestDir, 'svg')

    # Generates Intermediate State Files
    for move in movesMade:
        TD(move[0], move[1], TMDestDir, 'png', move[2])

    CTG(TMDestDir, gifDestDir, str(currentTime()), 1000).convert()

    # Deletes Intermediate files to clean up space
    dir = os.scandir(TMDestDir)
    for file in dir:
        os.remove(file)
    os.rmdir(TMDestDir)


    return TMAccepted

main()
