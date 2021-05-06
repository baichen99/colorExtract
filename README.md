
## 介绍

受到[这篇博客](https://blog.csdn.net/qq_16564093/article/details/80698479)的启发，根据LAB颜色空间计算两个颜色的相似度，并提取图片中的主要颜色。将与主要颜色相近的颜色替换为主要颜色来实现减色的效果。

## 使用方法

```python
from colorExtract import *

img = cv2.imread('imori.jpg')
colors = mergeColors(img)
print('main colors of the img are ', colors)

for c in colors:
  label = extract(img, c, thresh=200)
  img[label==1] = c

cv2.imshow('img', img)
cv2.waitKey(0)
```

## 截图

![](https://raw.githubusercontent.com/baichen99/pics/master/img/imori.jpg)

![](https://raw.githubusercontent.com/baichen99/pics/master/img/output.png)