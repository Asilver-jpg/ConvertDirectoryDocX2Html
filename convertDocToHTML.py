import mammoth
import os
import shutil
import zipfile


def ignore_files(dir, files):
    return [f for f in files if os.path.isfile(os.path.join(dir, f))]


# This file when run will take the contents of the test1 directory, which should be a directory or .docx files or .docx files
# And copy the same file structure and their contents but in HTML. Upload the contents of test 2 to AWS

# Have test1 be the directory with all the .docx files. 
# Delete contents of test2 each time you run 
# TODO make it so that test2 deletes its sudirtectories on its own  
def main():
    path = os.getcwd()
    originalPath = f"{path}/test1"
    destinationPath = f"{path}/test2"
    copyDirectory(originalPath, destinationPath)
    for subdir, dirs, files in os.walk(originalPath):
        for file in files:
            currFilePath =(os.path.join(subdir, file))
            fileName = file.split('.')[0]
            if(file):
                inputPath = subdir.replace('test1', 'test2')
                inputPath = inputPath.replace('.docx','')
               
                print(inputPath)
                createHtml(currFilePath, inputPath, fileName)

def copyDirectory(src, dest):
    if(os.path.exists(dest)):
        shutil.rmtree(dest)
    shutil.copytree(src, dest, ignore=ignore_files)

def createHtml(textFilePath, path, name):
    print(path)

    if(zipfile.is_zipfile(textFilePath)):
        f = open(textFilePath, 'rb')
        b = open(f"{path}/{name}.html", 'wb')
        document = mammoth.convert_to_html(f)
        b.write(document.value.encode('utf8'))
        f.close()
        b.close()




main()
