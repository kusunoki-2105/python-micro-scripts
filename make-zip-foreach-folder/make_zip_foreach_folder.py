import shutil
import os

def isDirectory(dirEntry):
    return dirEntry.is_dir() and not dirEntry.is_symlink()

def getDirEntryAtCurrentDirectory():
    return filter(isDirectory, os.scandir())

print('*****\n' + os.getcwd())
for dirEntry in getDirEntryAtCurrentDirectory():
    print("  " + dirEntry.name)
print('*****\n\nArchive these files.')
yesOrNo = input('Are you sure ? (y/n)')

if(yesOrNo == 'y'):
    print()
    for dirEntry in getDirEntryAtCurrentDirectory():
        print("Archiving \"" + dirEntry.name + "\"...")
        shutil.make_archive(dirEntry, 'zip', dirEntry)
