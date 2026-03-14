# Roadmap do Pitão 🐍

Este documento descreve as melhorias planejadas para o Pitão, focando na expansão da tradução de elementos Python para Português.

## ✅ Já Implementado

### Keywords (53 palavras-chave)
Todas as palavras-chave principais do Python já estão traduzidas:

| Português | Python | Categoria |
|-----------|--------|-----------|
| `Falso`, `Verdadeiro`, `Nulo` | `False`, `True`, `None` | Valores |
| `e`, `ou`, `nao` | `and`, `or`, `not` | Operadores Lógicos |
| `se`, `senaose`, `senao` | `if`, `elif`, `else` | Controle de Fluxo |
| `para`, `enquanto`, `quebre`, `continue` | `for`, `while`, `break`, `continue` | Loops |
| `def`, `classe`, `retorne`, `produza` | `def`, `class`, `return`, `yield` | Definições |
| `tente`, `exceto`, `finalmente`, `levante` | `try`, `except`, `finally`, `raise` | Exceções |
| `assincrono`, `aguarde` | `async`, `await` | Async |
| `importe`, `de`, `como` | `import`, `from`, `as` | Imports |
| `em`, `eh`, `com` | `in`, `is`, `with` | Outros |
| `afirme`, `del`, `global`, `naolocal`, `lambda`, `passe` | `assert`, `del`, `global`, `nonlocal`, `lambda`, `pass` | Outros |

## 🎯 Próximas Fases

### Fase 1: Funções Built-in Essenciais (Prioridade Alta)

Traduzir as funções mais comumente usadas:

#### 1.1 I/O e Interação
- [ ] `print()` → `imprimir()`
- [ ] `input()` → `entrada()`
- [ ] `open()` → `abrir()`

#### 1.2 Conversão de Tipos
- [ ] `int()` → `inteiro()`
- [ ] `float()` → `flutuante()`
- [ ] `str()` → `texto()`
- [ ] `bool()` → `booleano()`
- [ ] `list()` → `lista()`
- [ ] `dict()` → `dicionario()`
- [ ] `set()` → `conjunto()`
- [ ] `tuple()` → `tupla()`

#### 1.3 Funções de Sequência
- [ ] `len()` → `tamanho()`
- [ ] `range()` → `intervalo()`
- [ ] `enumerate()` → `enumerar()`
- [ ] `zip()` → `juntar()`
- [ ] `sorted()` → `ordenado()`
- [ ] `reversed()` → `invertido()`
- [ ] `sum()` → `soma()`
- [ ] `max()` → `max()`
- [ ] `min()` → `min()`

#### 1.4 Funções de Iteração
- [ ] `map()` → `mapear()`
- [ ] `filter()` → `filtrar()`
- [ ] `all()` → `todos()`
- [ ] `any()` → `algum()`

### Fase 2: Funções Built-in Intermediárias (Prioridade Média)

#### 2.1 Inspeção e Tipo
- [ ] `type()` → `tipo()`
- [ ] `isinstance()` → `ehinstancia()`
- [ ] `issubclass()` → `ehsubclasse()`
- [ ] `hasattr()` → `tematributo()`
- [ ] `getattr()` → `obteratributo()`
- [ ] `setattr()` → `defatributo()`
- [ ] `delattr()` → `delatributo()`
- [ ] `dir()` → `diretorio()`
- [ ] `vars()` → `variaveis()`
- [ ] `id()` → `identificador()`

#### 2.2 Matemática e Numérica
- [ ] `abs()` → `absoluto()`
- [ ] `round()` → `arredondar()`
- [ ] `divmod()` → `divmod()`
- [ ] `pow()` → `potencia()`

#### 2.3 Representação
- [ ] `repr()` → `representacao()`
- [ ] `format()` → `formatar()`
- [ ] `ascii()` → `ascii()`
- [ ] `bin()` → `binario()`
- [ ] `hex()` → `hexadecimal()`
- [ ] `oct()` → `octal()`
- [ ] `chr()` → `caractere()`
- [ ] `ord()` → `codigo()`

#### 2.4 Iteradores
- [ ] `iter()` → `iterador()`
- [ ] `next()` → `proximo()`

### Fase 3: Funções Built-in Avançadas (Prioridade Baixa)

#### 3.1 Programação Avançada
- [ ] `eval()` → `avaliar()`
- [ ] `exec()` → `executar()`
- [ ] `compile()` → `compilar()`
- [ ] `globals()` → `globais()`
- [ ] `locals()` → `locais()`
- [ ] `callable()` → `chamavel()`

#### 3.2 Orientação a Objetos
- [ ] `super()` → `super()`
- [ ] `classmethod()` → `metodoclasse()`
- [ ] `staticmethod()` → `metodoestatico()`
- [ ] `property()` → `propriedade()`
- [ ] `object()` → `objeto()`

