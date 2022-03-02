#Should look at an image
#http://xahlee.info/comp/unicode_braille.html
#https://home.unicode.org/
#https://www.tutorialspoint.com/working-with-images-in-python
#https://www.geeksforgeeks.org/python-pil-getpixel-method/
global Invert 
Invert = int
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
    name = ("TEMPIMAGENOTOUCH" + ".jpg")
    print ("Name Converted...")
    return name
  
  def imgresizer(img):
    print ("Resizing Image...")
    while img.size[0] * img.size[1] > 1000000:
      img = img.resize((math.ceil(img.size[0]/2),math.ceil(img.size[1]/2)))
      
    #Only use in braile version
    while img.size[0]%2 != 0:
      img = img.resize((img.size[0]-1, img.size[1]))
    while img.size[1]%3 != 0:
      img = img.resize((img.size[0], img.size[1]-1))
    print ("Image resized...")
    return img
  
  def createarrays(img,contrastsetting):
    def numtobraille(number):
      number = (number + 10240)
      return chr(number)
      #temp
      #use 2x3 braille for now
    def ChunkAnalyzer(chunklist,contrast):
      global Invert
      chunklist = [
        chunklist[5],
        chunklist[3],
        chunklist[1],
        chunklist[4],
        chunklist[2],
        chunklist[0]
      ]
      #should come in as # top to bottom left to right
      #example 
      #a b
      #c d
      #e f
      #will be [a, b, c, d, e, f]
      #should be [f,d,b,e,c,a]
      #then make it into binary
      temp = ("")
      for n in range(len(chunklist)):
        if chunklist[n] > contrastsetting:
          chunklist[n] = 1 - Invert
        else:
          chunklist[n] = 0 + Invert
          
      for i in range(len(chunklist)):
        temp = (str(temp) + str(chunklist[i]))
      temp = int(temp,2)
      return numtobraille(temp)
      
    print ("Generating Text...")    
    temp = []
    temp2 = []
    for y in range(0,img.size[1],3):
      temp.append(temp2)  
      temp2 = []
      for x in range(0,img.size[0],2):
        chunk = [
          (img.getpixel((x,y))),
          (img.getpixel((x + 1,y))),
          (img.getpixel((x,y + 1))),
          (img.getpixel((x + 1,y + 1))),
          (img.getpixel((x,y + 2))),
          (img.getpixel((x + 1,y + 2)))
        ]
        temp2.append(ChunkAnalyzer(chunk,contrastsetting)) 
    print ("Text Generated...")
    return (temp)
    
    
      
  
  def sendtofile(temp):
    temp.pop(0)
    print ("Writing to output.txt...")
    with open("output.txt", "w") as f:
      for y in range(len(temp)):
        if y != 0:
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

  decide = input("Would you like to change the final dimensions y/n: ").lower()
  if decide == "y":
    x = int(input("Enter Final x: "))
    y = int(input("Enter Final y: ")) + 1
    img = img.resize((x*2,y*3))
  decide2 = input("Would you like to invert the colors y/n: ").lower()
  if decide2 == "y":
    global Invert
    Invert = 1
  else:
    Invert = 0
    
  
  img = imgresizer(img)
  img.save(name)
  contrastsetting = contrast()

  temp = createarrays(img, contrastsetting)
  sendtofile(temp)        
  print ("Done!")
  
ImToTxt()