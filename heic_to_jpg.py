import os
from wand.image import Image

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nMake sure you're HEIC image folder is EMPTY!\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
heic_image_path = input("Enter HEIC Image Path (Enter nothing for /Input) ") + "\\"
final_image_path = input("Enter Output Folder Path (Enter nothing for /Output): ") + "\\"
if final_image_path == "\\":
    final_image_path = "Output\\"

if heic_image_path == "\\":
    heic_image_path = "Input\\"

 
count = 0
for file in os.listdir(heic_image_path): #change to enumerate sometime idk
    count +=1
    source_file = heic_image_path + file
    print(source_file)
    if source_file.endswith("c"): #sometimes its lowercase heic, sometimes it's uppercase heic....
        final_file = final_image_path + file.replace(".heic", ".jpg")
    else: 
        final_file = final_image_path + file.replace(".HEIC", ".jpg")
    with Image(filename=source_file) as original:
        with original.convert('heic') as converted:
        #img.format = 'jpg'
            converted.save(filename=final_file)
    print("Converted " + file + " to JPG successfully!\nConversion #"+str(count))

