from PIL import Image
import os
from os import listdir
from random import random
import csv

#attribute folders:
backgrounds = r"Backgrounds"
bodies = r"Bodies"
hair = r"Hair"
tail = r"Tail"
tattoo = r"Tattoo"
front_wings = r"Front_Wings"
back_wings = r"Back_Wings"
horn = r"Horn"
eyes = r"Eye"
helmets = r"Helmet"

#final images destination
finalImages = r"Blessings"

#dictionaries
background_name = {
    "ASTRONAUT BACKGROUND 1.png":"",
    "ASTRONAUT BACKGROUND 1.png":"",
    "ASTRONAUT BACKGROUND 1.png":"",
    "ASTRONAUT BACKGROUND 1.png":"",
    "ASTRONAUT BACKGROUND 1.png":"",
    "ASTRONAUT BACKGROUND 1.png":"",
    "ASTRONAUT BACKGROUND 1.png":"",
    
    "ASTRONAUT GRADIENT BACKGROUND 1.png":"",
    "ASTRONAUT GRADIENT BACKGROUND 1.png":"",
    "ASTRONAUT GRADIENT BACKGROUND 1.png":"",
    "ASTRONAUT GRADIENT BACKGROUND 1.png":"",
    "ASTRONAUT GRADIENT BACKGROUND 1.png":"",
    "ASTRONAUT GRADIENT BACKGROUND 1.png":"",
    "ASTRONAUT GRADIENT BACKGROUND 1.png":"",

    "ASTRONAUT RARE BACKGROUND 1.png":"",
    "ASTRONAUT RARE BACKGROUND 1.png":"",
    "ASTRONAUT RARE BACKGROUND 1.png":"",
    "ASTRONAUT RARE BACKGROUND 1.png":"",
}
body_name = {
    "ASTRONAUT BODY 1.png":"",
    "ASTRONAUT BODY 2.png":"",
    "ASTRONAUT BODY 3.png":"",

    "ASTRONAUT RARE BODY 1.png":"",
    "ASTRONAUT RARE BODY 2.png":""
}
hair_name = {
    "ASTRONAUT HAIR 1.png":"",
    "ASTRONAUT HAIR 2.png":"",
    "ASTRONAUT HAIR 3.png":"",

    "ASTRONAUT RARE HAIR 1.png":"",
    "ASTRONAUT RARE HAIR 2.png":"",

}
tail_name = {
    "ASTRONAUT TAIL 1.png":"",
    "ASTRONAUT TAIL 2.png":"",
    "ASTRONAUT TAIL 3.png":"",

    "ASTRONAUT RARE TAIL 1.png":"",
    "ASTRONAUT RARE TAIL 2.png":""
}
tattoo_name = {
    "220329-0959-BOS LAYER.png":"",
    "ASTRONAUT TATTOO 1.png":"",
    "ASTRONAUT TATTOO 2.png":"",
    "ASTRONAUT TATTOO 3.png":"",
    "ASTRONAUT TATTOO 4.png":"",
    "ASTRONAUT TATTOO 5.png":""
    
}
fWing_name = {
    "ASTRONAUT FRONT WING 1.png":"",
    "ASTRONAUT FRONT WING 2.png":"",
    "ASTRONAUT FRONT WING 3.png":"",
    "ASTRONAUT FRONT WING 4.png":"",
    "ASTRONAUT RARE FRONT WING 1.png":"",
    "ASTRONAUT RARE FRONT WING 2.png":"",
    "ASTRONAUT RARE FRONT WING 3.png":"",
}
bWing_name = {
    "ASTRONAUT BACK WING ?.png":"",
    "ASTRONAUT BACK WING 2.png":"",
    "ASTRONAUT BACK WING 3.png":"",
    "ASTRONAUT BACK WING 4.png":"",
    "ASTRONAUT RARE BACK WING 1.png":"",
    "ASTRONAUT RARE BACK WING 2.png":"",
    "ASTRONAUT RARE BACK WING 3.png":""
}
horn_name = {
    "ASTRONAUT HORN 1.png":"",
    "ASTRONAUT HORN 2.png":"",
    "ASTRONAUT HORN 3.png":"",
    "ASTRONAUT HORN 4.png":"",
}
eye_name = {
    "ASTRONAUT EYE F1.png":"",
    "ASTRONAUT EYE F2.png":"",
    "ASTRONAUT EYE F3.png":"",
    "ASTRONAUT EYE F4.png":"",
    "ASTRONAUT EYE M1.png":"",
    "ASTRONAUT EYE M2.png":"",
    "ASTRONAUT EYE M3.png":"",
    "ASTRONAUT EYE M4.png":"",
}
helmet_name = {
    "ASTRONAUT HELMET 1.png":"",
    "ASTRONAUT HELMET 2.png":"",
    "ASTRONAUT HELMET 3.png":"",
    "ASTRONAUT HELMET 4.png":"",
    "ASTRONAUT HELMET 5.png":"",
    "ASTRONAUT HELMET 6.png":"",
    "ASTRONAUT HELMET 7.png":"",
    "ASTRONAUT HELMET 8.png":"",
}


