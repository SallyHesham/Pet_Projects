import os

filelist = os.listdir()
for file in filelist:
    if file.find('.png') != -1:
        if len(file) == 14:
            list = file.split('.')
            newname = list[0] + ' (00).png'
            os.rename(file, newname)
        elif len(file) == 18:
            list = file.split('(')
            newname = list[0] + '(0' + list[1]
            os.rename(file, newname)
    elif file.find('.jpg') != -1:
        if len(file) > 23:
            list = file.split('_')
            parts = list[1].split('-')
            newname = parts[0][0:4] + '-' + parts[0][4:6] + '-' + parts[0][6:8] + ' (' + parts[1] + ')' + '.jpg'
            os.rename(file, newname)

print('Done, master.')
