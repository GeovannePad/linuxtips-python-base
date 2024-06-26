# Linuxtips - Python Base

## Dia 1 - Introdução a programação e ao Python

### Linguagens de Programação

- **Input** -> entrada, envia dados/instruções para a unidade computacional, exemplo: teclado.
- **Output** -> saída, maneira como a informação é disponibiliza, exemplo: monitor.

O computador por ser um dispositivo eletrônico, só entende a linguagem binária (0 e 1).

- 0 significa desligado.
- 1 significa ligado.

Padronização de como as informações são enviadas, feita através dos bits, cada bit representa 0 ou 1. Existindo uma sequência de 8 bits (byte), 16 bits...

Cada byte possui uma "mensagem", exigindo um cálculo na base 2, binária, chegando num número final.

- 10011011 = 155
- Letra "A" = 65 = 1000001

Linguagem de programação é uma abstração, ao olho humano é mais fácil de escrever, tendo um entendimendo melhor. No final o código é convertido para a base binária.

- **Linguagem de baixo nível** -> Assembly
- **Linguagem de médio nível** -> C, é convertida para uma linguagem de baixo nível.
- **Linguagem de alto nível** -> Python, contertida para a linguagem de médio nível.
  - **Linguagens compiladas** -> escreve o programa, e o programa precisa estar todo correto do ínicio ao fim, em pacote, o erro vai ser detectado na execução do programa já compilado.
  - **Linguagens interpretadas** -> significa que cada comando(linha) pode ser interpretado individualmente. O Python é interpretado.

No compilado se tiver um erro em qualquer lugar do código, a compilação vai falhar, e no interpretado uma linha pode funcionar e depois pode ocorrer um erro, por exemplo, no final do programa.

No código compilado, para cada sistema operacional, necessitará de um programa compilado separadamente, enquanto que o interpretado é multiplataforma, podendo o mesmo programa ser executado em diferentes sistemas operacionais.

### Como está organizada a plataforma Python

Componentes da Plataforma Python

Python é um conjunto de coisas.

- **PLR Python Language Reference** -> toda especificação, um documento de design formal da linguagem Python. A partir desse documento é possível criar uma implementação de um programa.

Implementações Python

- **IronPython** -> Python rodando no .NET.
- **Jython** -> Python rodando na Máquina Virtual do Java
- **PyPy** -> implementação do Python reescrito em Python para ficar mais rápido.
- **Stackless** Python -> galho do CPython que suporta multi-threading.
- **MicroPython** -> Python reduzido, rodando em micro controladores, dispositivos embarcados.

**CPython** -> implementação oficial. Escrito usando a Linguagem C

O CPython possui um ecossistema em torno dele, tudo em torno da linguagem Python.

- Comunidades
- PSF -> Python Software Foundation, fundacão que protege a marca Python e possui um código de conduta, também há empresas que se afiliam a fundação.
- APyB -> Fundação Python Brasil.
- Pacotes e ferramentas -> programas Pythons que podem ser reutilizados. E ferramentas para instalar bibliotecas, etc.
- PyPI -> Python Package Index.

### Instalação do Python e preparação do ambiente

- Replit
- Gitpod
- Micro
- Terminator

Comandos Python a partir do terminal

- `python -c "1"` -> não retorna nada, pois não foi instruído como utilizar o número 1, ele entende mas ele não sabe o que fazer, é um valor literal.
- `python -c "print(1)"` -> ele imprime o número 1, pois o interpretador foi instruído a fazer essa ação.
- `python -c "print('giovanni'.upper())"` -> imprime "GIOVANNI" pois a função `upper()` coloca todos os caracteres em maiúsculo.
- `python -m site` -> executa um módulo do Python já pré-definido. Mostra como o Python que está sendo utilizado que está instalado.
- `python -m turtledemo` -> interface gráfica feita em tk com exemplos de jogos e animações
- `python -V` -> mostra a versão do Python.
- `python -VV` -> mostra a versão e a data da última compilação do Python.
- `python --help` -> ajuda do Python.
- `python` -> terminal interativo do Python, é o interpretador padrão. Sempre mostra o output.

<hr>

- **REPL** -> Read Eval Print Loop.

### Introdução ao git e seu primeiro script Python

- **Script** -> é um arquivo de comandos encadeados independente.
- **Sintaxe** -> ordem e regras que as palavras e os comandos devem ser escritos.

**Comentários** -> são ignorados pelo interpretador. Alguns comentários colocados na frente do código podem ser interpretados por algumas ferramentas.

- **Shebang** -> característica do sistema Unix/Linux, é um comentário especial, sempre presente na primeira linha do script, ele serve para identificar qual é o interpretador e a versão do Python que vai ser usada para executar o script.
  - `which python` -> caminho do Python

Um ambiente é um "local" que está preparado para executar o script ou programa Python, que possui acesso ao interpretador e ele tem acesso a informações específicas do ambiente/sistema.

Um ambiente é formado de um shell e as variáveis de ambiente, a maioria dos programas são desenvolvidos orientados a ambiente.

Ao utilizar o SHEBANG apontando para o ambiente, todas as variáveis de ambiente serão fornecidas para o Python. Ao especificar o Python no SHEBANG não será necessário especificar o Python ao executar, pode escrever apenas `./arquivo.py`.

A biblioteca `os` implementa uma função `environ()`, o environ é um Dict Like Object, que não é um dicionário puro, mas implementa seus protocolos e métodos públicos.

### Criando um programa que lê variáveis de ambiente

- É recomendável seguir um guia de estilo para escrever códigos Python. O pep8.
- Para terminal é legal manter 80 colunas de caracteres por linha. Utilizar apenas até a coluna 79, quebrando para a linha de baixo.
- Também é necessário colocar no script/programa são os metadados, que são informações que necessariamente não fazem parte do programa, mas podem serem usadas para informações adicionais. Normalmente são adicionais após o comentário de bloco de explicação do script no início do programa.

`__` -> underline duplos podem ser chamado de Dunder.

O Python executa todo o conteúdo do arquivo mesmo não estando dentro de uma função `main()`.

- Usar snake case ao escrever nomes de variáveis, mas também existe o padrão Pascal Case.
- **Built-in** -> funções, bibliotecas ou ferramentas já implementadas no Python.
- **Biblioteca padrão** -> não está incluso no Python, precisa ser importada, mas já instalada junto com o pacote do Python.

