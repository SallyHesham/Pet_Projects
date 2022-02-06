import os

filelist = os.listdir()
for file in filelist:
    if file.find('.png') != -1:
        if len(file) > 30:
            listfull = file.split()
            listsmall = listfull[2].split("_")
            if len(listsmall[0]) > 2: continue
            newname = listfull[0] + " " + listfull[1] + " " + listsmall[2] + "_" + \
            listsmall[0] + "_" + listsmall[1] + " " + listfull[3] + " " + listfull[4]
            os.rename(file, newname)

print('Done, master.')
