#Should look at an image
#http://xahlee.info/comp/unicode_braille.html
#https://home.unicode.org/
#https://www.tutorialspoint.com/working-with-images-in-python
#https://www.geeksforgeeks.org/python-pil-getpixel-method/
from PIL import Image
import math

def ImToTxt():
  def contrast():
    try:
      c = int(input("Enter the contrast youd like (1-255): "))
    except:
      while c != int():
        try:
          c = int(input("Enter the contrast you would like (1-255): "))
        except:
          print ("Thats not accepted!")
    if c > 255 or c < 1:
      c = 128
    return c
    
  
  def nameconverter(name):
    print ("Converting Name...")
    name = name.replace(".", " ")
    name = name.split()
    name = name[0]
    name = (name + "_ToTxt" + ".jpg")
    print ("Name Converted...")
    return name
  
  def imgresizer(img):
    print ("Resizing Image...")
    while img.size[0] * img.size[1] > 1000000:
      img = img.resize((math.ceil(img.size[0]/2),math.ceil(img.size[1]/2)))
    
    while img.size[0]%2 != 0:
      img = img.resize((img.size[0]-1, img.size[1]))
    while img.size[1]%4 != 0:
      img = img.resize((img.size[0], img.size[1]-1))
    print ("Image resized...")
    return img
  
  def createarrays(img,contrastsetting):
    print ("Generating Text...")
    Material1 = ("⬜")
    Material2 = ("⬛")
    temp = []
    for y in range(img.size[1]):
      temp2 = []
      temp.append(temp2)
      for x in range(img.size[0]):
        if ((img.getpixel((x,y))) > contrastsetting):
          temp2.append(Material1)
        else:
          temp2.append(Material2)
    temp2 = []
    print ("Text Generated...")
    return temp
  
  def sendtofile(temp):
    print ("Writing to output.txt...")
    with open("output.txt", "w") as f:
      for y in range(len(temp)):
        f.write("\n")
        for x in range(len(temp[0])):
          f.write(str(temp[y][x]))
    print ("Wrote to output.txt...")




  name = input("Enter Image Name\nExample (test.png)\n: ")
  print ("")
  img = Image.open(name).convert("L")
  name = nameconverter(name)
  img.save(name)
  img = Image.open(name)
  img = imgresizer(img)
  img.save(name)
  contrastsetting = contrast()
  temp = createarrays(img,contrastsetting)
  sendtofile(temp)        
  print ("Done!")