**Fatiamento** -> forma de cortar um texto, exemplo: `string[:5]`, no exemplo, só é retornada os 5 primeiros caracteres da string.

Existe outra maneira de cortar uma string, quebrando a string a partir de um caractere, usando a função `split(caractere)`.

- `unset variavel` -> apaga uma variável de ambiente.
- `export variavel` -> altera o valor de uma variável de ambiente.
- `LANG=pt_BR python3 hello.py` -> exporta uma variável de ambiente diretamente ao executar um script Python, sobrescrevendo o valor padrão do sistema operacional.

### Tipos de Instruções: Expressions, Statements, Assignment

- **Expressão/Expression** -> instrução que espera um valor de retorno. Ex: `1+1`.
- **Declaração/Statement** -> instrução que prepara o interpretador para uma determinada tarefa mas não retorna valor. Ex: `if, else, def, for`.
- **Atribuição/Assignment** -> instrução que pega o retorno de uma expressão e processa o seu valor com intuito de armazenar. Ex: `soma = 40 + 2, soma += 3, soma -= 3`.

**Protocolos** -> o que o objeto é capaz de fazer.

O interpretador executa a linha sempre da esquerda para direita.

Precedência de operadores aritméticos (PEMDAS)

1. Parênteses.
2. Exponenciação e Raízes.
3. Multiplicação
4. Divisão.
5. Adição.
6. Subtração.

Precedência de operadores do Python

- 7(alto): exponenciação `**`.
- 6: multiplicação `*`.
- 5: adição `+,-`.
- 4: relacional `==,!=,<=,>=,>,<`.
- 3: lógico `not`.
- 2: lógico `and`.
- 1(baixo): lógico `or`.

### Blocos de código e identação

- Python não usa chaves para delimitar os blocos de código, ele usa 4 espaços em branco de identação(recuo) obrigatório.
- Os dois pontos (:) indica que a partir começa um bloco de código.
- Existem blocos condicionais e blocos de repetição.
- Para cada bloco de código aninhado, soma-se 4 espaços em branco, aumentando o recuo.
- É recomendável não passar de 3 a 4 níveis de identação.

### Ambientes virtuais e a ferramenta iPython

- O ambiente é aonde o programa/script vai ser executado.
- Para garantir que o programa/script rode corretamente e igualmente em todos os computadores se faz necessário a criação de um ambiente virtual.

É uma boa prática é criar um ambiente virtual do Python para todo projeto, evitando que danifique o sistema operacional, por conta de conflitos, separando todo o ambiente do projeto do ambiente real do computador.

- `python3 -m venv nome_do_ambiente` -> comando para criar um ambiente virtual utilizando a versão 3 do Python, uma conversão para nome de um ambiente é `.venv`, pois arquivos/pastas que utilizam "." antes do nome normalmente são ocultos e não aparecem no sistema de arquivo do SO.
- `source .venv/bin/activate` -> comando para ativar o ambiente virtual no Linux.

Não há necessidade de mandar a pasta do ambiente virtual para o repositório git.

- `python3 -m pip` -> módulo do Python destinado a instalação de pacotes.
- `python3 -m pip install ipython` -> instala a biblioteca iPython, um interpretador interativo melhorado de Python.
- `python3 -m pip install --upgrade pip` -> atualiza o pip para a última versão, recomendado sempre executar ao criar um novo ambiente virtual.

Ao usar `%time` no iPython antes de qualquer código, é mostrado o tempo de execução utilizado, além dos recursos computacionais.

## Dia 2 - Tipos de Dados e Protocolos

### A importância dos tipos de dados e o tipo inteiro

- Ao realizar uma operação de atribuição, o interpretador do Python realiza uma operação de inferência de tipo, para saber a maneira e o local correto de armazenar a informação na memória.

Tipo de dado também pode ser chamado de classe de dado ou categoria de dado.

O interpretador do Python converte um número inteiro para uma sequência de bits para armazená-los na memória.

- `bin(numero_inteiro)` -> retorna o valor em binário de qualquer número inteiro. Tudo que começa com `0b` no Python indica um número binário.

Na memória do computador, o identificador(nome da variável) está apontando para uma sequência de bits. Ao solicitar um dado da memória, o Python o converte para o contexto da aplicação, isso é realizado através do tipo de dado.

No caso de letras ou strings, cada letra é convertida para um número inteiro, depois converte novamente para binário e então é armazenado o valor binário na memória.

**Exemplo**

Como é realizado o armazenamento da operação de atribuição `numero = 65`.

- Em seguida, o interpretador vai identificar, através da inferência de tipos, qual o tipo daquele dado, neste caso, um inteiro(int).
- Depois, o interpretador cria um "envelope" e atribui a um espaço na memória RAM, numa posição qualquer.
- E dentro desse "envelope" o Python armazena o número inteiro "65" convertido para binário, que é "1000001".
- Finaliza colocando nesse "envelope" uma etiqueta contendo o nome da variável em questão, no caso "numero".

Ao solicitar essa variável `numero`, o interpretador Python vai buscar na memória o local que possui o identificador "numero" e ao ver que aquele valor é do tipo inteiro, o interpretador vai converter o número binário para um número inteiro e por fim, exibir na tela(output).

<hr>

- `id(variavel)` -> retorna o número, que é a posição em que se encontra aquela variável na memória RAM. Esses valores são aleatórios e não sequenciais.
- `type(variavel)` -> retorna qual o tipo do valor armazenado em uma variável qualquer.

Um objeto é um conjunto composto por um endereço de memória, um tipo, um valor e um identificador(nome da variável). Todo objeto possui as mesmas características.

Dado é o valor armazenado na memória, e é através do tipo de dado que esse dado é transformado em uma informação para ser compreendida.

Os tipos de dados são divididos em duas categorias: primários e compostos

#### Tipos de dados primários(Scalar Types)

- São tipos de dados que servem para representar apenas um único valor.

Um desses tipos de dado é o Tipo Inteiro(Integer), que é uma classe definida no código fonte do Python que juntamente do valor traz todo o comportamento específico dessa classe.

Não é necessário explicitamente dizer ao Python qual o tipo de objeto a guardar na memória, pois o interpretador faz isso dinamicamente.

- `int(valor)` -> força o tipo de um determinado valor para inteiro.
- `dir(tipo_de_dado)` -> retorna uma lista contendo todos os métodos e protocolos de um determinado tipo de dado, eles determinam quais operações que aquele objeto pode realizar.

**Métodos públicos**

