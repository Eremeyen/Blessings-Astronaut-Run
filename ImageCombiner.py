from PIL import Image
import os
from os import listdir
from random import random

#attribute folders:
backgrounds = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Backgrounds"
bodies = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Bodies"
hair = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Hair"
tail = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Tail"
tattoo = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Tattoo"
front_wings = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Front_Wings"
back_wings = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Back_Wings"
horn = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Horn"
eyes = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Eye"
helmets = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Helmet"

#final images destination
finalImages = r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run\Blessings"

#defining an empty images array which we'll use to come up with each final image
images = []
for i in range(len(os.listdir(r"C:\Users\meren\OneDrive\Masaüstü\Blessings Astronaut Rarity Test Run"))-3):
    images.append("")




bCounter = 1

def whichBackground():
    n = random()
    if(n < 0.06):
        return "ASTRONAUT COLOUR BACKGROUND 1.png"
    elif(n < 0.12):
        return "ASTRONAUT COLOUR BACKGROUND 2.png"
    elif(n < 0.18):
        return "ASTRONAUT COLOUR BACKGROUND 3.png"
    elif(n < 0.24):
        return "ASTRONAUT COLOUR BACKGROUND 4.png"
    elif(n < 0.30):
        return "ASTRONAUT COLOUR BACKGROUND 5.png"
    elif(n < 0.36):
        return "ASTRONAUT COLOUR BACKGROUND 6.png"
    elif(n < 0.42):
        return "ASTRONAUT COLOUR BACKGROUND 7.png"
    elif(n < 0.48):
        return "ASTRONAUT COLOUR BACKGROUND 8.png"
    elif(n < 0.54):
        return "ASTRONAUT COLOUR BACKGROUND 9.png"
    elif(n < 0.60):
        return "ASTRONAUT COLOUR BACKGROUND 10.png"
    elif(n < 0.64):
        return "ASTRONAUT GRADIENT BACKGROUND 1.png"
    elif(n < 0.68):
        return "ASTRONAUT GRADIENT BACKGROUND 2.png"
    elif(n < 0.72):
        return "ASTRONAUT GRADIENT BACKGROUND 3.png"
    elif(n < 0.76):
        return "ASTRONAUT GRADIENT BACKGROUND 4.png"
    elif(n < 0.80):
        return "ASTRONAUT GRADIENT BACKGROUND 5.png"
    elif(n < 0.84):
        return "ASTRONAUT GRADIENT BACKGROUND 6.png"
    elif(n < 0.88):
        return "ASTRONAUT GRADIENT BACKGROUND 7.png"
    elif(n < 0.91):
        return "ASTRONAUT GRADIENT BACKGROUND 8.png"
    elif(n < 0.94):
        return "ASTRONAUT GRADIENT BACKGROUND 9.png"
    elif(n < 0.95):
        return "ASTRONAUT RARE BACKGROUND 1.png"
    elif(n < 0.96):
        return "ASTRONAUT RARE BACKGROUND 2.png"
    elif(n < 0.97):
        return "ASTRONAUT RARE BACKGROUND 3.png"
    elif(n < 0.98):
        return "ASTRONAUT RARE BACKGROUND 4.png"
    elif(n < 0.99):
        return "ASTRONAUT RARE BACKGROUND 5.png"
    else:
        return "ASTRONAUT RARE BACKGROUND 6.png"
    
def whichBackWing():
    n = random()
    if(n < 0.21):
        return "BACK WING 1.png"
    elif(n < 0.42):
        return "BACK WING 1.png"
    elif(n < 0.62):
        return "BACK WING 1.png"
    elif(n < 0.82):
        return "BACK WING 1.png"
    elif(n < 0.88):
        return "RARE BACK WING 1.png"
    elif(n < 0.94):
        return "RARE BACK WING 2.png"
    else:
        return "RARE BACK WING 3.png"
def whichTail():
    n = random()
    if(n < 0.25):
        return "ASTRONAUT TAIL 1.png"
    elif(n < 0.5):
        return "ASTRONAUT TAIL 2.png"
    elif(n < 0.75):
        return "ASTRONAUT TAIL 3.png"
    elif(n < 0.875):
        return "RARE TAIL 1.png"
    else:
        return "RARE TAIL 2.png"

