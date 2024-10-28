## Descrição do Projeto
Este script em Python realiza a união de vários sólidos presentes em um arquivo de malha 3D. Ele utiliza bibliotecas poderosas como `Open3D` e `Trimesh` para processar e manipular malhas 3D, aplicando reparos e operações booleanas para unir geometrias separadas em uma única malha sólida.

## Requisitos
Para executar o script, as seguintes bibliotecas devem ser instaladas:

- Open3D (versão 0.13.0)
- Trimesh (versão 3.9.29)
- SciPy (versão 1.10.1)
- NumPy (versão 1.23.5)
- NetworkX (versão 2.6.3)

As dependências podem ser instaladas utilizando o arquivo `requirements.txt` com o comando:

```sh
pip install -r requirements.txt
```

## Como Criar e Ativar um Ambiente Virtual (venv)
É recomendável utilizar um ambiente virtual para garantir que as dependências sejam instaladas corretamente e não entrem em conflito com outras bibliotecas do sistema.

### Passos para criar e ativar o ambiente virtual:
1. Crie um ambiente virtual chamado `.venv`:

```sh
python -m venv .venv
```

2. Ative o ambiente virtual:
   - No **Windows**:

   ```sh
   .venv\Scripts\activate
   ```
   - No **Linux/Mac**:

   ```sh
   source .venv/bin/activate
   ```

3. Instale as dependências no ambiente virtual:

```sh
pip install -r requirements.txt
```

## Como Executar o Script
1. Certifique-se de que as bibliotecas necessárias estão instaladas no ambiente virtual.
2. Coloque o arquivo de malha que contém os sólidos separados na mesma pasta do script e nomeie-o como `malha_separada.obj`. Você pode alterar o nome do arquivo diretamente no código, se necessário.
3. Execute o script Python para processar a malha e unir todos os sólidos em um único objeto:

```sh
python nome_do_seu_script.py
```

Após a execução bem-sucedida, o script gerará dois arquivos de saída:
- `malha_unificada.obj`: A malha unificada no formato OBJ.
- `malha_unificada.ply`: A malha unificada no formato PLY.

## Estrutura do Código
O script executa as seguintes etapas principais:
1. **Carregamento da Malha**: Utiliza `Open3D` para carregar a malha 3D inicial.
2. **Conversão e Reparos**: Converte a malha para `Trimesh` e aplica reparos, como remoção de vértices não referenciados e preenchimento de buracos.
3. **Convex Hull**: Caso a malha não seja um volume fechado, tenta aplicar um "Convex Hull" para torná-la um volume.
4. **União Booleana**: Utiliza a funcionalidade de união booleana de `Trimesh` para unir os sólidos.
5. **Salvar a Malha**: Salva a malha unificada nos formatos OBJ e PLY.

## Possíveis Problemas e Soluções
- **Malha Não Carregada**: Certifique-se de que o caminho e o nome do arquivo de entrada estão corretos.
- **Falha ao Unir as Malhas**: O script tentará converter malhas não fechadas em volumes utilizando o `Convex Hull`. Certifique-se de que as malhas são apropriadas para união.
- **Falha ao Salvar a Malha**: Verifique as permissões do diretório onde o script está sendo executado.

## Autor
Este script foi criado com o objetivo de facilitar a manipulação de malhas 3D e unir sólidos em um único modelo utilizando bibliotecas Python modernas para computação gráfica.

## Licença
Este projeto é distribuído sob a licença MIT. Sinta-se à vontade para utilizá-lo e modificá-lo conforme necessário.