- Qualquer método que não possui dunder, são chamados de métodos públicos.

**Protocolos**

- Já os protocolos(métodos que possuem dunder), determinam as operações e ações que o tipo de dado pode realizar, normalmente, não são utilizados. Tudo no Python vai funcionar através desses protocolos, que são vários.
- Existem protocolos que exigem apenas um método dunder, enquanto há protocolos que exigem mais de um método dunder para funcionar.

**Exemplos**

***Método Dunder Add***

Quando um objeto implementa o método `__add__()`, ele implementa o protocolo addible, significa que o objeto é capaz de receber adição de outros números.

- `numero + 1` = `numero.__add__(1)`

***Método Dunder Eq***

Implementa o método `__eq__()`, que implementa o protocolo equal, significa que o objeto pode realizar operações de comparações.

- `numero == 65` = `numero.__eq__(65)`

### Tipos Float, Bool, NoneType

Os tipos Float, Bool, NoneType são tipos primitivos.

**Tipo Float**

- É um número que além do número inteiro, possui uma parte fracionada, Float de ponto flutuante. Representa frações.
- É a presença de um ponto no número que faz com o Python trate como Float.
- Podem ser negativos ou positivos.

```python
valor = 2.0
type(valor) # float
valor.is_integer() # true

valor = 2
type(valor) # int
```

- Para representar valores monetários, o ideal é utilizar o tipo Decimal (ou Currency). Pois a precisão do tipo Decimal é maior do que a do tipo Float.

**Tipo Boolean**

- Pode ter apenas o valor True (Verdade) ou o valor False (Falso).
- Representado pelo nome `bool`.
- O número 0 é igual a False e o número 1 é igual a True.
- Expressões lógicas sempre retornam um booleano.
- O `if` só funciona com valores booleanos.
- Texto vazio é considerado como o valor 0 (False).
- Para o interpretador do Python todo valor numérico, diferente de 0, é True.

**Tipo NoneType**

- Apenas possui uma opção de valor, `None`, que significa nulo ou ausência de valor.
- No Python, todo objeto (variável) deve ser inicializado, sempre contendo um valor.
- Pode ser usado para inicializar uma variável que ainda não se sabe o valor, posteriormente, essa variável pode ter seu valor mudado.

**Singleton** -> objetos que podem ser criados uma única vez durante toda a execução do código.

Toda variável None terá a mesma posição na memória, independente da quantidade de variáveis com o valor `None` atribuído.

- Em alguns casos, funções irão retornar um valor `None`. Isso ocorre pois toda função, por ser uma expressão, deve retornar um valor.

### Textos, Caracteres, Encoding e Strings

- Tipos de dados que fica entre os tipos primário e os tipos compostos.

**String**

- Representa uma cadeia de caracteres.
- Objeto representado pela classe `str`.
- Criado usando aspas duplas ou aspas simples.

Textos com mais de um caractere são chamados de Bytearrays ou String. Cada caractere no texto é convertido para um byte e armazenado na memória, formando uma cadeia de bytes.

**Tabela ASCII**

- O interpretador do Python usa uma tabela padrão ASCII para converter um número inteiro em um caractere específico.
- Limitada, pois só possui os caracteres americanos.
- Por limitação de memória possui apenas 127 valores (caracteres).
- Os primeiros 33 caracteres são chamados de caracteres de controle.

**Tabela Unicode**

- Uma tabela única extendida que possuem muitos caracteres, além de emojis. Melhoria da Tabela ASCII.
- O interpretador do Python já converte automaticamente qualquer valor hexadecimal da Tabela Unicode ao usar a função `print()`.
- É um consórcio mundial de várias empresas.

**UTF-8**

- Tabela Unicode que em cada posição consegue armazenar 8 bits.
- Existem alguns caracteres da Tabela Unicode que ocupam mais de 8 bits.

**Serialização**

Conversão de um objeto Unicode em uma representação em texto em hexadecimal. Ideal utilizar para trafegar pela rede ou armazenar caracteres Unicode em servidores ou banco de dados que não suportam Unicode.

- `variavel.encode("utf-8")` -> converte para uma string que tem uma sequência hexadecimal que representa um caractere especial da Unicode.
- `variavel.decode("utf-8")` -> converte da sequência hexadecimal para o caractere especial da Unicode.
- `bytes(variavel, "utf-8")` -> retorna a representação em bytes do valor de uma variável, o segundo parâmetro informa qual a tabela que o interpretador vai utilizar para buscar esses valores.
- `string[numero]` -> fatiamento, fatia a string em várias formas. Também é possivel selecionar um intervalo de caracteres da string, usando `[inicio:fim]`.
- `len(variavel)` -> retorna o número de itens dentro de um objeto que pode armazenar outros objetos, pode ser usado em uma string para retornar a quantidade de caracteres.

É possível concatenar apenas textos usando o caractere `+`, exemplo: `"Giovanni" + "Padilha"`.

Também é possível multiplicar textos, `"Giovanni" * 2` = `"GiovanniGiovanni"`.

Strings são percorríveis, podendo percorrer cada caractere como se a string fosse uma lista contendo caracteres.

- `next(variavel_iteravel)` -> retorna o próximo objeto de um objeto iterável.
- `string.upper()` -> retorna toda a string em maiúsculo.
- `string.lower()` -> retorna toda a string em minúsculo.
- `string.capitalize()` -> coloca a primeira letra da primeira palavra da string em maiúsculo.
- `string.title()` -> coloca a primeira letra de todas as palavras da string em maiúsculo.
- `string.split(caractere)` -> separa a string em uma lista, cortando com base em um caractere especificado.
- `string.startswith(caractere)` -> verifica se a string começa com o caractere especificado, retornando True ou False.

Esses métodos podem ser usados em cadeia. Por exemplo: `string.upper().split()`.

Strings podem ser comparadas, de acordo com o valor daquele caractere na tabela Unicode ou ASCII.

- `sorted(string)` -> retorna uma lista de caracteres em ordem alfabética.
- `reversed(string)` -> retorna um objeto do tipo reversed (pode ser convertido para uma lista) com os caracteres começando do fim.

Os dois métodos acima apenas funcionam pois o objeto `str` implementa o protocolo dunder `__eq__`.

As strings estão entre os objetos primários e compostos pois, uma string armazena semânticamente um único valor, porém internamente, o Python grava uma sequência de caracteres a partir dessa string.

### Formatação de Textos

#### Concatenação

