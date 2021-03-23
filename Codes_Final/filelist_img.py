import pandas as pd
import os

data_path='/home/dmachuve/Dropbox/AI4D_Dataset/rawImg/cocci'
listnames=os.listdir(data_path)  #list all the files in the directory
listnew=[i.split('.jpg',1)[0] for i in listnames] #remove the extension .jpg

listnamesdf=pd.DataFrame(listnew)
listnamesdf.to_csv('filelist_cocci.csv',index=False)