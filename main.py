import os
from PIL import Image
from datetime import datetime


path = 'c:/Users/artem/Desktop/New Archive/2021.05.05-09 Ponga'
os.chdir(path)


files = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))
list_name_time = []

for name in files:
    time = Image.open(path+'/'+name).getexif()[36867]
    date_time = datetime.strptime(time, '%Y:%d:%m %H:%M:%S')
    exact_seconds = date_time.hour*60*60+date_time.minute*60+date_time.second
    list_name_time.append((name, exact_seconds))
for i in range(len(list_name_time)-1):
    dif = list_name_time[i+1][1]-list_name_time[i][1]
    print(dif)


    