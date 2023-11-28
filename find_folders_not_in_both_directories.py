import os

directory_1=r'C:\Users\Liqaa Arttouch\Desktop\chrismtas products tamata'
directory_2=r'C:\Users\Liqaa Arttouch\Desktop\New folder (2)'

directories_not_in_both=set(os.listdir(directory_1))^set(os.listdir(directory_2))

for i in directories_not_in_both:
    print(i)
