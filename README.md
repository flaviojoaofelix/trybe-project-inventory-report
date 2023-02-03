# Trybe

## Curso de Desenvolvimento Web Full-Stack

- *Módulo de Ciências da Computação*


## Projeto: Inventory Report

:construction: EM CONSTRUÇÃO :construction:

## Tecnologias Utilizadas no Projeto

### 1. **Python**[^2]

- Como a linguagem principal do projeto.

### 2. **Pytest**[^3]

- Para desenvolvimento dos testes da aplicação.

## Como Utilizar

:construction: EM CONSTRUÇÃO :construction:

## REQUISITOS DO PROJETO

<details>
  <summary>Lista de Requisitos do Projeto</summary>
  
  # Requisitos obrigatórios

## 1 - Testar o construtor/inicializador do objeto Produto
> **Crie o teste em:** tests/product/test_product.py

  <p align="center">
    <img src="/.images/construtor.png " alt="Imagem de construtor em Python"  width="600"/>
  </p>

Ao analisar o código do projeto, você encontrará a classe do objeto produto já implementada neste arquivo: `inventory_report/inventory/product.py`, a classe **Product**.

Para termos confiança em continuar as implementações, precisamos que você implemente o teste, que certifique que o método `__init__` da classe Product esta funcionando corretamente.

O nome deste teste deve ser `test_cria_produto`, ele deve verificar o correto preenchimento dos seguintes atributos:
  - id (int)
  - nome_da_empresa (string)
  - nome_do_produto (string)
  - data_de_fabricacao (string)
  - data_de_validade (string)
  - numero_de_serie (string)
  - instrucoes_de_armazenamento (string)

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - **1** - Deve criar um novo produto com todos os atributos corretamente preenchidos.

</details>

<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>
  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme seu objetivo, e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendindo quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code>, ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>


## 2 - Gerar a versão simplificada do relatório

> **Crie a classe em:** inventory_report/reports/simple_report.py

O relatório deve ser gerado através de um método estático ou de classe chamado `generate` escrito dentro da classe `SimpleReport`.

- Ao rodar os testes localmente, você terá um teste para cada validação de cada informação
- Deve ser possível executar o método `generate` sem instanciar um objeto de `SimpleReport`
- O método deve receber um parâmetro que representa uma `list` (estrutura de dados), onde cada posição contém um `dict`(estrutura de dados).

Exemplo de formato de entrada

```json
   [
     {
       "id": 1,
       "nome_do_produto": "CADEIRA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-04-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar em local fresco"
     }
   ]
```

- O método deverá retornar uma `string` de saída com o seguinte formato:
   ```bash
   Data de fabricação mais antiga: YYYY-MM-DD
   Data de validade mais próxima: YYYY-MM-DD
   Empresa com mais produtos: NOME DA EMPRESA
   ```
- A data de validade mais próxima, somente considera itens que ainda não venceram.

