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
  pip install pillow
