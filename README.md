# 🖼️ Redimensionador e Conversor de Imagens

Este projeto é um script em **Python** que permite selecionar uma pasta com imagens e, automaticamente, redimensiona e converte todas elas para o formato **JPEG** com tamanho **1500x1500 pixels**.  
As imagens processadas são salvas em uma subpasta chamada **Redimensionadas** dentro da pasta escolhida.

---

## 🚀 Funcionalidades
- Seleção de pasta via interface gráfica (Tkinter).  
- Suporte a múltiplos formatos de imagem:  
  `.jpg, .jpeg, .png, .gif, .bmp, .tiff, .tif, .webp, .heic, .jfif, .ico`  
- Redimensionamento automático para **1500x1500** pixels.  
- Conversão para **JPEG** com qualidade de 95%.  
- Tratamento de imagens com **transparência** (fundo transparente vira fundo branco).  
- Relatório final com total de imagens, quantas foram processadas com sucesso e quantas falharam.  

---

## 📦 Requisitos
- Python 3.8+  
- Bibliotecas Python:
  ```bash
  pip install -r requirements.txt
  ```

---

## ▶️ Como usar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/nome-do-repositorio.git
   ```

2. Navegue até a pasta do projeto:
   ```bash
   cd nome-do-repositorio
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute o script:
   ```bash
   python redimensionar.py
   ```

5. Selecione a pasta que contém as imagens.  
6. Aguarde o processamento.  
7. As imagens convertidas estarão na pasta **Redimensionadas** criada automaticamente.  

---

## 📊 Exemplo de saída no terminal
```
 Redimensionada e convertida: foto1.png -> foto1.jpeg
 Redimensionada e convertida: imagem2.webp -> imagem2.jpeg
 Erro com corrompida.bmp: cannot identify image file

--- RELATÓRIO ---
Total de imagens encontradas: 5
Redimensionadas e salvas em JPEG: 4
Falharam: 1
As imagens redimensionadas estão na pasta 'Redimensionadas' dentro da pasta selecionada.
```

---

## 📝 Observações
- Caso alguma imagem esteja corrompida ou em formato não suportado, ela será ignorada e reportada no relatório.  
- Imagens com fundo transparente terão o fundo convertido para **branco**.  

---

👨‍💻 Desenvolvido em Python com [Pillow](https://python-pillow.org/).