#### 3.3 Bytes e Memória
- [ ] `bytes()` → `bytes()`
- [ ] `bytearray()` → `vetor_bytes()`
- [ ] `memoryview()` → `visao_memoria()`

#### 3.4 Conjuntos Imutáveis
- [ ] `frozenset()` → `conjunto_congelado()`

#### 3.5 Utilitários
- [ ] `hash()` → `hash()`
- [ ] `help()` → `ajuda()`
- [ ] `__import__()` → `__importar__()`

#### 3.6 Async (Python 3.10+)
- [ ] `aiter()` → `aiterador()`
- [ ] `anext()` → `aproximo()`

### Fase 4: Atributos e Métodos Especiais (Dunder Methods)

Traduzir os métodos mágicos mais comuns:

- [ ] `__init__` → `__iniciar__`
- [ ] `__str__` → `__texto__`
- [ ] `__repr__` → `__repr__`
- [ ] `__len__` → `__tamanho__`
- [ ] `__add__` → `__adic__`
- [ ] `__sub__` → `__sub__`
- [ ] `__mul__` → `__mul__`
- [ ] `__truediv__` → `__div__`
- [ ] `__eq__` → `__igual__`
- [ ] `__lt__` → `__menor__`
- [ ] `__gt__` → `__maior__`
- [ ] `__getitem__` → `__obteritem__`
- [ ] `__setitem__` → `__defitem__`
- [ ] `__delitem__` → `__delitem__`
- [ ] `__iter__` → `__iterador__`
- [ ] `__next__` → `__proximo__`
- [ ] `__enter__` → `__entrar__`
- [ ] `__exit__` → `__sair__`
- [ ] `__call__` → `__chamar__`
- [ ] `__name__` → `__nome__`
- [ ] `__main__` → `__principal__`
- [ ] `__file__` → `__arquivo__`
- [ ] `__doc__` → `__doc__`

### Fase 5: Biblioteca Padrão Essencial

Traduzir módulos e funções mais usados da biblioteca padrão:

#### 5.1 Módulo `os`
- [ ] `os.path.exists()` → `caminho.existe()`
- [ ] `os.path.join()` → `caminho.juntar()`
- [ ] `os.listdir()` → `listardir()`
- [ ] `os.mkdir()` → `criardir()`
- [ ] `os.remove()` → `remover()`

#### 5.2 Módulo `sys`
- [ ] `sys.argv` → `argumentos`
- [ ] `sys.exit()` → `sair()`
- [ ] `sys.path` → `caminho`

#### 5.3 Módulo `datetime`
- [ ] `datetime.now()` → `agora()`
- [ ] `datetime.today()` → `hoje()`
- [ ] `date` → `data`
- [ ] `time` → `hora`

#### 5.4 Módulo `math`
- [ ] `math.sqrt()` → `raizquadrada()`
- [ ] `math.pi` → `pi`
- [ ] `math.ceil()` → `teto()`
- [ ] `math.floor()` → `piso()`

#### 5.5 Módulo `random`
- [ ] `random.random()` → `aleatorio()`
- [ ] `random.choice()` → `escolher()`
- [ ] `random.randint()` → `intaleatorio()`

#### 5.6 Módulo `json`
- [ ] `json.loads()` → `carregartexto()`
- [ ] `json.dumps()` → `despejartexto()`
- [ ] `json.load()` → `carregar()`
- [ ] `json.dump()` → `despejar()`

#### 5.7 Módulo `re` (Regex)
- [ ] `re.match()` → `combinar()`
- [ ] `re.search()` → `buscar()`
- [ ] `re.findall()` → `encontrartodos()`
- [ ] `re.sub()` → `sub()`

### Fase 6: Tipos de Exceção

Traduzir as exceções mais comuns:

- [ ] `Exception` → `Excecao`
- [ ] `ValueError` → `ErroValor`
- [ ] `TypeError` → `ErroTipo`
- [ ] `KeyError` → `ErroChave`
- [ ] `IndexError` → `ErroIndice`
- [ ] `AttributeError` → `ErroAtributo`
- [ ] `NameError` → `ErroNome`
- [ ] `FileNotFoundError` → `ErroArquivoNaoEncontrado`
- [ ] `ZeroDivisionError` → `ErroDivisaoPorZero`
- [ ] `ImportError` → `ErroImportacao`
- [ ] `RuntimeError` → `ErroExecucao`
- [ ] `NotImplementedError` → `NaoImplementado`
- [ ] `StopIteration` → `PararIteracao`
- [ ] `KeyboardInterrupt` → `InterrupcaoTeclado`

### Fase 7: Métodos de String

Traduzir métodos comuns de string:

