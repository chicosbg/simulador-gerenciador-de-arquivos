# Sobre

O **Gerenciador de Arquivos** é um simulador do funcionamento de um sistema de arquivos em um sistema operacional. Um sistema de arquivos é uma camada de software que organiza, gerencia e armazena dados em dispositivos de armazenamento, como discos rígidos, SSDs ou pen drives.

O disco é divido em unidades gerenciaveis (blocos), que armazenam os arquivos e diretórios em uma hierarquia acessível. O sistema de arquivos então rastreia esses blocos, que podem estar livres ou ocupados no disco, e fornece um método uniforme para ler e gravar dados. 

+ Evita diperdício.
+ Garante uso eficiente do dispositivo.
+ Garante compatibilidade para vários dispositivos.

# Pré-requisitos e instalação

O sistema é desenvolvido na linguagem __python__, que pode ser feito o download [aqui](https://www.python.org/downloads/). O simulador pode ser visualizado [aqui](https://github.com/chicosbg/simulador-gerenciador-de-arquivos.git)

Primeiramente deve ser clonado o repositório do projeto com o comando:

```$
git clone https://github.com/chicosbg/simulador-gerenciador-de-arquivos.git
```

Com repositório clonado instale as dependências (é obrigatório o pacote estar instalado):
```Bash
pip install -r ./requirements.txt
```

Acesse a pasta do projeto e execute o arquivo main.py:

```$
python3 src/main.py
```

# Funcionamento do Simulador

A cada passo da simulação, o programa realiza as seguintes operações:

+ Cria o processo principal (que estará executando sempre no programa).
+ Enquanto executa, verifica se ocorreu uma interrupção (há 15% de chance de ocorrer uma interrupção).
+ Caso ocorra uma interrupção, coloca a interrupção na fila de interrupções (de acordo com a prioridade).
+ Salva o contexto do processo principal e o interrompe.
+ Trata as interrupções da fila (é possível que cheguem novas interrupções).
+ Retoma o contexto do processo principal e continua a execução.

# Arquitetura do Sistema

A arquitetura do simulador é composta pelos seguintes contextos: ``Base``, ``Diretórios``, ``Interface de comando``, ``Models`` e ``Operações`` cada uma com responsabilidades específicas que contribuem para o funcionamento do programa.

## Base

Esse contexto é composto por classes fundamentais que dão o suporte inical para o funcionamento do sistema

### Gerenciador de Diretórios

Classe que gerencia as operações de arquivos e diretórios do simulador. É responsável por cirar e listar os arquivos e possui métodos para "caminhar" pelos diretórios para chegar ao destino informado pelo usuário
  
### Gerenciador de Dispositivos

Classe que encapsula o disco e possui métodos para sua manipulação, como alocar bloco e liberar bloco

### OS
  
Classe que abstrai o papel do sistema operacional, centralizando as ações e chamando os componentens necessários no devido momento, tanto para tratar as operações requeridas pelo usuário quanto para ser um contexto que encapsula os outros componentes básicos do sistema.

## Diretórios

### Diretorio 

Esse contexto é composto apenas pela classe Diretorio que faz a abstração dos diretórios no sistema de arquivos. A classe possui os atributos: sub_diretorios (uma lista de diretorios filhos), raiz (diretorio pai) e arquivos (uma lista de arquivos filhos), além de métodos para adicionar diretório e adicionar arquivo. Essa organização torna a estrtura de dados responsável por representar o sistema de arquivos como uma árvore n-ária, com um "ponteiro" para o nodo pai.

## Interface de Comando

### Interface de Comando

Esse contexto é composto apenas pela classe InterfaceComando que apenas cria um ambiente de terminal virtual na execução do programa e capta a entrada do usuário de forma correta (sem permitir comandos e parâmetros inválidos)

## Models

### Arquivo

Uma classe simples para armazenar algumas informações importantes que cada arquivo deve possuir: uma referencia para o bloco no disco, o tamanho do arquivo em blocos, o nome do arquivo, a data de criação e uma refernecia para um arquivo real criado na pasta ``arquivos`` do simulador.

### Bloco

A classe bloco funciona como uma estrtura nodo de uma lista encadeada, tendo como os seguintes atributos: proximo, deletado e id.

### Disco

Classe que representa o disco, possuindo como atributos: numero de blocos totais, numero de blocos livres e um array que representa os "nodos" ou blocos em si. Possuindo métodos para adicionar, buscar e remover blocos.

## Operações

### Tratador de Operações

Esse contexto possui apenas a classe TratadosComandosCMD que é uma classe chamada pelo SO para tratar todas as funções geradas a partir dos comandos digitados pelo usuário ou seja: ``ls``, ``pwd``, ``cd``, ``mkdir``, ``touch``, ``rm``, ``open`` e ``status``


Classes fundamentais e que e que dão o suporte inicial para o funcionamento do sistema
  -- base --
## Gerenciador de Diretórios
## Gerenciador de Dispositivos
## OS

Classe que abstrai o funcionamento dos diretórios no sistema
-- Diretorios --
## Diretorio

Classe responsável por implementar o interfaceamento de linha de comnado com o usuario tal qual é feito em um terminal linux
-- Interface de Comando --
## Interface de Comando

Classes que utilizam das classes bases para o seu funcionamento
-- Models --
## Arquivo
## Bloco
## Disco

Responsável por executar de forma lógica os comandos digitados no terminal pelo usuário
-- Operações --
## Tratador de Operações


# Cenários de Testes

O simulador possui alguns cenário possíveis durante a sua execução:

## Execução Contínua do Processo

A execução normal do processo principal sem interrupções. Nesse caso o processo é executado continuamente, incrementando e simulando os valores de tempo, pc e ponteiro para pilha.

## Geração de Interrupções

A chance de gerar uma interrupção é de 15%, nesse caso ocorrem as seguintes ações:

+ A interrupção é registrada no log.
+ O contexto do processo é salvo.
+ A interrupção é adicionada na fila de interrupções.

## Tratamento de Interrupções

As interrupções na fila são tratadas pelo sistema operacional. Quando uma nova interrupção chega, é possível que ela possua uma prioridade maior do que uma interrupção que esteja sendo tratada no mesmo instante. Nesse caso, o sistema operacional passa o tratamento para a interrupção de maior prioridade.

## Retomada do Processo Principal

O processo principal é retomado após o tratamento das interrupções. Isso ocorre quando a fila de interrupções está totalmente vazia, nesse caso os valores de tempo, pc e ponteiro da pilha do processo principal são retomados.
