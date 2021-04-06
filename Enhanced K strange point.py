# Enhanched k strange point


from PIL import Image
import numpy as np
import array as arr
from time import time

start_time = time()
img = Image.open("roiImage.jpg")

img1 = Image.open("blankImg.jpg")
img2 = Image.open("blankImg.jpg")
img3 = Image.open("blankImg.jpg")


width, height = img.size

# green channel extraction
eye = img.load()
for i in range(width):
    for j in range(height):
        r, g, b = eye[i, j]
        eye[i, j] = (r-r, g-0, b-b)
img.save('greeneye.jpg')

# getting kmin and kmax
data = np.array(img)
kmin = data[..., 1].min()
kmax = data[..., 1].max()


# getiing Kstr
tempArr = arr.array('d', [])
#print(kmin, kmax, constDist)


for i in range(width):
    for j in range(height):
        r, g, b = eye[i, j]  # (0,78,0)

        tempArr.append(g)

dempoints = np.sort(tempArr)

ks = np.median(dempoints)

if np.linalg.norm(kmin-ks) == np.linalg.norm(kmax-ks):
    kstr = ks
    # print(cstr)
elif np.linalg.norm(kmin-ks) < np.linalg.norm(kmax-ks):
    kstr = (ks+(abs(kmax-ks)/2))  # 2 clusers 1
    # print(cstr)
elif np.linalg.norm(kmin-ks) > np.linalg.norm(kmax-ks):
    kstr = (kmin+(abs(ks-kmin)/2))  # 2 clusers 1
    # print(cstr)
print(kmin, kmax, kstr)

for i in range(width):
    for j in range(height):
        x = eye[i, j]  # (0,78,0)
        coords = i, j

        kminx = np.linalg.norm(x[1]-kmin)  # dist from kmin
        kmaxx = np.linalg.norm(x[1]-kmax)  # dist from kmax
        kstrx = np.linalg.norm(x[1]-kstr)  # dist from kstr

        if np.isnan(kminx) or np.isnan(kmaxx) or np.isnan(kstrx):
            continue
        elif(kstrx < kminx and kstrx < kmaxx):
            img3.putpixel(coords, x)
        elif (kminx < kstrx) and (kminx < kmaxx):
            continue
        elif (kmaxx < kminx) and (kmaxx < kstrx):
            img2.putpixel(coords, x)


img3.save("Enhanced_K_strange_disk.jpg")
img2.save("Enhanced_K_strange_cup.jpg")

proc_time = time()-start_time
print(proc_time)

# 10.950969696044922
