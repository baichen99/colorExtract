import cv2
import numpy as np


def calSim(x, y):
  """
  calculate 2 colors' diffrence
  """
  B_1 ,G_1, R_1 = x
  B_2 ,G_2, R_2 = y
  rmean = (int(R_1) + int(R_2)) / 2
  R = int(R_1) - int(R_2)
  G = int(G_1) - int(G_2)
  B = int(B_1) - int(B_2)
  return np.sqrt((2+rmean/256)*(R**2)+4*(G**2)+(2+(255-rmean)/256)*(B**2))

def str2np(colors):
  res = []
  for c in colors:
    a = c[1:-1].strip()
    a = a.split(' ')
    a = [x for x in a if x]
    res.append(np.array(a, dtype=np.uint8))
  return np.array(res)

def extract(img, color, thresh=200):
  """
  Extract other pixels that similar to the color from the img
  """
  H, W = img.shape[:2]
  label = np.zeros((H, W), dtype=np.int)
  sims = []
  for y in range(H):
    for x in range(W):
      sim = calSim(img[y, x], color)
      sims.append(sim)
      if sim <= thresh:
        label[y, x] = 1
  return label

def calColorProp(img):
  """
  Calculate color proportion
  :return {color:proportion}
  """
  colors = {}
  H, W = img.shape[:2]
  for i in range(H):
    for j in range(W):
      if str(img[i, j]) not in colors.keys():
        colors[str(img[i, j])] = 1
      else:
        colors[str(img[i, j])] += 1
  
  return colors


def mergeColors(img):
  # 提取图片中的主要颜色
  colors = calColorProp(img)
  # 过滤出现次数少的
  colors = {k:v for k,v in colors.items() if v > 10}
  k, v = list(colors.keys()), list(colors.values())
  k = str2np(k)
  v = np.array(v)

  idx = v.argsort()[::-1]
  for i in idx:
    color = k[i]
    if np.where((img == color).all(2))[0].size:
      label = extract(img, color)
      img[label == 1] = color

  colors2 = calColorProp(img)
  colors2 = {k:v for k,v in colors2.items() if v > 10}
  cols = [c for c in str2np(colors2)]

  n = len(cols)
  for i in range(n):
    for j in range(i+1, n):
      sim = calSim(cols[i], cols[j])
      if sim <= 300:
        cols[j] = cols[i]
  cols = list(set([tuple(c) for c in cols]))
  return cols



