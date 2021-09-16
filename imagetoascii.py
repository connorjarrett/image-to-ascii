# Imports #
import cv2 # Image processor
import os # For handling files

# Variables #
debug = True # Debug, shows extra date like the image in a window and prints image stats, reccomended off
compression = True # Compression, Makes an image more likely to fit in a normal terminal window, disable for higher quality images but make sure the terminal is the right size for correct results, reccomended on

luminance_table = ['.',",",'-','~',':',';','=','!','*','#','$','@'] # Table of ascii characters used to map brightness
final_out = [] # Home for all of the ascii characters
string_out = "" # Each new line per character
line_out = []  # Each  image per line

# Defenitions #
def findImages(custom_name): # Find the image
    if not custom_name: # If no custom file is specified, find a new one
        for x in os.listdir("./"):
            if (x.lower()).endswith(".png") or (x.lower()).endswith(".jpg"): # If it ends in png or jpg ignoring capitals
                return(x)
    else: # If custom name is specified, return the given name
        return(custom_name) 

def returnCharacter(brightness): # Map a character depending on how bright it is, 12 levels of brightness as indicated in luminance_table
    if brightness <= 21.25:
        return(luminance_table[0])
    elif brightness > 21.25 and brightness <= 42.5:
        return(luminance_table[1])
    elif brightness > 42.5 and brightness <= 63.75:
        return(luminance_table[2])
    elif brightness > 63.75 and brightness <= 85:
        return(luminance_table[3])
    elif brightness > 85 and brightness <= 106.25:
        return(luminance_table[4])
    elif brightness > 106.25 and brightness <= 127.5:
        return(luminance_table[5])
    elif brightness > 127.5 and brightness <= 148.75:
        return(luminance_table[6])
    elif brightness > 148.75 and brightness <= 170:
        return(luminance_table[7])
    elif brightness > 170 and brightness <= 191.25:
        return(luminance_table[8])
    elif brightness > 191.25 and brightness <= 212.5:
        return(luminance_table[9])
    elif brightness > 212.5 and brightness <= 233.75:
        return(luminance_table[10])
    else:
        return(luminance_table[11])

image = cv2.imread(findImages(None), 0) # Replace 'None' with the name (and path if oustside of this directory) of the file you would like to import. Leaving as 'None' will pick one from the folder the script is located in
height, width = image.shape # Calcuate width and height for adjustments

# Adjust the height and width accordingly dependingo n the file size, using divison so it maintains aspect ratio on strangely sized images
if compression: # Only adjust if Compression is enabled
    if height < 720 and width < 128: 
        image = cv2.resize(image, (int(width/1),int(height/1)))
    elif height == 237 and width == 643: # Custom Case
        image = cv2.resize(image, (int(width/5),int(height/5))) # Custom case
    elif height >= 720 and width >= 1280:
        image = cv2.resize(image, (int(width/10),int(height/10)))
    elif height >= 4000 and width >= 6000:
        image = cv2.resize(image, (int(width/50),int(height/50)))

height, width = image.shape # Recalucate height and width after adjustments

if debug: # Enable debug at top of file to see changes
    cv2.imshow('img', image)  # Displays processed image in window

for y in range(0, height, 1): # Map each pixels Brightness value and convert to ascii, send to table
    for x in range(0, width, 1):
        final_out.append(returnCharacter(image[y, x]))

for z in range(len(final_out)):
    if len(string_out) < width: # Check if line completed
        string_out = string_out + final_out[z] # If line not completed, add to it
    else: # If line completed, add it to the final and add to the next one
        line_out.append(string_out)
        string_out = ""
        string_out = string_out + final_out[z]

for x in line_out: # For each line in the file, print it.
    print(x)

if debug: # Enable at top of file to see changes
    print(len(final_out), width, height) # Print image width, height and character count
    cv2.waitKey(0) # Hide window on keypress
