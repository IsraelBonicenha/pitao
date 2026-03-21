# Pitão 🐍

<p align="center">
  <img src="https://raw.githubusercontent.com/ivancrneto/pitao/main/pitao.jpg" alt="Pitão Logo" width="200"/>
</p>

**Python com palavras reservadas em Português!**

Pitão é um preprocessador Python que permite escrever código usando palavras reservadas em Português. Inspirado no [Bython](https://github.com/mathialo/bython).

## Instalação

```bash
pip install pitao
```

Ou para instalar localmente com `uv`:

```bash
git clone https://github.com/ivancrneto/pitao.git
cd pitao
uv sync
```

## Galeria

![Sintaxe Básica](https://raw.githubusercontent.com/ivancrneto/pitao/main/vscode-pitao/assets/pitao1.png)
![Controle de Fluxo](https://raw.githubusercontent.com/ivancrneto/pitao/main/vscode-pitao/assets/pitao2.png)
![Classes e Funções](https://raw.githubusercontent.com/ivancrneto/pitao/main/vscode-pitao/assets/pitao3.png)

## Exemplo de Código

Pitão suporta arquivos com extensão `.pt` ou `.pit`:

```python
# ola_mundo.pt (ou ola_mundo.pit)
def ola_mundo():
    imprimir("Olá, Mundo!")

se __nome__ == "__principal__":
    ola_mundo()
```

Execute com:

```bash
pitao ola_mundo.pt
# ou
pitao ola_mundo.pit
```

## Palavras Reservadas

| Português | Python | | Português | Python |
|-----------|--------|---|-----------|--------|
| `Falso` | `False` | | `importe` | `import` |
| `Nulo` | `None` | | `em` | `in` |
| `Verdadeiro` | `True` | | `eh` | `is` |
| `e` | `and` | | `nao` | `not` |
| `ou` | `or` | | `passe` | `pass` |
| `se` | `if` | | `retorne` | `return` |
| `senaose` | `elif` | | `tente` | `try` |
| `senao` | `else` | | `exceto` | `except` |
| `para` | `for` | | `finalmente` | `finally` |
| `enquanto` | `while` | | `levante` | `raise` |
| `quebre` | `break` | | `com` | `with` |
| `continue` | `continue` | | `produza` | `yield` |
| `def` | `def` | | `assincrono` | `async` |
| `classe` | `class` | | `aguarde` | `await` |
| `del` | `del` | | `afirme` | `assert` |
| `de` | `from` | | `como` | `as` |
| `global` | `global` | | `naolocal` | `nonlocal` |

## Comandos

### `pitao` - Executar arquivos Pitão

```bash
pitao arquivo.pt [args...]     # Executa o arquivo
pitao -c arquivo.pt            # Compila para .py sem executar
pitao -k arquivo.pt            # Executa e mantém o .py gerado
pitao -v arquivo.pt            # Modo verbose
```

### `pt2py` - Traduzir Pitão para Python

```bash
pt2py arquivo.pt               # Cria arquivo.py
pt2py -o saida.py arquivo.pt   # Especifica nome de saída
```

### `py2pt` - Traduzir Python para Pitão

```bash
py2pt arquivo.py               # Cria arquivo.pt
py2pt -o saida.pt arquivo.py   # Especifica nome de saída
```

## Licença

MIT
