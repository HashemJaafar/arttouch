import os

directory=r'C:\Users\Liqaa Arttouch\Desktop\item_photos_folder\Throw Pillows - New 2023'

os.listdir(directory)

l=[]
for i in os.listdir(directory):
    l.append(i)

l.sort()
for i in l:
    print(i)