- É possível concatenar várias strings, ex: `'Giovanni' + 'Padilha' = 'Giovanni Padilha'`.
- O operador `+` apenas concatena string com string, para concatenar outros tipos de dados com strigs se utiliza o operador `,`, ou então converter a variável para string usando `str()`. Isso ocorre pois o Python é de tipagem forte.

#### Interpolação

- Define a mensagem (string) antes, criando um template.
- Nesse template, terá os placeholders que é o local que vai ser substituído na string por um valor de uma variável. Esses placeholders são definidos usando o operador de `%` seguido de uma letra, ex: `%s`.
  - `%s` indica um placeholder para strings.
  - `%d` indica um placeholder para integers. Para indicar a quantidade de dígitos `%03d`.
  - `%f` indica um placeholder para floats. Para indicar quantas casas decimais mostrar `%.2f`.

Para substituir esses placeholders por valores de variáveis utiliza: `template % (variavel_1, variavel_2, ...)`.

Útil para usar na biblioteca `logging`.

**Parâmetros Nomeados**

- Atribui um nome para o placeholder, usado em textos muito grande.
- Sintaxe: `%(nome)s`

Para atribuir valores a esses placeholders se usa um dicionário `template % {'nome':'Giovanni', chave: valor, ...}`.

#### String Format

- Método `str.format()`.
- New style, forma mais recente de formatar textos no Python3.
- Em vez de utilizar `%`, utiliza `{}`.
- Para formatar segue o mesmo padrão da Interpolação, a diferença é que vem `:` antes da especificação.

Útil para mensagens longas, como e-mails.

*Exemplo*

```python
msg = "Olá, {} você é o player n {:03d} e você tem {:.2f} pontos"

msg.format("Giovanni", 2, 987.3)
```

**Extras**

- Centraliza textos `{:^10}.format("Giovanni")`, o número 10 é o tamanho do espaço, centraliza em 10 caracteres.
- Alinha a esquerda `{:<10}.format("Giovanni")`.
- Alinha a direita `{:>10}.format("Giovanni")`.
- Preenche os espaços em branco com um caractere especificado `{:#^10}.format("Giovanni")`, preenche com `#`.
- Corta uma string `{:^10.3}.format("Giovanni")`, usando em valores floats imprime uma representação abreviada.

**Chaves Nomeadas**

- Atribui nome as chaves, ex: `{pontos:.2f}`.

Substituindo os placeholders nomeados `str.format(nome_variavel=valor, ...)`

#### f-strings

- A partir do Python3, nova sintaxe de aplicar `str.format`.
- Sintaxe simplificada: `f"Olá, {nome}"`
- Obrigatório aplicar um nome para os placeholders. E cade placeholder se refere a uma variável existente, se não existir a variável, retorna erro.

Uso geral, qualquer tipo de mensagem.

#### Emojis

Há duas formas de imprimir emojis no Python.

- A primeira forma é através do código unicode do emoji. Utiliza `\U000` antes do código do emoji.
- A segunda forma é substituir o `\U` pelo nome do emoji usando `\N{nome_emoji}`.

### Tipos de Dados Compostos e Tuplas

- Capaz de armazenar (como um contâiner) mais de um único valor, até mesmo diferentes tipos de dados.

#### Sequência

- Um único objeto na memória, que possui um nome.
- Dentro desse objeto sequência, terá posições que vão referenciar aos objetos contidos dentro desse contâiner. Cada objeto dentro de um contâiner vai ser armazenado na memória separadamente, da mesma forma que uma variável individual, tendo sua posição, tipo de dado e valor.

#### Tuplas (Tuple)

- Cria uma sequência de objetos heterogêneos.
- Cada objeto é separado por vírgulo, e os objetos como um todo são armazenados dentro de uma Tupla.

<hr>

- `tuple.count(valor)` -> retorna a quantidade de vezes que um determinado valor é encontrado dentro de uma Tupla.

A Tupla pode ser subscrita, ex: acessando o último valor da tupla `tuple[-1]`. As Tuplas são acessados pelo índice, começando por 0, ao usar índices negativos o acesso é feito do inverso. É o fatiamento, ex: `tuple[indice_inicial:indice_final]`

- Também pode ser iterada.
- É opcional o uso de parênteses ao realizar a atribuição, apenas as vírgulas são obrigatórios, é a partir delas que vai ser inferido o tipo de dado Tuple.
- A Tupla é imutável, a partir de sua criação, ela não pode ser alterada.

**Desempacotamento de Tupla**

- Desempacota uma Tupla em várias variáveis separadas, ao mesmo tempo.

*Ex:*

```python
pontos = 2, 1, 99

x, y, z = pontos

# x = 2
# y = 1
# z = 99
```

- Para ignorar valores, basta usar o operador `*_` no local da variável em questão.
- Também podem ser desempacotados o primeiro valor e o último elemento, ex: `primeiro, *_, ultimo = valores`.
- `len(objeto)` -> retorna o tamanho apenas de sequências materializadas.

### Listas

- Objeto "padrão" no Python para sequências.
- Podem ser comparadas com arrays ou vetores, com diferenças!
- Uma lista é declarada usando `[]` (preferível) ou `list()`.
- Pode ser criada vazia, pois é um objeto mutável, pode ser alterada após ser criada.
- Todas as operações com Tuplas também é possível fazer com uma Lista.
- É permitido somar Listas uma com a outra. E o resultado dessa soma é uma outra Lista com a junção dos objetos das duas Listas.

<hr>

- `list.append(valor)` -> adiciona um objeto ao final de uma lista.
- `list.insert(posicao, valor)` -> adiciona um objeto em uma posição (índice) específico.
- `list.remove(valor)` -> remove o primeiro valor encontrado na lista, mesmo que haja dois valores iguais.
- `list.extend(list)` -> extende uma Lista com outra Lista, sem criar um objeto novo. Funciona igual com o operador `+=`.
- `list.count(valor)` -> retorna quantas vezes aparece um valor dentro de uma lista.
- `list.pop()` -> remove o último valor da lista.

Possível usar `in` em Listas, retornando True se achar ou False se não encontrar, ex: `valor in list`. Em alguns objetos ele é lento!

### Exercícios com Listas, Tuplas, Loops e Condicionais

**Exercício Escola com Listas**

