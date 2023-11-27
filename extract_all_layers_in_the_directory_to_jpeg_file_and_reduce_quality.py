import os
from photoshop import Session
import photoshop


app = photoshop.api.Application()

new_directory="D:/artouch_items_photos"
directories=[
'D:/02 -Artntouch Sama 2021/11 November 2021',
'D:/02 -Artntouch Sama 2021/12 December 2021',
'D:/03 -artouch social media 2022/01 January 2022',
'D:/03 -artouch social media 2022/02 February 2022',
'D:/03 -artouch social media 2022/03 March 2022',
'D:/03 -artouch social media 2022/04 April 2022',
'D:/03 -artouch social media 2022/05 May 2022',
'D:/03 -artouch social media 2022/06 June 2022',
'D:/03 -artouch social media 2022/07 July 2022',
'D:/03 -artouch social media 2022/08 August 2022',
'D:/03 -artouch social media 2022/09 September 2022',
'D:/03 -artouch social media 2022/10 October 2022',
'D:/03 -artouch social media 2022/11 November 2022',
'D:/03 -artouch social media 2022/12 December 2022',
'D:/03-Artouch Social media 2023/01-January 2023',
'D:/03-Artouch Social media 2023/02-February 2023',
'D:/03-Artouch Social media 2023/03-March 2023',
'D:/03-Artouch Social media 2023/04-April 2023',
'D:/03-Artouch Social media 2023/05-May 2023',
'D:/03-Artouch Social media 2023/06-June-2023',
'D:/03-Artouch Social media 2023/07 July 2023',
'D:/03-Artouch Social media 2023/08 August 2023',
'D:/03-Artouch Social media 2023/09 September 2023',
'D:/03-Artouch Social media 2023/10 October 2023',
]


def hide_all_layers(layers):
    for layer in layers:
        layer.visible = False


def extract_jpeg_file_from_layer_in_psd_file(psd_file_path,file):
    with Session(psd_file_path, action="open",auto_close=True) as ps:
        doc = ps.active_document
        options = ps.JPEGSaveOptions(quality=8)
        layers = doc.layers
        if len(layers)==0:
            return

        for layer in layers:
            try:
                if layer.name.lower() in ["copyrights","background","assets"]:
                    continue
                hide_all_layers(layers)
                layer.visible = True
                folder_path=new_directory+"/"+file+"/"
                file_name="layer_"+str(layers.index(layer))+".JPEG"
                image_path = folder_path+file_name
                print(image_path)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                doc.saveAs(image_path, options, True)
            except:
                print("this file is error\n"+psd_file_path)
        

i=0
is_ok_to_start=False
for directory in directories:
    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.psd'):
                i+=1
                psd_file_path=os.path.join(subdir, file)

                # if psd_file_path==r"D:/03-Artouch Social media 2023/09 September 2023\Sales Reel\Sales Reel.psd":
                #     is_ok_to_start=True
                #     continue

                # if is_ok_to_start==False:
                #     continue

                file_with_no_extantion = os.path.splitext(file)[0]
                print(f"========================={i}=========================")
                print(psd_file_path)
                extract_jpeg_file_from_layer_in_psd_file(psd_file_path,file_with_no_extantion)


Session.alert(app,"done")
Session.echo()
