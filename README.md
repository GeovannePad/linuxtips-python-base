# Repositório de códigos e anotações do curso de python base da linuxtips

## Introdução a programação e ao Python - Day 1

### Linguagens de programação

__Input e Output (I/O)__

__Input:__ envia dados para a unidade computacional, instruções
__Output:__ recebe dados processados do computador, em diversos formatos

__Binário:__ principal componente de um computador. Os digitos 1 e 0,
1: ligado
0: desligado

__Padronização em formato de bits para se comunicar com a máquina__
Conjunto de 8, 16, 32 bits, formando mensagens específicas

Exemplo: letra A = 65 = 1 000001

__Linguagem de programação:__ abstração, forma mais natural ao entendimento humano de escrever, aprender e memorizar.

- __Linguagem de baixo nível (Assembly):__ nível mais próximo ao processador/hardware
- __Linguagem de médio nível (C):__ camada nem tanto abstrata e nem tão próxima do processador/hardware
- __Linguagem de alto nível (Python):__ camada mais abstrata, mais fácil para programar.

Uma linguagem de alto nível é convertida para o nível médio e depois então para o baixo nível.

__Linguagens compiladas:__ escreve o programa e o programa precisa estar todo correto do início ao fim. O compilador junta toda a lógica e forma um tipo "pacote" para executar o software. (simplificado)

__Linguagens interpretadas:__ cada comando/linha é interpretado de forma individual. 

__O código compilado para funcionar em diferentes sistemas operacionais é necessário compilar um pacote para cada sistema.__ Já o __código interpretado geralmente é multi plataforma pois ele é interpretado na hora que é executado.__

__Programa:__ conjunto de instruções colocados de forma organizada em um ou mais arquivos e que podem ser executados várias vezes obtendo os mesmos resultados. Existem 2 categorias de programas:

- __Programas compilados:__ exigem que todas as linhas de código sejam avaliadas e validadas antes do programa executável ser gerado já na linguagem de máquina e no momento da execução o programa está todo pronto para rodar.
- __Programas interpretados:__ aqueles que podem ser escritos em arquivos mas são avaliados linha a linha, bloco a bloco, sem a necessidade de o programa inteiro estar avaliado, cada instrução é lida e logo em seguida interpreta e executada, tornando mais fácil e mais dinâmica a programação, mas pode ser também mais suscetível a erros.

__Python é uma linguagem dinâmica e interpretada.__

### Como está organizada a plataforma Python

__Python é uma plataforma formada por uma série de componentes.__

__PLR - Python Language Reference__

 - Documento contendo toda a especificação da linguagem, extenso conjunto de textos escrito pelo criador do Python.
 - Regras gramaticais da linguagem.
 - Palavras reservadas.
 - Todos os comportamentos esperados de uma implementação de Python.

__Implementação__

__CPython__ - Implementação oficial escrita em linguagem C do Python

A partir da PLR se cria uma implementação do Python, essa especificação é programada com o objetivo de interpretar e executar programas Python, como:
- IronPython (.NET)
- Jython (Java Virtual Machine)
- PyPy (escrito em Python para ser mais rápido)
- Stackless Python (CPython com suporte microthreads)
- MicroPython (micro controllers)

__Ecossistema__

__Tudo em torno da linguagem Python__
- Comunidades
- PSF (Python Software Foundation)
- Pacotes e ferramentas
- pypi.org (Python Package Index), através da ferramenta `pip` que se instala os pacotes.

### Instalação do Python e preparação do ambiente

__Executar comandos Python no terminal:__ `python -c "comando"`

Python como uma entidade e você "conversa" com ele, sempre vai ter uma resposta.

Valores que o Python compreende mas não sabe tomar uma ação são chamados de __literais__.


`python -m site`, módulo que mostra como o Python que está sendo usado está instalado. Para executar outros módulos: `python -m nome_do_modulo`.
`python --version`: mostra versão instalada do Python
`python -VV`: mostra a versão instalada e o momento em que o Python foi compilado.
`python --help`: mostra a guia de ajuda.
`python`: terminal interativo do Python (interpretador).
`python -m turtledemo`, pacote gráfico com exemplos

