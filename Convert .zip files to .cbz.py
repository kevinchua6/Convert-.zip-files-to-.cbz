import os  
from os.path import join  
from shutil import copyfile

def convertzip(foldername):   
    if foldername.endswith('.zip'):
        try:
            copyfile(join(root_path, foldername), join(src_path, foldername))
            os.rename(foldername, foldername[:-4] + '.cbz' )
            print('Zipping '+ foldername[:-4])
        except FileExistsError:
            print('File already exists, going to the next one')
        

root_path = r'ROOT_DIRECTORY' #Directory with files to be zipped to .cbz
src_path = os.getcwd()

for root, dirs, files in os.walk(root_path):  
    for file in files:
        convertzip(file)