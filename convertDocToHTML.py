import mammoth
import os
import shutil
import zipfile


def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]
 
def main():
    path = os.getcwd()
    print(path)
    originalPath = f"{path}/test1"
    destinationPath = f"{path}/test2"
    copyDirectory(originalPath, destinationPath)
    for subdir, dirs, files in os.walk(originalPath):
        for file in files:
            currFilePath =(os.path.join(subdir, file))
            fileName = file.split('.')[0]
            if(file):
                createHtml(currFilePath, path, fileName)

def copyDirectory(src, dest):
    if(os.path.exists(dest)):
        shutil.rmtree(dest)
    shutil.copytree(src, dest, ignore=ignore_files)

def createHtml(textFilePath, path, name):
    if(zipfile.is_zipfile(textFilePath)):
        f = open(textFilePath, 'rb')
        b = open(f"{path}/test2/{name}.html", 'wb')
        document = mammoth.convert_to_html(f)
        b.write(document.value.encode('utf8'))
        f.close()
        b.close()




main()
