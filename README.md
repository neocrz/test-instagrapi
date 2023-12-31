# test-instagrapi
Código de teste de utilização do [instagrapi](https://github.com/subzeroid/instagrapi). O Instagrapi é uma API não oficial do [Instagram](https://www.instagram.com).

## Utilização
Para utilizar o instagrapi na configuração deste repositório, é necessário realizar o login com uma conta do instagram. 

**Esse código é disponibilizado sem nenhum tipo de garantia! A sua utilização é por conta e risco do próprio usuário.**

As etapas a seguir contém orientações para criação de um ambiente capaz de rodar o código presente no arquivo `exemplo.py` deste repositório.

### Dependências

É necessário ter o [Git](https://git-scm.com/) e [Python](https://www.python.org/) instalados, disponíveis e configurados para realizar o clone do repositório, a criação do ambiente (`venv`) e a utilização do `pip`.

Com o auxílio de um terminal, execute os comandos a seguir.

#### Clonar o repositório

```console
git clone https://github.com/neocrz/test-instagrapi
```

#### Acessar a pasta clonada

```console
cd test-instagrapi
```
#### Criar um ambiente Python.

```console
python -m venv venv
```
#### Ativar o ambiente Python

Linux
```console
source ./venv/bin/activate
```

Windows (PowerShell)
```console
.\venv\Scripts\Activate.ps1
```

Windows (Command Prompt)
```console
.\venv\Scripts\activate.bat
```
#### Instalar as dependências.
```console
pip install -r requirements.txt
```

### Obtenção do `sessionid`
Neste código experimental, o login do Instagram é realizado por meio de um `sessionid` válido, presente em navegadores com seções logadas no Instagram.

O exemplo a seguir foi realizado utilizando o navegador [Firefox](https://www.mozilla.org/pt-BR/firefox/new/) em Sistema Operacional [GNU/Linux](https://pt.wikipedia.org/wiki/GNU/Linux) ([Linux Mint](https://linuxmint.com/)). As etapas tomadas podem ser diferentes para outros ambientes e navegadores.

1. No navegador Firefox, com a aba do instagram aberta e com seção logada, pressione `F12` e acesse a seção de "Armazenamento".
2. Na seção de "Armazenameto", acesse a aba de "Cookies".
3. Na aba de "Cookies", encontre o *cookie* por nome `sessionid` e copie seu valor.
4. Renomeie (ou copie/crie em novo arquivo) o arquivo `.env_exemplo` deste repositório para `.env`
5. Dentro do arquivo `.env` adicione o valor obtido de `sessionid` após o texto `INSTA_SESSION_ID=`.


### Execução
No arquivo `exemplo.py` exite um código que utiliza-se de funções de apoio para demonstrar uma pequena parte da capacidade do instagrapi. Na atual configuração, a execução deste arquivo têm por objetivo obter informações de 15 posts do perfil do [Instagram](https://www.instagram.com/instagram/) e criar um arquivo csv no mesmo diretório, que contém parte das informações referentes aos 15 posts acessados.

Para executar o código é só executar:

```console
python exemplo.py
```

## Observações
Uma alternativa para etapa 5 da seção sobre o `sessionid` seria exportar a variável `INSTA_SESSION_ID` diretamente no ambiente de execução, evitando inserção desses dados diretamente em arquivos.

É aconselhável a remoção da seção do `sessionid` após a utilização do código. Essa remoção pode ser realizada excluindo o *cookie* do `sessionid` (seguindo o caminho das instruções 1-3) ou fazendo o *logout* da conta do Instagram no navegador que contém o *cookie*.

## Code Info

#### `data_to_csv(data: dict) -> None`
- Recebe um dicionário `data` e cria um arquivo csv no diretório atual.



#### `download_media(username: str, qtdmedia: int, output: str = None) -> dict`
- Baixa a quantidade de posts conforme `qtdmedia` do perfil `username` e salva em `save_path` ou no diretório atual se o valor de `save_path` for `None`
- Retorna um dicionário contendo os dados das *medias*.


#### `getinfo_media(username: str, qtdmedia: int) -> dict`
- Retorna um dicionário de informações das *medias* de acordo com a quantidade de posts conforme `qtdmedia` do perfil `username`.