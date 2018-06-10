# -*- coding: utf-8 -*-

from math import cos, pi, sqrt
import numpy as np

def idct_2d(image):
    
    height = image.shape[0]
    width =  image.shape[1]
    imageRow = np.zeros_like(image).astype(float)
    imageCol = np.zeros_like(image).astype(float)

  
    for h in range(height):
        imageRow[h, :] = idct_1d(image[h, :]) # aplicando IDCT na linhas
    for w in range(width):
        imageCol[:, w] = idct_1d(imageRow[:, w]) # aplicando IDCT nas colunas

    return imageCol

def idct_1d(image):
   
    n = len(image)
    newImage = np.zeros_like(image).astype(float)

    for i in range(n):
        sum = 0
        for k in range(n):
            ck = sqrt(0.5) if k == 0 else 1 # operador tenario para verificar o valor do CK
            sum += ck * image[k] * cos(2 * pi * k / (2.0 * n) * i + (k * pi) / (2.0 * n))

        newImage[i] = sqrt(2.0 / n) * sum

    return newImage
