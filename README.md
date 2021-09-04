# lzw-compressor

Este algoritmo disponibiliza um arquivo principal, o main.py
onde o usuário, através do terminal, pode executar o mesmo,
a fim de realizar as atividades de compressão e descompressão
de arquivos de texto no formato .txt.

### Requerimentos
- Python 3.x^

### Modo de usar
Execute o seguinte comando no terminal
```
$ python3 main.py arg1 arg2 arg3
```
Ex:
```
$ python3 main.py encode ./textos/01.txt ./resultados/01.bin

$ python3 main.py decode ./binarios/01.bin ./resultados/01.txt
```

### Valores dos argumentos
Para comprimir um arquivo de texto, utilizar os seguintes valores

| Argumento  |            Valor                    |                                 Descrição                                                |
| -----------| ----------------------------------- | ---------------------------------------------------------------------------------------- |
|  arg1      |  'encode'                           | Nome da operação para comprimir um arquivo de texto                                      |
|  arg2      |  Path para o arquivo de texto       | Este argumento recebe um path que indica o arquivo de texto que deve ser comprimido      |
|  arg3      |  Path para salvar o arquivo binário | Este argumento recebe um path que indica o local onde o arquivo binário vai ser salvo.   |

Para descomprimir um arquivo binário, utilizar os seguintes valores

| Argumento  |             Valor                    |                                   Descrição                                               |
| ---------- | ------------------------------------ | ----------------------------------------------------------------------------------------- |
|  arg1      |  'decode'                            | Nome da operação para descomprimir um arquivo de texto                                    |
|  arg2      |  Path para o arquivo binário         | Este argumento recebe um path que indica o arquivo binário que deve ser lido              |
|  arg3      |  Path para salvar o arquivo de texto | Este argumento recebe um path que indica o local onde o arquivo de texto vai ser salvo.   |

### Funcionamento
Ao iniciar o programa, é feito uma validação dos argumentos passado,
a fim de determinar se eles se adequam ao que o algoritmo espera receber
para poder funcionar da maneira esperada. Se uma validação falhar,
uma mensagem aparece na tela falando sobre a falha, e o programa encerra.
Em caso da validação passar, o algoritmo chama uma função
para abrir o arquivo de texto ou binário, dependendo do tipo da operação.
Após isso, em caso de compressão, o algoritmo chama uma função para comprimir
o arquivo, e em seguinda chama outra função para salvar o resultado
em um arquivo binário. Em caso de descompressão, o algoritmo
chama uma função para ler o arquivo binário, e em seguida chama outra função
para salvar o resultado em um arquivo de texto.

Este trabalho foi desenvolvido como avaliação parcial
para a matéria de Sistemas Multimídia, ministrada pelo
Professor Doutor Raoni Simões Ferreira, na
Universidade Federal do Acre (UFAC)

### Autores
|         ALUNO              |  MATRÍCULA   |
| -------------------------- | ------------ |
|  Italo Oliveira            |  20170300021 |
|  Thalisson Bandeira Araújo |  20170300046 |
