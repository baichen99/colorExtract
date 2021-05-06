from colorExtract import *

img = cv2.imread('imori.jpg')
colors = mergeColors(img)
print('main colors of the img are ', colors)

for c in colors:
  label = extract(img, c, thresh=200)
  img[label==1] = c

cv2.imshow('img', img)

cv2.waitKey(0)