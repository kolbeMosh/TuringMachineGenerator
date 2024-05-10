from PIL import Image
import os

class convertToGif:
    def __init__(self, SrcDir: str, DestDir: str, fileName: str, timePerFrame: int, optimize=True):
        self._SrcDir = SrcDir
        # self._DestDir = DestDir
        self._fileName = fileName
        self._imgPath = f'{DestDir}/{self._fileName}.gif'
        self._timePerFrame = timePerFrame
        self._fileList = self._getFilesInDir()
        self._imageArr = self._getImageObjs()
        self._optimize = optimize

    def _getFilesInDir(self):
        files = []
        dir = os.scandir(self._SrcDir)
        for file in dir:
            files.append(file.name)
        files.sort(key=lambda f: int(f.split('.')[0]))
        return files
    
    def _getImageObjs(self):
        arr = []
        for i in range(len(self._fileList)):
            arr.append(Image.open(f'{self._SrcDir}/{self._fileList[i]}'))
        return arr
    
    def convert(self):
        self._imageArr[0].save(self._imgPath, save_all=True, append_images=self._imageArr[1:], duration=self._timePerFrame, optimize=self._optimize, loop=0 )
        print(f'Successfully saved image to {self._imgPath}')