#defining an empty images array which we'll use to come up with each final image
images = []
for i in range(len(os.listdir("."))-3):
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



Metadata = []

while(bCounter < 2532):
    blessing = {}

    if(bCounter < 10):
        id = "000" + str(bCounter)
    elif(bCounter < 100):
        id = "00" + str(bCounter)
    elif(bCounter < 1000):
        id = "0" + str(bCounter)
    else:
        id = str(bCounter)
    blessing["id"] = int(id)

    wBackground = whichBackground()
    images[0] = Image.open(backgrounds + "/" + wBackground).convert("RGBA")
    blessing["Background"] = background_name[wBackground]

    backW = whichBackWing()
    images[1] = Image.open(back_wings + "/" + backW).convert("RGBA")
    blessing["Back Wing"] = bWing_name[backW]

    wTail = whichTail()
    images[2] = Image.open(tail + "/" + wTail).convert("RGBA")
    blessing["Tail"] = tail_name[wTail]

    wBody = whichBody()
    images[3] = Image.open(bodies + "/" + wBody).convert("RGBA")
    blessing["Body"] = body_name[wBody]

    wEye = whichEye()
    images[4] = Image.open(eyes + "/" + wEye).convert("RGBA")
    blessing["Eyes"] = eye_name[wEye]

    wTattoo = whichTattoo()
    images[5] = Image.open(tattoo + "/" + wTattoo).convert("RGBA")
    blessing["Tattoo"] = tattoo_name[wTattoo]

    #determining which front wing to use
    fWing = ""
    if(backW[:4] == "RARE"):
        fWing = "RARE FRONT WING " + backW[-5] + ".png"
    else:
        fWing = "FRONT WING " + backW[-5] + ".png"
    images[6] = Image.open(front_wings + "/" + fWing).convert("RGBA") #front wing
    blessing["Front Wing"] = fWing_name[fWing]

    #determining which hair to use
    wHair =""
    if(wTail[:4] == "RARE"):
        wHair = "RARE HAIR " + wTail[-5] + ".png"
    else:
        wHair = "HAIR " + wTail[-5] + ".png"
    images[7] = Image.open(hair + "/" + wHair).convert("RGBA") #hair
    blessing["Hair"] = hair_name[wHair]

    wHorn = whichHorn()
    images[8] = Image.open(horn + "/" + wHorn).convert("RGBA")
    blessing["Horn"] = horn_name[wHorn]

    wHelmet = whichHelmet()
    images[9] = Image.open(helmets + "/" + wHelmet).convert("RGBA")
    blessing["Helmet"] = helmet_name[wHelmet]

    final_image = images[0]

    #combining all layers
    for i in range(1,len(images)):
        final_image = Image.alpha_composite(final_image,images[i])
    #saving the image with the correct name and directory
    final_image.save(finalImages+"/Blessings Astronaut " +str(bCounter)+".png")

    Metadata.append(blessing)
    bCounter += 1

main_info = ["id","Background","Back Wing","Tail","Body","Eyes","Tattoo","Front Wing","Hair","Horn","Helmet"]

with open("metadata.csv", "w") as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames= main_info)
    writer.writeHeader()
    writer.writerows(Metadata)

    

    