- [ ] `str.upper()` → `maiuscula()`
- [ ] `str.lower()` → `minuscula()`
- [ ] `str.capitalize()` → `capitalizar()`
- [ ] `str.title()` → `titulo()`
- [ ] `str.strip()` → `removerespacos()`
- [ ] `str.split()` → `dividir()`
- [ ] `str.join()` → `juntar()`
- [ ] `str.replace()` → `substituir()`
- [ ] `str.find()` → `encontrar()`
- [ ] `str.startswith()` → `comecacom()`
- [ ] `str.endswith()` → `terminacom()`
- [ ] `str.isdigit()` → `ehdigito()`
- [ ] `str.isalpha()` → `ehalfa()`
- [ ] `str.isalnum()` → `ehalfanum()`

### Fase 8: Métodos de Lista

Traduzir métodos comuns de lista:

- [ ] `list.append()` → `adicionar()`
- [ ] `list.extend()` → `estender()`
- [ ] `list.insert()` → `inserir()`
- [ ] `list.remove()` → `remover()`
- [ ] `list.pop()` → `retirar()`
- [ ] `list.clear()` → `limpar()`
- [ ] `list.index()` → `indice()`
- [ ] `list.count()` → `contar()`
- [ ] `list.sort()` → `ordenar()`
- [ ] `list.reverse()` → `inverter()`
- [ ] `list.copy()` → `copiar()`

### Fase 9: Métodos de Dicionário

Traduzir métodos comuns de dicionário:

- [ ] `dict.keys()` → `chaves()`
- [ ] `dict.values()` → `valores()`
- [ ] `dict.items()` → `itens()`
- [ ] `dict.get()` → `obter()`
- [ ] `dict.pop()` → `retirar()`
- [ ] `dict.update()` → `atualizar()`
- [ ] `dict.clear()` → `limpar()`
- [ ] `dict.copy()` → `copiar()`
- [ ] `dict.setdefault()` → `definirpadrao()`

## 🔧 Implementação Técnica

### Desafios

1. **Compatibilidade com Bibliotecas**: Bibliotecas externas usam nomes em inglês
2. **Mapeamento Bidirecional**: Necessário para `pt2py` e `py2pt`
3. **Métodos de Objetos**: Requer análise de contexto mais sofisticada
4. **Performance**: Tradução em tempo real precisa ser rápida
5. **Documentação**: Manter docs sincronizadas com traduções

### Abordagens Possíveis

#### Opção 1: Aliases em Runtime (Mais Simples)
Criar um módulo `pitao.builtins` que exporta aliases:

```python
# pitao/builtins.py
imprimir = print
entrada = input
tamanho = len
# ...
```

**Vantagens**: Simples, compatível com Python puro  
**Desvantagens**: Requer `de pitao.builtins importe *`

#### Opção 2: Preprocessamento (Atual)
Expandir o parser atual para traduzir funções built-in:

```python
# Em parser.py
BUILTIN_FUNCTIONS = {
    "imprimir": "print",
    "entrada": "input",
    "tamanho": "len",
    # ...
}
```

**Vantagens**: Consistente com abordagem atual  
**Desvantagens**: Mais complexo para métodos de objetos

#### Opção 3: Híbrida (Recomendada)
- **Keywords e built-ins**: Preprocessamento
- **Métodos de objetos**: Wrappers em runtime
- **Biblioteca padrão**: Módulo `pitao.std` com aliases

### Estratégia de Rollout

1. **Fase 1-3**: Implementar via preprocessamento (expandir `parser.py`)
2. **Fase 4**: Criar sistema de tradução de dunder methods
3. **Fase 5-9**: Criar módulos wrapper (`pitao.std`, `pitao.tipos`)

## 📚 Recursos Educacionais

### Documentação
- [ ] Tutorial completo em português
- [ ] Guia de migração Python → Pitão
- [ ] Referência de API traduzida
- [ ] Exemplos práticos por categoria

### Ferramentas
- [ ] Extensão VS Code melhorada (syntax highlighting completo)
- [ ] REPL interativo em português
- [ ] Linter com mensagens em português
- [ ] Jupyter kernel para Pitão

### Comunidade
- [ ] Site oficial com playground online
- [ ] Repositório de exemplos
- [ ] Fórum/Discord para discussões
- [ ] Contribuições da comunidade

## 🎓 Casos de Uso

### Educação
- Ensino de programação para falantes de português
- Redução da barreira linguística para iniciantes
- Material didático em português

### Prototipagem Rápida
- Scripts rápidos em português
- Automação de tarefas
- Data science exploratória

## 🤝 Como Contribuir

1. Escolha uma fase do roadmap
2. Implemente as traduções
3. Adicione testes
4. Atualize a documentação
5. Abra um Pull Request

## 📝 Notas

- Manter compatibilidade com Python 3.8+
- Priorizar clareza sobre brevidade nas traduções
- Aceitar tanto português brasileiro quanto europeu quando possível
- Manter nomes em inglês como aliases válidos para compatibilidade

---

**Última atualização**: Março 2026  
**Versão**: 0.2.x
