import tkinter
from tkinter import *
from PIL import Image, ImageTk
import os

#Redimesionnement
basewidth = 64

img = Image.open('emoticones.png')

wpercent = (basewidth/float(img.size[0]))
hsize = int((float(img.size[1])*float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)

os.remove("redimension.png")
print("remove")
img.save('redimension.png')

#Noir et Blanc
ref_image = Image.open("redimension.png")
largeur, hauteur = ref_image.size

print(ref_image.format)
print(ref_image.getbands())
print(ref_image.getpixel((50, 50)))

ref_image_r, ref_image_g, ref_image_b, ref_image_a = ref_image.split()
ref_image_r.show()

print(ref_image_r.getbands())
print(ref_image.getpixel((50, 50)))
# - - - -
# C Sauvegarde dans un fichier de l'objet image
# - - - -
os.remove("test.png")
ref_image_r.save("test.png")

#permet de récuperer une image de la redimensionner et de la rendre en noir et blanc
