Do not touch anything unless I say so dummy!
This is my code if you want to use parts of it thats fine but if you want to use the whole thing credit me please.

Instructions!
1. Find some sort of image youd like to convert and drop it into this folder
2. IT WILL BE IN THE SAME FOULDER AS THIS TEXT
3. Run the code. It will ask you for the file name so enter it including the type of file it is such as example.png or test.jpg
4. Questions will come up asking for things as materials or if you would like to inver the colors. you can just answer no
5. WHEN IT ASKS FOR CONTRASTS LISTEN you will have to dial it in for a better image I recommend doing 128 first and seeing how well it comes out. If Its not good try like 200 or 100 and see what happens. If it gets better or worse. Base your number off what you want.
6. Output.txt will update everytime so if you want to save your masterpiece copy the file and move it elsewhere.
7. Once you have the file you can name it whatever its just a text file.

Info on code
If you are curios on how it works I will explain now.
First the code grabs an image. It then converts it to black and white and resizes it appropriatly.
Then once it does that it will look over the image. pixel by pixel. if the pixel is within a range set by the contrast it will make it the desired material.
For example
Contrast = 128
[170,90,190]
[200,50,255]
[195,76,211]

Result

[⬛,⬜,⬛]
[⬛,⬜,⬛]
[⬛,⬜,⬛]

This can be simply changed for color too if you really want.
Just use rgb values instead of the shading value and choose the according emoji color

Once it has an array of arrays I just write each line into the text document
See! Simple as that!

Extra info
I plan to make an algorithm that will use the braille unicode instead.
It will look for 2x4 patterns and assign braile accordingly
This will allow for the same quality of images in less space.
Just have to figure out how ill calculate what each chunk will be and how to get those chunks