```python
#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade

Imprimir a lista de crianças agrupadas por sala
que frequentam cada uma das atividades.
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

# Listas com alunos
sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"]
sala2 = ["João", "Antonio", "Carlos", "Maria", "Isolda"]

# Listas com alunos inscritos nas atividades.
aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio"]
aula_musica = ["Erik", "Carlos", "Maria"]
aula_danca = ["Gustavo", "Sofia", "Joana", "Antonio"]

# Cria uma Lista atribuindo cada Lista de aula e label em uma Tupla.
atividades = [
    ("Inglês", aula_ingles), 
    ("Música", aula_musica), 
    ("Dança", aula_danca),
]

# Itera sobre cada atividade da Lista de atividades.
# Desempacota a Tupla, atribuindo o label da atividade para a variável `nome_atividade` e os alunos para `alunos_atividade`.
for nome_atividade, alunos_atividade in atividades:
    print(f"Alunos da atividade de {nome_atividade}\n")

    # Variáveis para adicionar os alunos de cada sala de determinada atividade.
    # Essas variáveis são resetadas a cada loop.
    atividade_sala1 = []
    atividade_sala2 = []

    # Iterando cada aluno de cada atividade.
    for aluno in alunos_atividade:
        
        # Comparando se o aluno da atividade está na sala 1 ou sala 2.
        if aluno in sala1:
            atividade_sala1.append(aluno)
        elif aluno in sala2:
            atividade_sala2.append(aluno)
    
    # Imprimindo os alunos de cada sala.
    print("Sala 1:", atividade_sala1)
    print("Sala 2:", atividade_sala2)
    print("-" * 20)
```

### Sets e a Teoria dos Conjuntos

- Sets (Conjuntos), um conjunto não ordenado de valores únicos.
- Para criar um conjunto se usa `{}`, porém é confundida com o Dicionário que também usam chaves para delimitar. A melhor maneira de criar então é usar `set()`.
- Dentro da função `set()` você passa qualquer objeto iterável, seja uma Tupla ou Lista.
- Ao criar um Set a partir de uma String, ele cria uma sequência de caracteres únicos não ordenados. Remove itens duplicados de uma coleção.
- Não são indicados para armazenar valores, são objetos de transição, geralmente usados para operações.

Não usar Sets quando se precisa ter valores repetidos e também de manter a ordem de uma sequência ao alterá-la.

- Não possui o protocolo Subscriptable, não podendo usar índices para acessar os elementos.

#### Implementa o Diagrama de Venn e a Teoria dos Conjuntos

![Operações com Conjuntos](./images/operacoes_conjuntos_day2.webp)

**Conjuntos de exemplo**

```python
conjunto_a = set([1, 2, 3, 4, 5])
conjunto_b = set([4, 5, 6, 7, 8])
```

- Podem ser convertidos diretamente ao realizar a operação usando `set()` ou criá-los já como Sets.
- Internamente, as funções `union(), intersection(), difference() e symmetric_difference()` também convertem o objeto iterável passado para um Set.

**União**

- Retorna todos os valores unidos de ambos os conjuntos. Não repete os valores.

```python
conjunto_a | conjunto_b

# ou

conjunto_a.union(conjunto_b)

# {1, 2, 3, 4, 5, 6, 7, 8}
```

**Intersecção**

- Retorna todos os valores que aparecem nos dois Sets.

```python
conjunto_a & conjunto_b

# ou

conjunto_a.intersection(conjunto_b)

# {4, 5}
```

**Diferença**

- Retorna os elementos que aparecem no conjunto A e não aparecem no conjunto B, ou vice-versa.

```python
conjunto_a - conjunto_b

# ou

conjunto_a.difference(conjunto_b)

# {1, 2, 3}

conjunto_b.difference(conjunto_a)

# {6, 7, 8}
```

**Diferença Simétrica**

- Retorna todos os elementos que estão apenas no conjunto A e apenas no conjunto B.

```python
conjunto_a ^ conjunto_b

# ou

conjunto_a.symmetric_difference(conjunto_b)

# {1, 2, 3, 6, 7, 8}
```

- `set.add(valor)` -> adiciona um novo elemento ao Set. Sempre garantindo elementos únicos.

#### Implementa Hash Table

- Resolve a complexidade algorítmica ao realizar busca dentro de uma coleção.
- Quando uma busca precisa iterar sobre todos os valores de uma coleção, a complexidade dessa busca é O(n) Big O. Este é o caso do protocolo Contains `in` das Listas e Tuplas.

No caso de buscas usando Sets, a operação de busca é de complexidade O(1) ou constante, pois ele possui uma Hash Table, onde cada elemento possui um hash único que aponta para a posição de cada objeto na memória.

### Dicionários

- É um super tipo de dado, características parecidas com a "união" do Set com a Lista.
- Implementa Hash Table e permite ser iterado.
- O Dicionário guarda duas informações para cada posição. Cada posição tem uma chave, que aponta para um valor.
- Não precisa de um índice para buscar por um valor, através da chave é possível saber aonde se encontra tal dado, independente da posição.
- As buscas para valores de chaves no Dicionário é de complexidade O(1). Agora as buscas por valores vão ter menos performance, será necessário criar um algoritmo de busca de árvore invertida.

Sintaxe para criar `{chave:valor}` ou `dict()`

- A chave e o valor podem ser todo tipo de objeto compatível com Hash Table.
- Não permitem chaves duplicadas.
- São mutáveis.

<hr>

- `dict[key] = value` -> adiciona um novo conjunto de chave/valor no dicionário. Também é usado para alterar um campo.
- `del dict[key]` -> remove um campo do dicionário através da chave.
- `dict[key]` -> acessa o valor a partir de uma chave.
- `dict.keys()` -> retorna uma lista contendo apenas as chaves.
- `dict.values()` -> retorna uma lista contendo apenas os valores.
- `dict.items()` -> retorna todos os campos chave e valor como Tuplas.
- `dict.update(another_dict)` -> junta um dicionário em outro. Também é possível juntar dois dicionários em um novo usando desempacotamento `{**dict_1, **dict_2}`.

Um único `*` desempacota sequências que contém um único elemento em cada posiçao, enquanto dois `**` desempacota dois elementos para cada posição, usado em Dicionários.

- `dict.get(key)` -> busca uma chave no dicionário, se não existir não retorna nada, se existir retorna o seu valor. Não gera erro se não encontrar a chave.

### Refatorando o Hello World usando Dicionários

**Código**

