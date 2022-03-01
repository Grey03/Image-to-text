#Should look at an image
#http://xahlee.info/comp/unicode_braille.html
#https://home.unicode.org/
#https://www.tutorialspoint.com/working-with-images-in-python
#https://www.geeksforgeeks.org/python-pil-getpixel-method/
from PIL import Image
import math

def ImToTxt(*args):
  try:
    if args[0] == int:
      contrast = args[0]
      if contrast > 255 or contrast < 0:
        contrast = 255
    else:
      contrast = 128
  except:
    contrast = 128
     
  name = input("Enter Image Name\nExample (test.jpg)\n: ")
  
  print ("\nConverting Name...")
  img = Image.open(name).convert("L")

  name = name.replace(".", " ")
  name = name.split()
  name = name[0]
  name = (name + "_ToTxt" + ".jpg")
  
  img.save(name)

  img = Image.open(name)
  
  print ("Resizing Image...")
  
  while img.size[0] * img.size[1] > 1000000:
    img = img.resize((math.ceil(img.size[0]/2),math.ceil(img.size[1]/2)))
    
  while img.size[0]%2 != 0:
    img = img.resize((img.size[0]-1, img.size[1]))
  while img.size[1]%4 != 0:
    img = img.resize((img.size[0], img.size[1]-1))

  img.save(name)

  temp = []
  print ("Generating Text...")
  Material1 = ("⬜")
  Material2 = ("⬛")
  for y in range(img.size[1]):
    temp2 = []
    temp.append(temp2)
    for x in range(img.size[0]):
      if ((img.getpixel((x,y))) > contrast):
        temp2.append(Material1)
      else:
        temp2.append(Material2)
        
  print ("Writing to output.txt...")
  
  with open("output.txt", "w") as f:
    for y in range(len(temp)):
      f.write("\n")
      for x in range(len(temp[0])):
        f.write(str(temp[y][x]))
  temp = []
  print ("Done!")