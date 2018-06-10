# -*- coding: utf-8 -*-

import cv2  # openCV
# Importante!!! open CV usa modelo BGR e nao RGB
import config
from dct import dct_2d
from idct import idct_2d


def main():
	# ler imagem.
	# A imagem lida eh um array[linha][coluna]
	img = cv2.imread(config.imageToRead)
	numberCoefficients = input("Quantos coeficiente você deseja aplicar: ") 
	print("Numero de coeficiente	" + str(numberCoefficients) + " !" + "\n")
	# Chama cada questao de forma isolada
	print('*************** DCT_img ****************')
	imgResult = dct_2d(img,numberCoefficients)
	cv2.imwrite('AAAdct256.jpg',imgResult)
	
	print('*************** Iidct_img ****************')
	idct_img = idct_2d(imgResult)
	cv2.imwrite('AAAidct256.jpg',idct_img)

	

if __name__ == '__main__':
	main()