```python
#!/usr/bin/env python3
"""Hello World Multi Línguas.

Dependendo da língua configurada no ambiente o programa exibe a mensagem
correspondente.

Como usar:

Tenha a variável de ambiente LANG devidamente configurada ex:

    export LANG=pt_BR

Execução:

    python3 hello.py
    ou
    ./hello.py
"""
# Metadados com informações adicionais.
__version__ = "0.1.2"
__author__ = "Giovanni Padilha"
__license__ = "Unlicense"

# Importando a biblioteca `os` que permite que o Python se comunique com o SO.
import os

# Define um bloco principal de um script Python,
# apesar de estar caindo em desuso.
#if __name__ == "__main__":

# A função `getenv()` da lib `os` coleta o valor de uma variável de ambiente.
# - O primeiro parâmetro informa qual o nome da variável de ambiente.
# - O segundo parâmetro informa um valor padrão, caso essa variável não existir.

# O `[:5]` refere-se ao fatiamento da string, coletando apenas os 5 primeiros caracteres.
current_language = os.getenv("LANG", "en_US")[:5]

# Dicionário contendo uma chave com o País e a língua dele e o valor é a mensagem na língua do País.
msg = {
    "en_US": "Hello, World!",
    "pt_BR": "Olá, Mundo!",
    "it_IT": "Ciao, Mondo!",
    "es_SP": "Hola, Mundo!",
    "fr_FR": "Bonjour, Monde!",
}

#Estrutura condicional `if`, onde a expressão lógica será dada como true ou false,
#e a partir desse valor booleano, é executado um bloco de código.

#A palavra `elif` faz com que uma nova comparação possa ser adicionada na estrutura.

#Ordem de Complexidade O(n)
"""
if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Bonjour Monde!"
"""

# A função `print()` imprime um conteúdo qualquer na tela (output).
# Ordem de Complexidade O(1) - Constante.
print(msg[current_language])
```

## Dia 3 - Input-Output, Algoritmos, Condicionais, Repetições

### Standard Input & Output e argumentos do CLI

Botão Ligar -> Sinal elétrico para Bios (liga o computador e inicializa os componentes iniciais), possui um SO imbutido -> CPU, inicia o processo de boot -> SSD, identifica o SO -> RAM, carrega o SO -> **stdout** (Standard Input), imprime informações na tela.

#### stdout

**stdout** -> saída padrão do computador, é um módulo virtual do sistema. Pode ter um ou vários monitores conectados a esse módulo, ou até mesmo vários terminais. Cada programa possui um Shell e possui sua saída padrão (stdout).

- O ambiente de execução do Python é acessado atráves de uma biblioteca chamada `sys` do Python, podendo acessar o stdout.
- stdout é um objeto TextIOWrapper. Espera receber texto, um descritor de arquivos. Possuindo um modo de escrita e um encoding.
- stdout varia de acordo com o programa. O stdout do iPython é o terminal.
- A função print implementa o `sys.stdout`, é uma abstração da interface stdout.
- Está no modo de escrita "write".

<hr>

- `sys.stdout.write(text)` -> imprime uma mensagem no stdout junto de um número inteiro, que é o tamanho desse texto.
- `print("text", file=open("path", "mode"))` -> substitui o stdout por um outro descritador de arquivo, em vez de imprimir no terminal, a mensagem do print vai ser gravado no arquivo.
- `open("path", "mode")` -> cria um novo arquivo em um modo especificado.

#### stdin

- Coleta informações a partir de uma interface stdin.
- Também é um descritor de arquivos e é acessado pela biblioteca `sys`.
- Está no modo de leitura "read".
- A função `input()` é a abstração do stdin, está preparado para receber a tecla Enter.

<hr>

- `sys.stdin.read(char_length)` -> espera ler um caractere, informando a quantidade esperada de caractere.
- `input("question")` -> abstração do stdin. Utilizado para programas que tenham interação humana. Também pode ser usado para dar uma pequena pausa do programa. Toda informação recebida por essa função está no formato de string e considera espaços em branco.
- `strip("char")` -> remove todos os espaços em branco do começo e do final de uma string. Também pode ser especificado um caractere específico a ser removido da string, do início e do fim.

**Formas de se comunicar e receber dados do ambiente**

- Variáveis de ambiente (não recomendável).
- CLI Args (recomendável).

Se o usuário não passar os CLI Args, então se usa a variável de ambiente, e se não tiver uma variável de ambiente definida, se utiliza um valor padrão.

- `sys.argv` -> retorna uma lista contendo os argumentos passados pelo CLI ao executar o script.
- `str.replace(actual_char, new_char)` -> substitui os caracteres de uma string por um novo caractere especificado.
- `str.lstrip("char")` -> retira todos os caracteres apenas no início da string a partir de um caractere especificado.
- `str.removeprefix("str")` -> a partir do Python 3.9, também remove caracteres do início da string.

### Exercício: Prefix calculator com CLI args e inputs

**Meu algoritmo**

```python
#!/bin/usr/env python3
"""Calculadora prefix

Funcionamento:

[operação] [n1] [n2]

Operações:

sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ python3 prefixcalc.py sum 5 2
7

$ python3 prefixcalc.py mul 10 5
50

$ python3 prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("operação: ")
    n1 = float(input("n1: "))
    n2 = float(input("n2: "))
else:
    operation, n1, n2 = arguments
    result = 0
    n1 = float(n1)
    n2 = float(n2)

if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":
    if n2 == 0:
        print("Division by zero")
        sys.exit()
    result = n1 / n2

print(result)
```

**Algoritmo Final**

