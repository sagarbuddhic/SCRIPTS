#! /usr/bin/python
import shutil
import os
print("Starting")


depth = 2
sourceDirectory = "../../Source/"
folderToBeRemoved = "example_folder"

for root, dirs, files in os.walk(sourceDirectory):
    if root[len(sourceDirectory):].count(os.sep) < depth:
        for name in dirs:
            if name == folderToBeRemoved:
                shutil.rmtree(os.path.join(root, name), ignore_errors=True)
                print('Removing: ', os.path.join(root, name))
print('end')