No interpretador Python, ele sempre vai imprimir os comandos inseridos.

__REPL - read-eval-print loop__ (laço de leitura, execução e impressão)

### Introdução ao git e seu primeiro script Python

__Script Python é um arquivo aonde se tem comandos__, cada linha para o interpretador é entendido como um comando diferente. Arquivo isolado que pode ser executado isoladamente.

- __Shebang (ambientes Linux):__ comentário especial, sempre na primeira linha, usado para especificar um interpretador específico para o progrmama.

`which python`: mostra o caminho do python que o sistema está usando.
`mv nome_arquivo nome_novo`: renomeia um arquivo

### Criando um programa que lê variáveis de ambiente

`env`: mostra a lista de todas as variáveis do ambiente.
`env | grep variavel_ambiente`: grep é uma ferramenta de filtragem do linux.
`export variavel_ambiente`: altera o valor de uma variável de ambiente.
`unset variavel_ambiente`: exclui uma variável de ambiente.
`variavel_ambiente script`: força um script a atualizar um determinado valor de uma determinada variável de ambiente.

__Variáveis de Ambiente__

Termo usado para referir ao local onde o programa é executado, o ambiente em termos gerais é formado por um shell que pode ser entendido como um local isolado onde o seu programa executa.
Neste ambiente existem variáveis que servem para configurar o comportamento do próprio ambiente, do sistema e dos programas que rodam.

__Condicionais:__ define um teste e sempre se usa junto com uma expressão de comparação.

__Guia de estilo do python:__ pep8.org

Manter 80 colunas por linha, uma boa prática.

- __Snake case =__ current_language
- __Pascal Case =__ CurrentLanguage

__Built-in:__ algo que já vem imbutido na linguagem.
__Biblioteca padrão:__ tudo aquilo que já vem instalado por padrão no Python.

### Tipos de instruções: expressions, statements, assignment

Tipos de instruções que podem ser passadas para o interpretador do Python.

- __Expression/Expressão:__ instrução que espera um valor de retorno. Exemplo: 1 + 1
- __Statement/Declaração:__ instrução que prepara o interpretador para uma determinada tarefa mas não retorna valor, normalmente acompanhado de uma expressão. Exemplo: if, else, for, while, pass
- __Assignment/Atribuição:__ intrução que pega o retorno de uma expressão e processa o seu valor com intuito de armazenar. Exemplo: soma = 40 + 2, soma += 3

__Protocolo:__ o que o objeto é capaz de fazer.

__A precedência de operadores no Python__

Além da precedência de operadores aritméticos PEMDAS também existe a tabela de precedência de operadores da própria linguagem:

|   __Nível__  |   __Categoria__   |   __Operadores__   |
|:--------:|:-------------:|:---------------:|
|  7(alto) | Exponenciação |        **       |
|     6    | Multiplicação |     *,/,//,%    |
|     5    |     Adição    |       +,-       |
|     4    |   Relacional  | ==,!=,<=,>=,>,< |
|     3    |     Lógico    |       not       |
|     2    |     Lógico    |       and       |
| 1(baixo) |     Lógico    |        or       |

### Bloco de código e identação

Linguagem fácil de ser entendida por pessoas que não são programadores.

Tarefa: fazer compras
Lista de compras, categorias/blocos

__Blocos de código lógicos:__ possui um escopo definido.
Os ":" inidica um início de um bloco de código, sendo o recúo obrigatório.

__Identação:__ termo usado para a formatação da lista de compras por exemplo, após cada categoria ou seção colocamos um recuo antes de começar o conteúdo.

### Ambientes virtuais e ferramenta iPython

__Ambiente real:__ ambiente onde se encontra o Python do sistema operacional.

__Ambientes virtuais__

- É uma sandbox, é uma cópia de todo o ambiente Python.
- Garante que as dependências e o programa como um todo funcione de forma igual e correta em qualquer computador, evitando conflitos e danos. Cada projeto terá um ambiente virtual.

__Convenção Linux:__ Todo arquivo/pasta que tem um ponto no início é um arquivo/pasta oculto.

