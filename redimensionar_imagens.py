from PIL import Image
import os
from tkinter import Tk, filedialog

# Ocultar a janela principal do Tkinter
root = Tk()
root.withdraw()

# Abrir janela para a pessoa selecionar a pasta
pasta_imagens = filedialog.askdirectory(title="Selecione a pasta com as imagens")

if not pasta_imagens:
    print("Nenhuma pasta selecionada. Encerrando o programa.")
    input("Pressione Enter para sair...")
    exit()

# Criar pasta de saída
pasta_saida = os.path.join(pasta_imagens, 'Redimensionadas')
os.makedirs(pasta_saida, exist_ok=True)

# Contadores para relatório
total = 0
sucesso = 0
falha = 0

# Extensões aceitas
extensoes_imagens = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp', '.heic', '.jfif', '.ico')

# Loop pelos arquivos da pasta
for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith(extensoes_imagens):
        total += 1
        caminho_completo = os.path.join(pasta_imagens, nome_arquivo)

        # Gera novo nome com extensão .jpeg
        nome_saida = os.path.splitext(nome_arquivo)[0] + ".jpeg"
        caminho_saida = os.path.join(pasta_saida, nome_saida)

        try:
            with Image.open(caminho_completo) as img:
                # Tratar imagens com transparência (ex.: PNG, WEBP, GIF)
                if img.mode in ("RGBA", "LA"):
                    fundo = Image.new("RGB", img.size, (255, 255, 255))  # fundo branco
                    fundo.paste(img, mask=img.getchannel("A"))
                    imagem_redimensionada = fundo.resize((1500, 1500), Image.LANCZOS)
                else:
                    imagem_redimensionada = img.resize((1500, 1500), Image.LANCZOS)

                imagem_redimensionada.save(caminho_saida, format='JPEG', quality=95)
                print(f" Redimensionada e convertida: {nome_arquivo} -> {nome_saida}")
                sucesso += 1
        except Exception as e:
            print(f" Erro com {nome_arquivo}: {e}")
            falha += 1

print("\n--- RELATÓRIO ---")
print(f"Total de imagens encontradas: {total}") 
print(f"Redimensionadas e salvas em JPEG: {sucesso}")
print(f"Falharam: {falha}")
print(f"As imagens redimensionadas estão na pasta 'Redimensionadas' dentro da pasta selecionada.")
input("\nPressione Enter para sair...")
