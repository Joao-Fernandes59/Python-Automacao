import os
import shutil


def organizar_arquivos(diretorio):
    # Extensões e pastas correspondentes
    extensoes_pastas = {
        '.pdf': 'PDFs',
        '.jpg': 'Imagens',
        '.jpeg': 'Imagens',
        '.png': 'Imagens',
        '.docx': 'Documentos',
        '.xlsx': 'Planilhas',
        '.txt': 'Textos',
        '.mp4': 'Videos',
        '.mp3': 'Músicas'
    }

    # Criar pastas se não existirem
    for pasta in set(extensoes_pastas.values()):
        caminho_pasta = os.path.join(diretorio, pasta)
        if not os.path.exists(caminho_pasta):
            os.makedirs(caminho_pasta)

    # Organizar arquivos
    for arquivo in os.listdir(diretorio):
        # Ignorar pastas
        if os.path.isdir(os.path.join(diretorio, arquivo)):
            continue

        # Obter extensão do arquivo
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()  # garantir minúsculas

        # Mover arquivo para pasta correspondente
        if extensao in extensoes_pastas:
            pasta_destino = extensoes_pastas[extensao]
            origem = os.path.join(diretorio, arquivo)
            destino = os.path.join(diretorio, pasta_destino, arquivo)

            shutil.move(origem, destino)
            print(f'Arquivo {arquivo} movido para {pasta_destino}/')


if __name__ == '__main__':
    # Usar o diretório atual ou especificar outro
    diretorio_alvo = os.getcwd()  # Pode substituir por outro caminho
    print(f'Organizando arquivos em: {diretorio_alvo}')
    organizar_arquivos(diretorio_alvo)
    print('Organização concluída!')
