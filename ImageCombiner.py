from PIL import Image
import os
from os import listdir

#go through each file and combine each attribute with each other
backgrounds = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut\Backgrounds"
bodies = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut\Bodies"
hair = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut\Hair"
tail = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut\Tail"
tattoo = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut\Tattoo"
wings = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut\Wings"
horn = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut\Horn"
finalImages = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut\Blessings"
images = []

for i in range(len(os.listdir(r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut"))-2):
    images.append("")
    


bCounter = 1


for background in os.listdir(backgrounds):
    #counter = 0
    images[0] = Image.open(backgrounds + "/" + background).convert("RGBA")
    #print("background is saved at index " + str(counter))
    #counter += 1

    for body in os.listdir(bodies):
        images[1] = Image.open(bodies + "/" + body).convert("RGBA")
        #counter += 1
        for h in os.listdir(hair):

            images[2] = Image.open(hair + "/" + h).convert("RGBA")
            #counter += 1
            for t in os.listdir(tail):

                images[3] = Image.open(tail + "/" + t).convert("RGBA")
                #counter += 1
                for tat in os.listdir(tattoo):

                    images[4] = Image.open(tattoo + "/" + tat).convert("RGBA")
                    #counter += 1
                    for wing in os.listdir(wings):

                        images[5] = Image.open(wings + "/" + wing).convert("RGBA")
                        final_image = images[0]
                        for h in os.listdir(horn):
                            images[6] = Image.open(horn + "/" + h).convert("RGBA")
                            for i in range(1,len(images)):
                                print(i)
                                final_image = Image.alpha_composite(final_image,images[i])
                            final_image.save(finalImages + "/Blessing_"+str(bCounter)+".png")
                            bCounter += 1
                        






