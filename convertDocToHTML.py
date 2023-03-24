import mammoth
import os
import shutil

def main():
    path = os.getcwd()
    originalPath = "f{path}/test1"
    destinationPath = "f{path}/test2"
    shutil.rmtree(destinationPath)

def createHtml(path, name):
    f = open("C:\\Users\\asilv\\Code\\UNSHUT\\misc\\Doc2Html\\test.docx", 'rb')
    b = open('filename.html', 'wb')
    document = mammoth.convert_to_html(f)
    b.write(document.value.encode('utf8'))
    f.close()
    b.close()


main()
