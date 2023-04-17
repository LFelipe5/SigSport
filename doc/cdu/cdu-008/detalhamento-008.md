# CDU008. Gerenciar bolsista

- **Ator principal**: CODESP.
- **Atores secundários**: Não há atores secundários.	 
- **Resumo**: Um usuário da secretaria da CODESP realiza o cadastro de bolsistas no sistema.
- **Pré-condição**: Usuário estar logado no sistema.
- **Pós-Condição**: Sistema executa ação desejada pela CODESP, seja ela cadastrar,visualizar,atualizar. 

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - CODESP acessa o sistema na internet | Inicialização do Sistema|  
| 2 - Acessar interface de login| Sistema exibe interface para realizar login.|
| 3 - CODESP acessa a funcionalidade gerenciar bolsista| Sistema exibe interface para efetuar cadastro|
| 4 - CODESP insere dados para o cadastro de um bolsista| Sistema efetua cadastro de um bolsista|

## Fluxo alternativo 1
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - CODESP acessa o sistema na internet | Inicialização do Sistema|  
| 2 - Acessar interface de login| Sistema exibe interface para realizar login.|
| 3 - CODESP acessa a funcionalidade gerenciar bolsista| Sistema exibe interface de bolsistas cadastrados|
| 4 - CODESP acessa a opção de alterar informações de um bolsista| Sistema efetua alteração de dados de um bolsista|
| 5 - CODESP acessa a opção de remover informações de um bolsista| Sistema efetua remoção de dados de um bolsista|
