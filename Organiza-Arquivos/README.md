# 🐍 Python-Automacao

Automação simples e poderosa usando Python para organizar seus arquivos automaticamente.  
Ideal para manter sua pasta de **Downloads** limpa e categorizada com apenas um clique. 🚀

---

## 📁 Projeto: `Organiza_Arquivos`

Este script move arquivos da pasta especificada para subpastas organizadas por tipo (extensão).  
Uma solução prática para quem lida com muitos arquivos diariamente.

---

## ⚙️ Como usar

### 1️⃣ Clone o repositório

```bash
git clone https://github.com/seu-usuario/Python-Automacao.git
cd Python-Automacao/Organiza_Arquivos
```

### 2️⃣ Execute o script

> Por padrão, o script organiza a pasta `~/Downloads`.

```bash
python app.py
```

📂 O script criará subpastas como:
- `Imagens/`
- `Documentos/`
- `Vídeos/`
- `Áudios/`
- `Compactados/`
- `Executáveis/`
- `Scripts Python/`
- `Outros/`

---

## ✏️ Personalização

Você pode editar o caminho da pasta alvo no topo do `app.py`:

```python
PASTA_ALVO = os.path.expanduser("~/Downloads")
```

Altere para qualquer pasta que deseje organizar.

---

## 🧠 Tecnologias utilizadas

- Python 3.x
- Módulos padrão: `os`, `shutil`

---

## 🧰 Melhorias futuras (em andamento)

- Interface de linha de comando (CLI) com argumentos personalizados ✅
- Agendamento automático via cron/tarefa agendada 🕒
- Logs detalhados da organização 📊

---

## 💡 Exemplos visuais (em breve)

Imagens e gifs de uso real do script organizando arquivos!

---

## 🧑‍💻 Autor

Desenvolvido por [Seu Nome](https://github.com/seu-usuario) 💻  
Sinta-se livre para contribuir, sugerir melhorias ou reportar problemas!

---

## ⭐️ Contribua com o projeto!

Se este script te ajudou, deixe uma estrela ⭐ no repositório!  
Isso ajuda muito a manter e melhorar projetos open source como este!
