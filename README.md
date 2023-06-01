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