import os
from PIL import Image
from datetime import datetime


path = 'c:/Users/artem/Desktop/New Archive/2021.05.05-09 Ponga new'
os.chdir(path)

##Read files in the specified directory
files = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))

# ## Fix up the erros in names
# for name in files:
#     if (name[0] == '_'):
#         new_name = 'DSC0' +name[4:8]+'.jpg'
#         os.rename(name, new_name)
        
##This is gona be a list of tupeles (name, time taken)
list_name_time = []

for name in files:
    time = Image.open(path+'/'+name).getexif()[36867]
    date_time = datetime.strptime(time, '%Y:%d:%m %H:%M:%S')
    exact_seconds = date_time.hour*60*60+date_time.minute*60+date_time.second
    list_name_time.append((name, exact_seconds))
    
## Go through the list we just created
i = 0
while (i < len(list_name_time)-4):
    
    ## Compute the time taken dif between the given file and next four files
    dif1  = list_name_time[i+1][1]-list_name_time[i][1]
    dif2  = list_name_time[i+2][1]-list_name_time[i][1]
    dif3  = list_name_time[i+3][1]-list_name_time[i][1]
    dif4  = list_name_time[i+4][1]-list_name_time[i][1]
    print (list_name_time[i][0], dif1, dif2, dif3, dif4)
    
    ##If they were created within 5 sec, move them to a seprate dir
    if (dif1<5 and dif2<5 and dif3<5 and dif4<5):
        dir_name = list_name_time[i][0][:8]
        os.makedirs(path+'/'+dir_name)
        for k in range (i, i+5):
            os.rename(list_name_time[k][0],dir_name+'/'+list_name_time[k][0])
        i = i+5
        continue
    i = i+1
    


    