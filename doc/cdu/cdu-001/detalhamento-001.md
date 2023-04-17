# CDU001. Login

- **Ator principal**: Professor, Bolsista e pessoas da CODESP
- **Atores secundários**: Não há atores secundários.	 
- **Resumo**: Um usuário insere as credenciais, matrícula ou e-mail e senha, para as informações serem autenticadas e por sua vez, ser redirecionado para uma interface associada com um usuário específico que exibe suas devidas funcionalidades.
- **Pré-condição**: Acessar o sistema.
- **Pós-Condição**: Redirecionamento de interface.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 -  Acessar sistema | Sistema é inicialzado.|  
| 2 -  Acessar interface de login | Sistema exibe interface para realizar login.|  
| 3 - Inserir matrícula/e-mai e senha | Sistema recebe dados de usuário inseridos. A autenticação é feita e o sistema redireciona para próxima interface.| 



## Fluxo Alternativo I - ...
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - Usuário acessa sistema | Sistema é inicialzado.|  
| 1.2 - Usuário Acessa interface de login | Sistema exibe interface para realizar login. |
| 1.3 - Usuário recupera senha | Sistema envia um e-mail para poder recuperar uma senha |
| 1.4 - Usuário Insere matrícula/e-mai e senha | Sistema recebe dados de usuário inseridos. A autenticação é feita e o sistema redireciona para próxima interface. |

## Fluxo Alternativo II - ...
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - Usuário acessa sistema | Sistema é inicialzado. |  
| 2.2 - Usuário Acessa interface de login | Sistema exibe interface para realizar login. |  
| 2.3 - Usuário Insere matrícula/e-mai e senha | Sistema recebe dados de usuário inseridos. Uma exceção é lançada por conta de uma falha na autenticação. |  
