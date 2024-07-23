import numpy as np
import cv2
from collections import deque

# for decryption we need the seed and the size of image that is hidden

# read image
img = cv2.imread("New_image.png")

# put our binary code in main
row = img.shape[0]
column = img.shape[1]

# Data from the image which is hidden
b_str_len = 200*266*8
# selecting random seed
np.random.seed(9)
# generate random numbers
rand_num = np.random.randint(row*column, size=b_str_len)

# even for 1, odd for 0
# now we obtain hidden image, if the number is even so we know we had 1 otherwise it is 0
arr = deque()
for i in range(b_str_len-1,-1,-1):
    x = rand_num[i] // column
    y = rand_num[i] % column
    if(img[x, y, 0]%2 == 0):
        img[x, y, 0] -= 1
        arr.append(1)
    elif(img[x, y, 0]%2 != 0):
        img[x, y, 0] += 1
        arr.append(0)

# Now that we have the binaries let obtain acual number from it
res = np.zeros((266,200),dtype=int)
for i in range(266):
    for j in range(200):
        tmp = np.array([0,0,0,0,0,0,0,0])
        for z in range(8):
            tmp[z] = arr.pop()
        res[i][j] = tmp.dot(1 << np.arange(tmp.size)[::-1])

# Make the image
cv2.imwrite('hidden_image.png', res)