import os
import shutil

# Caminho da pasta que será organizada (pode personalizar)
PASTA_ALVO = os.path.expanduser("~/Downloads")

# Extensões e pastas de destino
TIPOS_DE_ARQUIVO = {
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".pptx"],
    "Vídeos": [".mp4", ".mov", ".avi"],
    "Áudios": [".mp3", ".wav"],
    "Compactados": [".zip", ".rar", ".7z"],
    "Executáveis": [".exe", ".msi", ".sh", ".bat"],
    "Scripts Python": [".py"],
}


def organizar_pasta(pasta):
    for arquivo in os.listdir(pasta):
        caminho_completo = os.path.join(pasta, arquivo)

        if os.path.isfile(caminho_completo):
            _, extensao = os.path.splitext(arquivo)
            movido = False

            for categoria, extensoes in TIPOS_DE_ARQUIVO.items():
                if extensao.lower() in extensoes:
                    destino = os.path.join(pasta, categoria)
                    os.makedirs(destino, exist_ok=True)
                    shutil.move(caminho_completo, os.path.join(destino, arquivo))
                    print(f"Movido: {arquivo} → {categoria}/")
                    movido = True
                    break

            if not movido:
                outros = os.path.join(pasta, "Outros")
                os.makedirs(outros, exist_ok=True)
                shutil.move(caminho_completo, os.path.join(outros, arquivo))
                print(f"Movido: {arquivo} → Outros/")


if __name__ == "__main__":
    print(f"Organizando: {PASTA_ALVO}")
    organizar_pasta(PASTA_ALVO)
    print("Organização concluída!")
