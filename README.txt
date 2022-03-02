Do not touch anything unless I say so dummy!
This is my code if you want to use parts of it thats fine but if you want to use the whole thing credit me please.

If you think your image looks weird heres why.
1. Could be my code
2. Try zooming out on what you are using. Things like .txt are strange and format text weirdly sometimes. If it looks like lines are not the same size I garuntee that isn't the code its whatever you are using.
3. Did you use the resize? It does not change the image the way you think. It makes the final product have those many letters. If you want it to lets say be 60 by 60 pixels you would actually enter 30 for the x and 20 for the y. This is because the braille is 2x3 so if you want a 60x60 pixel image perfectly like that, do that.

Instructions!
1. Find some sort of image you would like to convert!
2. Put it in the folder this readme is in
3. Run the code!
4. tell it the file name including the .jpg or .png ending
5. tell it the contrast
6. decide if you want to change the final dimensions
7. if you chose yes enter the ammount of char for the x and y
8. the output will update with the new image so if you want to save a masterpiece copy the .txt file elsewhere


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

Here is where it differs from the normal converter
It will look at the data in chunks of 2 wide 3 tall
It then assigns a 1 or 0 based on what was earlier said about the contrast setting
I then send this over to the braille converter which looks at the array and assigns the correct braille

Example
0 1
0 0
1 0

Result

 *

* 


(Not actually braille but big for example)

then it makes all these chunks into arrays of arrays as shown earlier
and adds it to the output file

Extra info
Lower Contrasts will pick up more white
Higher will pick up more dark
I recommend using 128 to start and then going either direction if you want more detail
If the image is lighter use a higher contrast if its darker use a lower contrast