# CDU006. Gerenciar Espaço de Modalidade

- **Ator principal**: CODESP.
- **Atores secundários**: Não há atores secundários.	 
- **Resumo**: A CODESP gerencia o espaço de realização da atividade esportiva de acordo com o esporte desejado, as modalidades e suas respectivas localizações. 
- **Pré-condição**: Logar no sistema; Ter definidas as modalidades no Sistema.
- **Pós-Condição**: Após realizar o cadastro dos espaços das modalidades, devem estar definidas as localizações; Irá aparecer uma tela com opções de gerenciamento dos espaços criados, como editar, excluir etc.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Acessar interface de login | Sistema exibe interface para realizar login |  
| 2 - CODESP seleciona a opção de registrar espaço | Sistema exibe as modalidades registradas |
| 3 - CODESP seleciona uma modalidade específica | O sistema exibe e o campo de inserir a localização da modalidade |
| 4 - CODESP insere a descrição da localização e clica em salvar | O Sistema salva as informações inseridas |

## Fluxo Alternativo I - Editar

| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Acessar interface de login | Sistema exibe interface para realizar login |
| 2 - CODESP seleciona a opção de registrar espaço | Sistema exibe as modalidades registradas |
| 3 - CODESP seleciona a modalidade específica | Sistema exibe o campo de inserir a localização da modalidade |
| 4 - CODESP seleciona a opção de editar localização, insere a mensagem e clica em salvar | O Sistema salva as informações inseridas |

## Fluxo de Exceção 

| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: |  
| 1 - Acessar interface de login | Sistema exibe interface para realizar login |
| 2 - CODESP seleciona a opção de registrar espaço | Sistema exibe as modalidades registradas |
| 3 - CODESP seleciona a modalidade específica | Sistema exibe o campo de inserir a localização da modalidade |
| 4 - CODESP não insere uma descrição e clica em salvar | Sistema exibe uma mensagem de que é necessário preencher o campo | 