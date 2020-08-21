import glob
fonts=glob.glob("font/*")
from trdg.generators import (
    GeneratorFromDict,
    GeneratorFromRandom,
    GeneratorFromStrings,
    GeneratorFromWikipedia,
)

id=open("id.txt","r").split("\n")[:-1]
# The generators use the same arguments as the CLI, only as parameters
generator = GeneratorFromStrings(
    string,
    blur=1,
    count=30,
    random_blur=True,
    background_type=3,
    random_skew=True,
    space_width=2,
    size=32,
    character_spacing=1,
    fit=True,
    alignment=1,
    #text_color="#a07081",
    fonts=fonts,
    image_dir="./background",
)

d=0
for img, lbl in generator: 
    img.save("data/"+str(d)+"_"+lbl+".jpg")
    d+=1
    print(lbl)
