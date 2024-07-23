import numpy as np
import cv2

# Read both images first image is our hidding image, second the one will be hidden
main_img = cv2.imread("235470.jpg")
C_img = cv2.imread("my_image.jpg")

# Convert to grey scale
C_img_grey = cv2.cvtColor(C_img, cv2.COLOR_BGR2GRAY)

# Convert gray scale numbers to binary
bnum_str = ""
for i in C_img_grey:
    for j in i:
        bnum_str += np.binary_repr(j, width = 8)

# Put our binary code in main
row = main_img.shape[0]
column = main_img.shape[1]

# Length of binary string
b_str_len = len(bnum_str)
# Selecting random seed
np.random.seed(9)
# Generate random numbers
rand_num = np.random.randint(row*column, size=b_str_len)

# Even for 1, Odd for 0
# That is the way we change the main image we increase or decrease to obtain the values
# to be even or odd
for i in range(b_str_len):
    x = rand_num[i] // column
    y = rand_num[i] % column

    if(bnum_str[i] == '1' and main_img[x, y, 0]%2 != 0):
        if main_img[x, y, 0] != 255:
            main_img[x, y, 0]+=1
        else:
            main_img[x, y, 0]-=1
    elif(bnum_str[i] == '0' and main_img[x, y, 0]%2 == 0):
        if main_img[x, y, 0] != 0:
            main_img[x, y, 0]-=1
        else:
            main_img[x, y, 0]+=1

# Save as png cz low change in pixels with title of New_image
cv2.imwrite('New_image.png', main_img)
