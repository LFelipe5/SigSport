# CDU013. Gerenciar categoria de uma modalidade

- **Ator principal**: CODESP.
- **Atores secundários**: Não há atores secundários.	 
- **Resumo**: A coordenação gerencia as categorias de uma modalidade, podendo criar,atualizar, deletar ou apenas e.
- **Pré-condição**: Logar no sistema e modalidades devem estar cadastradas.
- **Pós-Condição**: Sistema executa ação desejada pela CODESP, seja ela cadastrar,visualizar,atualizar. 

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - CODESP acessa o sistema na internet | Inicialização do Sistema|  
| 2 - Acessar interface de login| Sistema exibe interface para realizar login.|
| 3 - CODESP acessa a funcionalidade gerenciar modalidades| Sistema exibe as modalidades cadastradas|
| 4 - CODESP seleciona a modalidade desejada | Sistema exibe a funcionalidades da modalidade|
| 5 - CODESP seleciona a funcionalidade gerenciar categoria de modalidade  | Sistema exibe as categorias e funcionalidades de categorias|
| 6 - CODESP seleciona a opção adicionar nova categoria para a modalidade  | Sistema exibe formulário para preenchimento de informações da nova categoria|
| 7 - CODESP preenche formulário e aperta a opção cadastras | Sistema cadastra nova categoria para a modalidade |

## Fluxo alternativo 1
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - CODESP acessa o sistema na internet | Inicialização do Sistema|  
| 2 - Acessar interface de login| Sistema exibe interface para realizar login.|
| 3 - CODESP acessa a funcionalidade gerenciar modalidades| Sistema exibe as modalidades cadastradas|
| 4 - CODESP seleciona a modalidade desejada | Sistema exibe a funcionalidades da modalidade|
| 5 - CODESP seleciona a funcionalidade gerenciar categoria de modalidade  | Sistema exibe as categorias e funcionalidades de categorias|
| 6 - CODESP seleciona uma categoria e seleciona a opção excluir categoria selecionada  | Sistema deleta categoria selecionada|

