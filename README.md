# README

Este repositório contém um script Python para extrair texto de uma imagem usando a biblioteca Pytesseract.

## Pré-requisitos

Certifique-se de ter instalado o Python em seu sistema. Além disso, o Tesseract OCR precisa estar instalado em seu sistema. Você pode baixá-lo e instalá-lo a partir do seguinte link: [Tesseract OCR](https://github.com/tesseract-ocr/tesseract).

## Instalação

1. Clone este repositório em sua máquina local usando o comando:
   ```
   git clone https://github.com/mario-evangelista/transformando_imagem_em_texto.git
   ```

2. Certifique-se de ter instalado as dependências necessárias. Você pode instalar as dependências usando o seguinte comando:
   ```
   pip install pytesseract opencv-python
   ```

3. Certifique-se de ter a imagem da qual deseja extrair o texto. Coloque a imagem na pasta `input`.

## Uso

Execute o script Python `extract_text_from_image.py` fornecendo o caminho para sua imagem como argumento. O texto extraído será salvo no arquivo `output.txt` na pasta `output`.

Exemplo:
```
python extract_text_from_image.py input/bootcamp.webp
```

Certifique-se de que o caminho do Tesseract OCR esteja corretamente definido no script Python.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas e enviar solicitações de recebimento (pull requests).

Se encontrar algum problema ou tiver alguma sugestão, por favor, abra um problema [aqui](https://github.com/mario-evangelista/transformando_imagem_em_texto/issues).

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