**Dica:** O módulo [datetime](https://docs.python.org/3/library/datetime.html) pode te ajudar.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


  - **2.1** - O método generate da classe SimpleReport deve retornar todas informações do relatório simples. Informações necessárias:
    - a data de fabricação mais antiga
    - a validade mais próxima
    - a empresa com maior número de produtos

  - **2.2** - O método generate da classe SimpleReport deve retornar o formato correto do relatório simples

    📌 Atente-se a espaçamentos e quebras de linhas

</details>

## 3 - Gerar a versão completa do relatório

> **Crie em:** inventory_report/reports/complete_report.py

O relatório deve ser gerado através de um método `generate` para a classe `CompleteReport`.
Ele deverá receber dados numa lista contendo estruturas do tipo `dict` e deverá retornar uma string formatada como um relatório.

- A classe `CompleteReport` deve herdar da classe `SimpleReport` e sobrescrever o método `generate`, de modo a especializar seu comportamento.

- Deve ser possível executar o método `generate` sem instanciar um objeto de `CompleteReport`
  
- O método deve receber de parâmetro uma lista de dicionários no seguinte **formato**:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "MESA",
       "nome_da_empresa": "Forces of Nature",
       "data_de_fabricacao": "2022-05-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "Conservar ao abrigo de luz"
     }
   ]
   ```

- O método deverá retornar uma saída com o seguinte formato:

```bash
Data de fabricação mais antiga: YYYY-MM-DD
Data de validade mais próxima: YYYY-MM-DD
Empresa com mais produtos: NOME DA EMPRESA
Produtos estocados por empresa:
- Physicians Total Care, Inc.: QUANTIDADE
- Newton Laboratories, Inc.: QUANTIDADE
- Forces of Nature: QUANTIDADE
```

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


  - **3** - O método generate da classe CompleteReport deve retornar todas informações do relatório completo no formato correto. Informações necessárias:
    - a data de fabricação mais antiga
    - a validade mais próxima
    - a empresa com maior estoque
    - a quantidade de produtos por empresa, ordenado pela mesma ordem que as empresas aparecem na lista de entrada

</details>

## 4 - Gere os relatórios através de um arquivo CSV
> **Crie em:** inventory_report/inventory/inventory.py

A importação do arquivo CSV deve ser realizada através do método `import_data` que você deve criar em uma classe chamada `Inventory`.
    
O método deve ser estático ou de classe, ou seja, deve ser possível chamá-lo sem instanciar um objeto da classe.

O método receberá como primeiro parâmetro uma string como caminho para o arquivo `CSV` e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - **4** - Ao importar um arquivo CSV, deve retornar o relatórios simples ou o completo conforme solicitado.

</details>

## 5 - Gere os relatórios através de um arquivo JSON
> **Incremente em:** `inventory_report/inventory/inventory.py`. 

> 📌 Utilize o mesmo método do requisito anterior.

Altere o método `import_data` para que ele também seja capaz de carregar arquivos `JSON`.
    
Como no requisito anterior, o método ainda receberá como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).


<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


- **5** - Ao importar um arquivo JSON, deve retornar o relatórios simples ou o completo conforme solicitado.

</details>

## 6 - Gere os relatórios através de um arquivo XML
> **Incremente em:** `inventory_report/inventory/inventory.py`. 

> 📌 Utilize o mesmo método do requisito anterior.
    
Altere o método `import_data` para que ele também seja capaz de carregar arquivos `XML`.
    
Como no requisito anterior, o método ainda receberá como primeiro parâmetro uma string como caminho para o arquivo, e como segundo parâmetro uma string que representa o tipo de relatório a ser gerado. Tipos:
 - `"simples"`
 - `"completo"`

De acordo com os parâmetros recebidos, deve recuperar os dados do arquivo e chamar o método de gerar relatório correspondente à entrada passada. Ou seja, o método da classe `Inventory` deve chamar o método `generate` da classe que vai gerar o relatório (`SimpleReport`, `CompleteReport`).


<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>
  
  - **6** - Ao importar um arquivo XML, deve retornar o relatórios simples ou o completo conforme solicitado.

</details>

## 7 - Organizar o código de importação com o padrão Strategy
> **Crie em:** inventory_report/importer/importer.py

Como pôde observar até aqui, o método `import_data` está com muitas responsabilidades, e, com o intuito de resolver isso, podemos dividir a sua complexidade para cada formato de arquivo.

O padrão de projeto `Strategy` nos ajuda a isolar cada estratégia em um objeto, e por meio de uma Interface podemos padronizar a assinatura dos métodos, garantindo que todas elas possuam o comportamento similar.

- Ao rodar os testes localmente, você terá um teste para cada validação de cada informação
- Crie uma classe abstrata `Importer` para ser a interface da estratégia
- A Interface será uma classe abstrata `Importer` terá três classes de estratégias herdeiras: `CsvImporter`, `JsonImporter` e `XmlImporter`.
- Crie as classes nos respectivos arquivos:
  > inventory_report/importer/csv_importer.py
  > inventory_report/importer/json_importer.py
  > inventory_report/importer/xml_importer.py

- A classe abstrata deve definir a assinatura do método `import_data` a ser implementado por cada classe herdeira. Esse método deve ser estático ou de classe, e deve receber como parâmetro o nome do arquivo a ser importado.

- O método `import_data` definido por cada classe herdeira deve lançar uma exceção do tipo `ValueError` caso a extensão do arquivo passado por parâmetro seja inválida. Por exemplo, quando se passa um caminho de um arquivo com extensão `.csv` para o `JsonImporter`. A mensagem de erro da exceção deve ser _"Arquivo inválido"_.

- O método deverá ler os dados do arquivo passado e retorná-los estruturados em uma lista de dicionários conforme exemplo abaixo:

   ```json
   [
     {
       "id": 1,
       "nome_do_produto": "Cafe",
       "nome_da_empresa": "Cafes Nature",
       "data_de_fabricacao": "2020-07-04",
       "data_de_validade": "2023-02-09",
       "numero_de_serie": "FR48",
       "instrucoes_de_armazenamento": "instrucao"
     }
   ]
   ```

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - **7** - As classes estratégicas `CsvImporter`, `JsonImporter` e `CsvImporter` devem cada uma:
      - herdar a classe `importer`
      - importar e retornar os dados para uma lista (`list`) de dicionários (`dict`)
      - validar se ao enviar um arquivo com extensão incorreta deve gerar um erro

</details>


## 8 - Testar o relatório individual do produto
> **Crie o teste em:** tests/product_report/test_product_report.py

Boa novidade, o primeiro relatório já implementamos neste arquivo `inventory_report/inventory/product.py`. Formulamos uma frase construída com as informações do produto, que será muito útil para etiquetarmos o estoque.

Para desenvolver este relatório, utilizamos o recurso `__repr__` do Python, que permite alterar a representatividade do objeto, para que sempre que usarmos um print nele, no lugar de endereço de memória, teremos uma String personalizada.

**Dica:** A reimplementação do `__repr__` não faz o objeto retornar exatamente uma `string`, fazer um `cast` para `string`, pode te ajudar.

Exemplo da frase:
> O produto `farinha` fabricado em `01-05-2021` por `Farinini` com validade até `02-06-2023` precisa ser armazenado `ao abrigo de luz`.

Agora para mantermos uma boa cobertura de testes, precisamos que você implemente o teste.

O nome deste teste deve ser `test_relatorio_produto`, ele deve instanciar um objeto `Product` e verificar se acessá-lo a frase de retorno esta correta.

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>


  - **8** - Se seu código testa que o retorno padrão (`__repr__`) de um objeto `Product` deve ser um relatório sobre ele 
</details>
    
<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>
  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme seu objetivo, e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendindo quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code>, ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>


## 9 - Testar a geração de uma versão do relatório em cores
> **Crie o teste em:** tests/report_decorator/test_report_decorator.py

Uma versão deste relatório será exibida em letreiros em Led, estes letreiros são coloridos, para isso, já implementamos o método responsável por retornar este relatório em cores.

> Implementamos em : inventory_report/reports/colored_report.py

Em vez de criarmos uma classe que herda os relatórios originais, utilizamos o padrão `Decorator` para receber o tipo do relatório por composição (`SimpleReport` ou `CompleteReport`) e, assim, colorir o retorno do método `generate`, que recebe uma lista de produtos e retorna o relatório já colorido.

Para termos confiança que as cores sairão corretamente, precisamos que você implemente o teste, que certifique que o método **generate**  de **ColoredReport** funciona corretamente.

Para que o Python consiga colorir as strings, é preciso que a string contenha o início do código da cor, e o reset da cor.

📌 Execute este print teste em um terminal interativo `python3 -i`. O resultado das cores podem não ser exatos, por isso, atente-se aos códigos deste exemplo:

```python
print("\033[36mAzul\033[0m \033[32mVerde\033[0m \033[31mVermelho\033[0m")
```

  <p align="center">
    <img src="/.images/print_colorido.png" alt="Logo Flask"/>
  </p>

O nome deste teste deve ser `test_decorar_relatorio`, ele deve verificar se o relatório está devidamente colorido. Representamos abaixo como deve ser a disposição das cores:

<span style="color: green;">🟩Data de fabricação mais antiga:🟩</span> <span style="color: blue;">🟦10-05-2022🟦</span>

<span style="color: green;">🟩Data de validade mais próxima:🟩</span> <span style="color: blue;">🟦14-06-2021🟦</span>

<span style="color: green;">🟩Empresa com mais produtos:🟩</span> <span style="color: red;">🟥Farinini🟥</span>

  
<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - **9** - Deve retornar o relatório devidamente colorido.
    - **verde:**
        - "Data de fabricação mais antiga:"
        - "Data de validade mais próxima:"
        - "Empresa com mais produtos:"
    -  **azul:** As datas
    - **vermelho:** Nome da empresa com mais produtos
</details>

<details>
  <summary>
    <b>📌Como seu teste é avaliado</b>
  </summary>
  O <strong>teste da Trybe</strong> irá avaliar se o <strong>seu teste</strong> está passando conforme seu objetivo, e confirmará se ele está falhando em alguns casos que deve falhar.
  Para estes testes que esperemos que falhe, o requisito será considerado atendindo quando a resposta do Pytest for <code>XFAIL(Expected Fail)</code>, ao invés de <code>PASS</code> ou <code>FAIL</code>.
</details>

# Requisitos bônus

## 10 - Criar uma classe `InventoryIterator`

> **Crie em:** inventory_report/inventory/inventory_iterator.py
    
O estoque será mostrado por painéis de led. Para não sobrecarregarmos a memória destes painéis, queremos poder iterar pelos itens do estoque, um item por vez. Para isso, precisamos primeiro refatorar a forma com que importamos os dados, e então aplicar o Padrão Iterator.
 
- A classe `Inventory` deverá ser refatorada (copiada) em outro arquivo chamado `inventory_report/inventory/inventory_refactor.py`. Nesse arquivo você irá refatorar a classe `Inventory` chamando-a de `InventoryRefactor`.

- A classe `InventoryRefactor` deve utilizar as classes definidas no requisito 8 para lidar com a lógica de importação, via **composição** no método `import_data`.

- A classe `InventoryRefactor` deve receber por seu construtor a classe que será utilizada para lidar com a lógica de importação e armazenar em um atributo chamado `importer`.
  
- A classe `InventoryRefactor` deve ter um método *de instância* que recebe um caminho para o arquivo a ser importado, e carrega seus dados.

- Ao importar os dados, os mesmos devem ser armazenados na instância, em adição aos itens já presentes naquela instância. O atributo de `InventoryRefactor` que armazena esses dados deve se chamar `data`.

- Os atributos e os métodos devem ser públicos.

- A classe `InventoryIterator` deverá implementar a interface de um iterator (`Iterator`) com o método `__next__`. Além disso, a classe `InventoryRefactor` deve implementar o método `__iter__`, que retornará este iterador.
    
- As classes `InventoryIterator` e `InventoryRefactor` devem implementar corretamente a interface do padrão de projeto **Iterator**, de modo que seja possível iterar sobre os itens em estoque.
    

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary>

```python
iterator = iter(inventory)
first_item = next(iterator)
```
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - 10.1 - Será validado que a instancia de InventoryRefactor é iterável (Iterable)

  - 10.2 - Será validado que é possível iterar o primeiro item da lista usando csv

  - 10.3 - Será validado que é possível iterar o primeiro item da lista usando json

  - 10.4 - Será validado que é possível iterar o primeiro item da lista usando xml

  - 10.5 - Será validado que é possível receber duas fontes de dados sem sobrescrita

  - 10.6 - Será validado que não é possível enviar arquivo inválido

</details>

## 11 - Preencha a função `main` no módulo `inventory_report/main.py`

Essa função deve, ao receber pela linha de comando o caminho de um arquivo e o tipo de relatório, devolver o relatório correto.

- Deverá ser usado a classe `InventoryRefactor` para recuperar os dados e gerar o relatório.

- Ao chamar o comando no formato abaixo pelo terminal, deve ser impresso na tela o devido relatório no formato da saída dos requisitos `3` e `4`: 

```bash
inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
```

- Caso a chamada tenha menos de três argumentos (o nome `inventory_report` é considerado o primeiro argumento), exiba a mensagem de erro "Verifique os argumentos" na `stderr`.
    
**Dicas:**
  - Se o comando não encontrar o pacote `inventory_report`, basta executar `pip install .` na raiz do projeto.

  - Você pode utilizar o `sys.argv` para receber a entrada de dados da pessoa usuária.
    
  - Ao utilizar algo do módulo `sys`, faça a importação com `import sys` e utilize `sys.xxxx` (onde xxxx é o que você quer utilizar). Não faça `from sys import xxxx`, pois isso pode fazer com que os testes não passem.
    
  - Tome a precaução de não deixar um `print()` em seu código, pois ele irá conflitar com os testes.

<details>
  <summary>
    <b>✍️ Teste manual</b>
  </summary> No ambiente virtual onde seu projeto foi configurado, instale o próprio projeto com o comando
  <code>pip install .</code>
  Agora execute o projeto com:
  <code>inventory_report parametro_1 parametro_2</code>
  exemplo:
  <code>inventory_report inventory_report/data/inventory.csv simples</code>
  Desta forma você conseguirá interagir gerar o relatório com o comando.
</details>

<details>
  <summary>
    <b>🤖 O que será verificado pelo avaliador</b>
  </summary>

  - 11.1 - Será validado se pelo comando é possível importar um arquivo csv simples

  - 11.2 - Será validado se pelo comando é possível importar um arquivo csv completo

  - 11.3 - Será validado se pelo comando é possível importar um arquivo json simples

  - 11.4 - Será validado se pelo comando é possível importar um arquivo json completo

  - 11.5 - Será validado se pelo comando é possível importar um arquivo xml simples

  - 11.6 - Será validado se pelo comando é possível importar um arquivo xml completo

  - 11.7 - Será validado se houverem argumentos faltantes será retornando um erro
  
 </details>
