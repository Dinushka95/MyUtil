import os
import sys

CurrentExtention = sys.argv[1] 
NewExtention = sys.argv[2] 

for filename in os.listdir(os.getcwd()):
    #print(filename)
    if(filename.endswith(NewExtention)):
        continue
    else:
        if ( CurrentExtention in filename ):
            #print (filename + " = FOUND" )
            # Check extention
            try:
                os.rename(filename,filename+NewExtention)
                print(filename + " = Sucessfully Renamed")
            except:
                print("Failed to Rename")
        else:
            continue