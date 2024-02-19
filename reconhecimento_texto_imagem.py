import pytesseract
import cv2

imagem = cv2.imread("input/bootcamp.webp")  # caminho da imagem

caminho = r"C:\Program Files\Tesseract-OCR"  # caminho de intalação do tesseract
pytesseract.pytesseract.tesseract_cmd = caminho + r'\tesseract.exe'  # concatenando o caminho da instalação com o exe do pytesseract
texto = pytesseract.image_to_string(imagem,
                                    lang="por")  # para utilizar outras linguas no tesseract: print(pytesseract.get_languages())

arquivo = open("output/output.txt", "w+")  # escrever texto no arquivo

print(texto, file=arquivo)  # salvar o texto da imagem no arquivo .txt