def whichBody():
    n = random()
    if(n < 0.25):
        return "ASTRONAUT BODY 1.png"
    elif(n < 0.5):
        return "ASTRONAUT BODY 1.png"
    elif(n < 0.75):
        return "ASTRONAUT BODY 1.png"
    elif(n < 0.875):
        return "ASTRONAUT RARE BODY 1.png"
    else:
        return "ASTRONAUT RARE BODY 2.png"
def whichEye():
    n = random()
    if(n < 0.09):
        return "ASTRONAUT EYE F1.png"
    elif(n < 0.18):
        return "ASTRONAUT EYE F2.png"
    elif(n < 0.27):
        return "ASTRONAUT EYE F3.png"
    elif(n < 0.36):
        return "ASTRONAUT EYE F4.png"
    elif(n < 0.52):
        return "ASTRONAUT EYE M1.png"
    elif(n < 0.68):
        return "ASTRONAUT EYE M2.png"
    elif(n < 0.84):
        return "ASTRONAUT EYE M3.png"
    else:
        return "ASTRONAUT EYE M4.png"

def whichTattoo():
    n = random()
    if(n < 0.025):
        return "ASTRONAUT TATTOO 1.png"
    elif(n < 0.05):
        return "ASTRONAUT TATTOO 2.png"
    elif(n < 0.075):
        return "ASTRONAUT TATTOO 3.png"
    elif(n < 0.1):
        return "ASTRONAUT TATTOO 4.png"
    else:
        #no tattoo, reminder: add empty image to tattoo folder
        return "Bos Layer.png"


def whichHorn():
    n = random()
    if(n < 0.25):
        return "HORN 1.png"
    elif(n < 0.5):
        return "HORN 2.png"
    elif(n < 0.75):
        return "HORN 3.png"
    else:
        return "HORN 4.png"

def whichHelmet():
    n = random()
    if(n < 0.21):
        return "HELMET 1.png"
    elif(n < 0.42):
        return "HELMET 2.png"
    elif(n < 0.62):
        return "HELMET 3.png"
    elif(n < 0.82):
        return "HELMET 1.png"
    elif(n < 0.88):
        return "HELMET 1.png"
    elif(n < 0.94):
        return "HELMET 1.png"
    else:
        return "HELMET 1.png"




while(bCounter < 2532):
    images[0] = Image.open(backgrounds + "/" + whichBackground()).convert("RGBA")
    backW = whichBackWing()
    images[1] = Image.open(back_wings + "/" + backW).convert("RGBA")
    wTail = whichTail()
    images[2] = Image.open(tail + "/" + wTail).convert("RGBA")
    images[3] = Image.open(bodies + "/" + whichBody()).convert("RGBA")
    images[4] = Image.open(eyes + "/" + whichEye()).convert("RGBA")
    images[5] = Image.open(tattoo + "/" + whichTattoo()).convert("RGBA")
    #determining which front wing to use
    fWing = ""
    if(backW[:4] == "RARE"):
        fWing = "RARE FRONT WING " + backW[-5] + ".png"
    else:
        fWing = "FRONT WING " + backW[-5] + ".png"
    images[6] = Image.open(front_wings + "/" + fWing).convert("RGBA") #front wing
    #determining which hair to use
    wHair =""
    if(wTail[:4] == "RARE"):
        wHair = "RARE HAIR " + wTail[-5] + ".png"
    else:
        wHair = "HAIR " + wTail[-5] + ".png"
    images[7] = Image.open(hair + "/" + wHair).convert("RGBA") #hair
    images[8] = Image.open(horn + "/" + whichHorn()).convert("RGBA")
    images[9] = Image.open(helmets + "/" + whichHelmet()).convert("RGBA")
    final_image = images[0]

    #combining all layers
    for i in range(1,len(images)):
        final_image = Image.alpha_composite(final_image,images[i])
    #saving the image with the correct name and directory
    print(str(bCounter) + " images generated")
    final_image.save(finalImages+"/Blessings Astronaut " +str(bCounter)+".png")
    bCounter += 1

    

    

"""
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
"""





