# test-instagrapi
Código de teste de utilização do [instagrapi](https://github.com/subzeroid/instagrapi). O Instagrapi é uma API não oficial do [Instagram](https://www.instagram.com).

## Utilização
Para utilizar o instagrapi na configuração deste repositório, é necessário realizar o login com uma conta do instagram. 

**Esse código é disponibilizado sem nenhum tipo de garantia! A sua utilização é por conta e risco do próprio usuário.**

As etapas a seguir contém orientações para criação de um ambiente capaz de rodar o código presente no arquivo `exemplo.py` deste repositório.

### Dependencias

É necessário ter o [Python](https://www.python.org/) instalado e disponível.

Com o auxilio de um terminal, execute os comandos a seguir.
#### Clonar o repositório

```console
git clone https://github.com/neocrz/test-instagrapi
```

#### Acessar a pasta clonada

```
cd test-instagrapi
```
#### Criar um ambiente do Python.

```console
python -m venv venv
```
#### Ativar o ambiente Python

Linux
```console
souce ./venv/bin/activate
```

#### Instalar as dependencias.
```console
pip install -r requirements.txt
```

### Obtenção do `sessionid`
Neste código experimental, foi realizado o login do instagram por meio da `sessionid` presente em navegadores com seções logadas no instagram.

O exemplo a seguir foi realizado utilizando o navegador [Firefox](https://www.mozilla.org/pt-BR/firefox/new/) em Sistema Operacional [GNU/Linux](https://pt.wikipedia.org/wiki/GNU/Linux) ([Linux Mint](https://linuxmint.com/)). As etapas tomadas podem ser diferentes para outros ambientes e navegadores.

1. No navegador Firefox, com a aba do instagram aberta e com seção logada, pressione `F12` e acesse a seção de "Armazenamento".
2. Na seção de "Armazenameto", acesse a aba de "Cookies".
3. Na aba de "Cookies", encontre o cookie por nome `sessionid` e copie seu valor.
4. Renomeie (ou copie/crie em novo arquivo) o arquivo `.env_exemplo` deste repositório para `.env`
5. Dentro do arquivo `.env` adicione o valor obtido de `sessionid` apos o texto `INSTA_SESSION_ID=` na mesma linha do mesmo. (substitua `SUBSTITUA_ESSE_TEXTO_PELO_SESSIONID` pelo valor da `sessionid`).

### Execução
No arquivo `exemplo.py` exite um código que utiliza-se de funções de apoio para demonstrar uma pequena parte da capacidade do instagrapi. Na atual configuração, a execução deste arquivo tem por objetivo obter informações de 15 posts do perfil do [instagram](https://www.instagram.com/instagram/) e criar um arquivo csv no mesmo diretório, que contem parte das informações referentes aos 15 posts acessados.

Para executar o código é só executar:

```console
python exemplo.py
```

## Info
### `data_to_csv` 
#### `data_to_csv(data: dict) -> None`
- Recebe um dicionário `data` e cria um arquivo csv no diretório atual.


### `download_media` 
#### `download_media(username: str, qtdmedia: int, output: str = None) -> dict`
- Baixa e salva a quantidade de posts conforme `qtdmedia` do perfil `username` e Salva em `save_path` ou no diretório atual se o valor de `save_path` for `None`
- Retorna um dicionário contendo os dados das medias.

### `getinfo_media` 
#### `getinfo_media(username: str, qtdmedia: int) -> dict`
- Retorna um dicionário de informações das medias de acordo com a quantidade de posts conforme `qtdmedia` do perfil `username`.