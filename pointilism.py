"""
file name is pointilism.py

purpose: produces a SCALED (4) pointilistic image of a given image using pygame. more on pointilism: https://en.wikipedia.org/wiki/Pointillism. 

revision: Boris Zugic - Initial code

instructions: run the program in the following way: python pointilism.py {filename}.{image type} {OPTIONAL: name of image to be saved}
    for example: python pointilism.py flowers.jpg
                 python pointilism.py flowers.jpg flowers_pointilism

issues/limitations:
    - file provided must be an image, behaviour unknown otherwise
    - the larger the given image, the longer the program takes to produce an output, BUT the output image is of higher quality
"""

# IMPORTS #
import pygame
import random
import sys


def main():

    scaling_factor = 4

    try:
        source_image = sys.argv[1] 

    except:
        print("Image not provided. Please run the program in the following way: python pointilism.py {filename}")
        exit(-1)

    image = pygame.image.load(source_image)

    (width, height) = image.get_size()  # get dimensions of image

    modified_image = pygame.display.set_mode((width * scaling_factor, height * scaling_factor)) # create a pygame screen with the corresponding dimensions

    for y in range(height): # for each pixel in row
        
        for x in range(width): # for each pixel in column
        
            (r, g, b, _) = image.get_at((x, y)) # get corresponding rgb value
            
            # PRODUCING THE OUTPUT IMAGE #  
            
            # reducing number of red, green and blue pixels (these will be the dots used to draw the output image)
            red_pixels = r // 50 
            green_pixels = g // 50
            blue_pixels = b // 50
            
            
            # drawing pixels at pseudo-random locations of a scaled rectangle #
            
            # red
            for i in range(red_pixels + 1): 
            
                pygame.draw.rect(modified_image, (255, 0, 0), (random.randint(x * scaling_factor, (x * scaling_factor) + (scaling_factor - 1)), random.randint(y * scaling_factor, (y * scaling_factor) + (scaling_factor - 1)), 1, 1))  

            # green    
            for i in range(green_pixels + 1): 
            
                pygame.draw.rect(modified_image, (0, 255, 0), (random.randint(x * scaling_factor, (x * scaling_factor) + (scaling_factor - 1)), random.randint(y * scaling_factor, (y * scaling_factor) + (scaling_factor - 1)), 1, 1)) 
                
            # blue
            for i in range(blue_pixels + 1):  

                pygame.draw.rect(modified_image, (0, 0, 255), (random.randint(x * scaling_factor, (x * scaling_factor) + (scaling_factor - 1)), random.randint(y * scaling_factor, (y * scaling_factor) + (scaling_factor - 1)), 1, 1))  
                
            
    pygame.display.update() # update display to implement new drawings

    # condition loop to keep the window open until user exits #     
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                try:
                    pygame.image.save(modified_image, f"{sys.argv[2]}.jpg") # saves image with user provided name
                except:
                    pass

                exit()	

if __name__ == "__main__":
    main()