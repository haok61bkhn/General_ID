import imgaug.augmenters as iaa
import cv2
import numpy as np
import uuid
import glob
import random
import tqdm
class Augment(object):
    def __init__(self,ratio):
        self.ratio = ratio

    def aug1(self,img):
        seq = iaa.Sequential([
            iaa.MaxPooling(kernel_size=2) #=2 or 3
        ])
        img_au=seq(image=img)
        return img_au

    def aug2(self,img):
        x= random.randint(1,2)
        
        seq = iaa.Sequential([
            iaa.MinPooling(kernel_size=x) #=2 or 3,4,5
        ])
        img_au=seq(image=img)
        return img_au

    def aug3(self,img):
        seq=iaa.Sequential([iaa.Fog(0)])
        img_au=seq(image=img)
        return img_au
    
    def aug4(self,img):
        seq=iaa.Sequential([
        iaa.Rain(speed=(0)) 
        ])
        img_au=seq(image=img)
        return img_au
    
    def run(self,img):
        img_aus=[]
        # x=random.randint(0,100)
        # if(x/100<self.ratio):
        #     img_aus.append(self.aug1(img))

        #take
        x=random.randint(0,100)
        if(x/100<self.ratio):
            img_aus.append(self.aug2(img))


        #take
        x=random.randint(0,100)
        if(x/100<self.ratio):
            img_aus.append(self.aug3(img))

        # x=random.randint(0,100)
        # if(x/100<self.ratio):
        #     img_aus.append(self.aug4(img))
        
        return img_aus


if __name__ == "__main__":
    output="data"
    X=Augment(0.5)
    d=0
    list_img=glob.glob("data/*.jpg")
    for path in tqdm(list_img):
    
        name=path.split("/")[-1]
        img=cv2.imread(path)
        img_aus=X.run(img)
        for im in img_aus:
            new_name=output+"/"+str(d)+"au"+name
            d+=1
            cv2.imwrite(new_name,im)
        
