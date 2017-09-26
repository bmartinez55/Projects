#Brian Martinez
from PIL import Image

im = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png','8.png','9.png'] #Make an array on array of the images
o_list=[]

for i in range(9):
  o_list.append(Image.open(im[i])) #Opening every image in the array

width , height = o_list[0].size #Setting the width and height of one image
newImage=Image.new('RGB',(width,height)) #Creating a new image file
midImg = newImage.load() #Loading the new image file

for x in range(width): #Both for loops interates through each pixel of every image
  for y in range(height):
    r_list=[] # r,g,b lists hold their designated pixels
    g_list=[] 
    b_list=[]
    for z in range(0,9): # Iterates through each image
      r,g,b = o_list[z].getpixel((x,y)) #Grabs each pixel from the designated location
      r_list.append(r) #All pixels are transferred to the three list by RGB
      g_list.append(g)
      b_list.append(b)
    r_list.sort() # The three lists sort the pixels
    g_list.sort()
    b_list.sort()
    midImg[x,y] = (r_list[4], g_list[4], b_list[4]) # Initialize the median
    
newImage.save("mod.png") # Save the last modification
      
      
    