```python
#!/bin/usr/env python3
"""Calculadora prefix

Funcionamento:

[operação] [n1] [n2]

Operações:

sum -> +
sub -> -
mul -> *
div -> /

Uso:

$ python3 prefixcalc.py sum 5 2
7

$ python3 prefixcalc.py mul 10 5
50

$ python3 prefixcalc.py
operação: sum
n1: 5
n2: 4
9
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

import sys

# Colentando os argumentos necessários
arguments = sys.argv[1:]

# TODO: Exceptions
# Verificando se a lista de argumentos está vazio ou não.
# Se estiver vazia, perguntar a operação e os números ao usuário e reatribui na variável `arguments`.

# Uma lista vazia ao ser passada em um statement, retorna False. Com o uso do not, inverte, ficando como True.
if not arguments:
    operation = input("operação: ")
    n1 = input("n1: ")
    n2 = input("n2: ")

    arguments = [operation, n1, n2]

# Verifica se a lista de argumentos tem menos de 3 argumentos.
# Se tiver, imprime um erro, junto com um exemplo de uso e encerra o programa.
elif len(arguments) != 3:
    print("Número de argumentos inválidos")
    print("ex: `sum 5 5`")
    sys.exit(1)

# Desempacota a variável `arguments` em uma variável com a operação e uma com os números.
operation, *nums = arguments

# Tupla com as operações válidas.
valid_operations = ("sum", "sub", "mul", "div")

# Verifica se a operação digitada pelo usuário não está dentro das operações válidas.
# Se não estiver, imprime um erro, junto com a lista de operações válidas e encerra o programa.
if operation not in valid_operations:
    print("Operação inválida")
    print(valid_operations)
    sys.exit(1)

# Lista para armazenar os números validados.
validated_nums = []

# Validando cada um dos números inseridos pelo usuário.
for num in nums:
    # TODO: Repetição com while + exceptions

    # Remove, se houver, o "." no conteúdo da variável.
    # Após, verifica se o conteúdo possui apenas dígitos.

    # Se não tiver apenas dígitos, imprime um erro, junto com o conteúdo da variável em questão e encerra o programa.
    if not num.replace(".", "").isdigit():
        print(f"Número inválido {num}")
        sys.exit(1)

    # Verifica se no conteúdo da variável possui o "."

    # Se possuir, converter para float.
    # Se não possuir, converter para int.
    if "." in num:
        num = float(num)
    else:
        num = int(num)

    # Insere o número já validado dentro da Lista de números validados.
    validated_nums.append(num)

# Desempacota os números validados nas variáveis `n1` e `n2`.
n1, n2 = validated_nums

# Variável para armazenar o resultado.
result = 0

# TODO: Usar dict de funções

# Verifica qual o tipo da operação, realizando-a e armazenando o resultado na variável `result`.
if operation == "sum":
    result = n1 + n2
elif operation == "sub":
    result = n1 - n2
elif operation == "mul":
    result = n1 * n2
elif operation == "div":

    # Verifica se o dividor é igual a 0, não é possível dividir por 0.

    # Se for igual, imprime uma mensagem de erro e encerra o programa.
    if n2 == 0:
        print("Division by zero")
        sys.exit(1)
    result = n1 / n2

# Imprime o resultado na tela.
print(f"O resultado é {result}")
```

### Manipulando arquivos e pastas

- Biblioteca `os` permite manipular o sistemas de arquivos do SO.

**Alguns métodos da biblioteca os**

- `os.listdir("path")` -> retorna uma lista com o conteúdo da pasta especificada no caminho dentro do método.
- `os.chdir("path")` -> navega para o caminho especificado.
- `os.mkdir("nome_pasta")` -> cria um diretório/pasta.
- `os.makedirs("nome_pasta", exist_ok=True)` -> cria um subdiretório dentro de outro sem exibir um erro.
- `os.path.join("pasta1", "pasta2", ...)` -> une e retorna o caminho de um diretório, considerando o SO em questão, usando a "\" ou "/". Sempre crie pastas e arquivos usando o caminho que esse método retorna.
- `os.curdir` -> retorna o diretório atual, o caminho relativo. Mais recomendável, pois considera outros SOs também, multiplataforma.
- `os.mknod(os.path.join(path, "nome_arquivo"))` -> cria um arquivo vazio dentro de um caminho.
- `os.path.basename(filepath)` -> retorna apenas o nome do arquivo do caminho dele.
- `os.path.exists(filepath)` -> retorna se o caminho de um arquivo existe ou não.
- `os.abspath(path)` -> retorna o caminho absoluto de uma pasta ou arquivo.

Para escrever num arquivo vazio é necessário um descritor de arquivos, um objeto capaz de ler e escrever um arquivo.

- `open(filepath, mode)` -> cria um file descriptor que permite a interação com um arquivo, por padrão, inicia no modo de leitura. O segundo parâmetro é o modo do arquivo, "r" para leitura, "w" para escrita. Arquivos no modo "w" substitui todo o conteúdo do arquivo, para não apagar todo o conteúdo do arquivo usar o modo "a" append. Cria o arquivo se não existir.
- `arquivo.read()` -> lê o conteúdo do arquivo. Consome o conteúdo do arquivo, linha por linha.
- `arquivo.readlines()` -> retorna uma lista, onde cada posição é uma linha de conteúdo do arquivo.
- `arquivo.write("text")` -> escreve algo dentro de um código. `\n` quebra linha.
- `arquivo.close()` -> fecha o arquivo, necessário sempre ao terminar de realizar as operações desejadas.
- `arquivo.seek()` -> volta no histórico de linhas consumidas do arquivo. Ou então reabra novamente o arquivo.

**Context Manager with**

- Cria um Context Manager usando `with`, um objeto especial para interagir com o arquivo em questão.
- Dentro do escopo do Context Manager o código é gerenciado pelo Gerenciador de Contextos, abrindo devidamente o arquivo, realizar as operações e depois fechar o arquivo automaticamente.
- Sempre utilizar um Gerenciador de Contexto para escrever em arquivos. Em alguns casos mais simples o `print("text", file=file_descriptor)` pode ser usado.

```python
with open(filepath, "a") as arquivo:
    # Code block
```

- `arquivo.writelines()` -> escreve várias linhas de uma única vez no arquivo.

**Biblioteca Pathlib**

- Abordagem mais orientada a objetos.
- Funciona em qualquer Sistema Operacional.
- Não tem necessidade de importar a biblioteca `os`.
- `from pathlib import Path`

<hr>

- `Path("pasta")` -> retorna um objeto que referencia a pasta em questão.
- `Path("pasta") / Path("pasta2")` -> une duas pastas.
- `path / Path("nome_arquivo")` -> cria um arquivo dentro de um caminho usando o objeto Path.
- `path / "nova_pasta"` -> cria um novo objeto que representa essa nova pasta. Para criar `(path / "nova_pasta").mkdir()`.
- `filepath.write_text("text")` -> escreve num arquivo usando o objeto Path.
- `filepath.read_text()` -> lê o conteúdo de um arquivo usando o objeto Path.

### Exercício - criando um bloco de anotações

**Meu algoritmo**

