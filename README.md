# Transformação de imagens em Dados

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

Execute o script Python `reconhecimento_texto_imagem.py` fornecendo o caminho para sua imagem como argumento. O texto extraído será salvo no arquivo `output.txt` na pasta `output`.

Exemplo:
```
python reconhecimento_texto_imagem.py input/bootcamp.webp
```

Certifique-se de que o caminho do Tesseract OCR esteja corretamente definido no script Python.

## INPUT / IMAGEM
<div align="center">
<img src="https://github.com/mario-evangelista/transformando_imagem_em_texto/assets/121322767/10e1ba47-8156-4c2f-919b-a62298d3fba0" width="700px" />
</div>

## OUTPUT / TXT
<div align="center">
<img src="https://github.com/mario-evangelista/transformando_imagem_em_texto/assets/121322767/bcfd431d-d9e3-493f-add3-266d0e88c656" width="700px" />
</div>

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir problemas e enviar solicitações de recebimento (pull requests).

Se encontrar algum problema ou tiver alguma sugestão, por favor, abra um problema [aqui](https://github.com/mario-evangelista/transformando_imagem_em_texto/issues).

## Licença

Este projeto é licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