`python3.11 -m venv nome_ambiente_virtual`: comando para criar um ambiente virtual. 
`source .venv/bin/activate`: comando para ativar um ambiente virtual no Linux bash.
`deactivate`: comando para sair do ambiente virtual

__Pip:__ busca pacotes em repositórios para ser instalado no Python. Busca em pypi.org

__iPython:__ interpretador Python com mais ferramentas e colorido.

`%time função`: comando do iPython que demonstra o uso do CPU para executar determinada função.

## Tipos de dados e protocolos - Day 2

### A importância dos tipos de dados e o tipo inteiro

Classe, categoria e tipo são as mesmas coisas. Apesar de terem suas diferenças. 

`bin(numero_inteiro)`: função que mostra a versão binária de determinado número inteiro.
`chr(numero_inteiro)`: função que retorna um caractere referente a um número inteiro.
`id(variavel)`: função que retorna a posição na memória RAM de uma determinada variável.
`type(variavel)`: função que retorna o tipo de dado de uma variável.

__Todo objeto do Python possui as mesmas características__, um objeto contém um endereço de memória, que contém um tipo/classe/categoria e um valor.

__Através do tipo de dado que o Python consegue saber qual informação você quer__, sendo um número, uma letra ou outras coisas.

Através do tipo que é possível converter um dado em uma informação.

__Tipos de dados primários (Scalar Types)__

__Utilizados para armazenar uma única unidade de informação como por exemplo um número ou um texto__ Exemplo: `numero = 65`, um número inteiro.

`int(valor)`: força a um valor a ser do tipo inteiro.

`dir(tipo_de_dado)`: função que retorna a implementação do objeto, tudo que é possível ser feito com objetido de um determinado tipo de dado.

- __Métodos públicos:__ métodos que não possuem dunder, podem ser usados diretamente.
- __Protocolos:__ métodos dunder/especiais, determina uma operação que um objeto dentro de um tipo de dado pode tomar, só o Python deve usar, nós devemos usar abstrações que por baixo chamaram esses métodos, exemplos:

`__add__()`: implementa o protocolo de adição, sendo um objeto Aditivel. Exemplo: `numero.__add__(1) = numero + 1`.
`__sub__()`: implementa o protocolo de subtração, sendo um objeto redutivel. Exemplo: `numero.__sub__(1) = numero - 1`.
`__mul__()`: implementa o protocolo de multiplicação, sendo um objeto multiplicável. Exemplo: `numero.__mul__(2) = numero * 2`.
`__eq__()`: implementa o protocolo de equilidade. Exemplo: `numero.__eq__(2) = numero == 2`.

- __Tipo inteiro:__ armazena os números inteiros em Python e é representado pela classe int.

### Tipos de dados primitivos float, Bool, NoneType

__Tipo de dado Float__

Armazena um valor fracionado, resultados de divisões, um ponto flutuante. Exemplo: `valor = 5 / 2`.

Para trabalhar com valores monetários, em uma aplicação de verdade, usa o tipo de dado Decimal ou Currency.

__Tipo de dado Booleanos__

- __Armazena um valor True (verdade, 1) ou False (falso, 0).__ Serve para criação de flags.
- O if só trabalha com valores Booleanos.
- Qualquer número diferente de 0 ou texto não vazio é considerado True para o Python.
- Usado para apresentar uma sintaxe mais bonita. Mas por baixo o Python interpreta 0 como False e 1 como True.

__Tipo de dado NoneType__

- __Possui apenas uma única opção de valor, "None", significa nulo, ausência de valor.__
- Usado para criar uma variável que não se sabe o valor. Possui um endereçamento de memória e um tipo. O valor da variável pode ser redefinido.
- __NoneType é um objeto Singleton__, durante toda a execução do código, só pode ser criado apenas uma única vez, só pode existir apenas um único objeto.
- Uma função que não tem um retorno explícito sempre irá retornar um valor NoneType.

O próprio Range é um tipo de dado, ele gera um tipo de dado.
__Protocolo Iterable (percorrível)__, pode percorrer cada um dos seus itens e realizar uma operação. For = Para.