import os
for subdir, dirs, files in os.walk('./'):
    for file in files:
        if ".csv" in file:
            statinfo = os.stat(file)
            if statinfo.st_size > 20000000:
                print "split -b 20m "+file+" "+file[:-4]
                os.system("split -b 20m "+file+" "+file[:-4]+"_")

for subdir, dirs, files in os.walk('./'):
    for file in files:
        if "." not in file:
            os.rename(file, file+".csv")


#for subdir, dirs, files in os.walk('./'):
#for files in os.walk('./'):
#    for file in files:
#        if ".csv" in file:
#            statinfo = os.stat(file)
#            if statinfo.st_size > 20000000:
#                print "split -b 20m "+file+" "+file[:-4]
#                os.system("split -b 20m "+file+" "+file[:-4]+"_")
#
#for files in os.walk('./'):
#    for file in files:
#        if "." not in file:
#            os.rename(file, file+".csv")