```python
#!/usr/bin/env python3
"""Bloco de notas

$ python3 notes.py new "Minha nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia.

$ python3 notes.py read --tag=tech
...
...
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "archives", "notes.txt")

arguments = sys.argv[1:]
if not arguments:
    print("Invalid usage")
    sys.exit(1)

valid_commands = ("new", "read")

if arguments[0] not in valid_commands:
    print(f"Invalid command {arguments[0]}")

if arguments[0] == "new":
    title = arguments[1]
    tag = input("tag: ")
    text = input("text: \n")

    with open(filepath, "a") as file_:
        file_.write(f"{title}, {tag}, {text} \n")

if arguments[0] == "read":
    tag_read = arguments[1][6:].strip()

    for line in open(filepath):
        title, tag, text = line.split(",")
        if tag_read == tag.strip():
            print(f"Title: {title}")
            print(f"Tag: {tag}")
            print(f"Text: {text}", end="")
            print("-" * 50)
```

**Algoritmo final**

```python
#!/usr/bin/env python3
"""Bloco de notas

$ python3 notes.py new "Minha nota"
tag: tech
text: 
Anotação geral sobre carreira de tecnologia.

$ python3 notes.py read tech
...
...
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"

# Importando bibliotecas `os` e `sys`
import os
import sys

# Coletando o caminho relativo do diretório atual
path = os.curdir

# Definindo o caminho relativo do arquivo para armazenar as notas
filepath = os.path.join(path, "archives", "notes.txt")

# Coletando os argumentos CLI, menos o nome do arquivo.py
arguments = sys.argv[1:]

# Lista com os comandos aceitos
valid_commands = ("new", "read")

# Verificando se a lista de argumentos está vazia
# Se não estiver com conteúdo, imprime uma mensagem de erro, juntamente com os comandos válidos e encerra o programa
if not arguments:
    print("Invalid usage")
    print(f"you must specify subcommand {valid_commands}")
    sys.exit(1)

# Verifica se o comando inserido pelo usuário está dentro dos comandos válidos

# Se não estiver dentro, imprime um erro juntamente com o comando errado e encerra o programa
if arguments[0] not in valid_commands:
    print(f"Invalid command {arguments[0]}")
    sys.exit(1)

# Verifica se o comando inserido é o `new`, comando para criar uma nova nota
if arguments[0] == "new":

    # Coleta o título da nota dos argumentos CLI
    title = arguments[1] # TODO: Tratar exception

    # Cria uma lista que armazena o título, tag e o conteúdo da nota em cada posição
    note = [
        f"{title}",

        # Inserção de dado, excluindo os espaços em branco do início e do fim
        input("tag: ").strip(),
        input("text:\n").strip()
    ]

    # Abre o arquivo com o Gerenciador de Contexto `with` para armazenar a nota
    with open(filepath, "a") as file_:

        # A função `join(list)` concatena uma lista de strings em uma única string, inserindo um tab (`\t`) entre cada item 
        # e no final um espaço em branco (`\n`)
        # Por fim, a string concatena é escrita em uma única linha no arquivo
        file_.write(f"\t".join(note) + "\n")

# Verifica se o comando inserido é o `read`, comando para ler notas a partir da tag
if arguments[0] == "read":

    # Itera sobre cada linha do arquivo
    for line in open(filepath):

        # Desempacota a linha dividida por tab (`\t`) do arquivo em três variáveis, 
        # o primeiro valor é título, segundo valor a tag e o terceiro valor o conteúdo da nota
        title, tag, text = line.split("\t")

        # Compara a tag de cada linha com a tag inserida pelo usuário
        # Na tag inserida pelo usuário, a função `strip()` retira os espaços em branco do início e do fim da string e
        # a função `lower()` transforma todas os caracteres da string em minúsculo

        # Na tag da nota apenas é usada a função `lower()` que transforma todos os caracteres da string em minúsculo
        if tag.lower() == arguments[1].strip().lower():

            # Imprime o título, tag e o conteúdo da nota separados por linhas
            print(f"Title: {title}")
            print(f"Tag: {tag}")
            
            # Não coloca uma quebra de linha no final
            print(f"Text: {text}", end="")
            print("-" * 50)
```

### Tratamentos de Erros com Exceptions

- **Traceback** -> palavra usada no Python para indicar um erro.
- Evitar mostrar Tracebacks para o usuário, pois expõem informações sensíveis do programa.

**Duas abordagens para tratar erros**

#### LBYL (Look Before You Leap)

Antes de tentar fazer uma operação, primeiro verifica se é possível realizar essa operação. 

Não é perfeita pois o tempo de execução do programa não é constante, sendo executado na mesma velocidade sempre.

- **Race Condition** -> é uma condição de um software aonde o comportamento do sistema é dependente de uma sequência ou tempo de eventos incontroláveis, levando a resultados inconsistentes ou inesperados.

**Exemplo de LBYL**

```python
import sys
import os

if os.path.exists("archives/names.txt"):
    input("...") # Race Condition
    names = open("archives/names.txt").readlines()
else:
    print("[Error] File names.txt not found.")
    sys.exit(1)

if len(names) >= 3:
    print(names[2])
else:
    print("[Error] Missing name in the list")
    sys.exit(1)
```

#### EAFP (Easy to Ask Forgiveness than Permission)

- Primeiro executa a operação, depois trata qualquer erro gerado.
- Deixa a complexidade algorítmica do programa melhor, pois teremos menos verificações.
- Usa a estrutura `try/except`.

**Bare except** -> captura qualquer exceção que ocorrer. Ruim, pois vários erros diferentes podem ocorrer. Não recomendado.

Sempre pensar nos erros individualmente!

- Dentro de um bloco `try` pode haver diversos `except`, cada um tratando um erro individual, maneira mais recomendada.
- São blocos de controle de fluxo, ajudam a tomar decisão sobre o fluxo do programa.
- Evitar fazer várias operações num bloco `try`.
- Possível capturar cada erro usando a palavra reservada `as`.
- Em um único `except` é possível capturar vários erros específicos.
- Pode ser usado um `else` também no bloco `try/except`, caso não houver nenhum erro, o bloco será executado.
- Também possui o `finally`, que sempre executa o bloco de código, independente se tiver ou não um erro.

É possível estourar as próprias exceções.

- `vars(__builtins__)` -> mostra uma lista com todos os erros já inseridos no Python.

Quando não souber a categoria exata do erro, o ideal é sempre utilizar um RuntimeError, erro em tempo de execução.

**Exemplo de EAFP**

```python
try:
    names = open("archives/names.txt").readlines()
except FileNotFoundError as e:
    print(str(e))
    sys.exit(1)
```
