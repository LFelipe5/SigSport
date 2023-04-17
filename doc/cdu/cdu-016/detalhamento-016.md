# CDU016. Registrar uso de espaço de atividade

- **Ator principal**: Bolsista
- **Atores secundários**: Não há atores secundários.	 
- **Resumo**: O bolsista possui a funcionalidade de registrar o uso de espaço de atividades. Em outras palavras, um bolsista precisa ter as informações de um professor com sua respectiva turma e modalidades para registrar um uso de um espaço para uma modalidade. Um bolsista pode alterar, acessar ou remover os registros, também.
- **Pré-condição**: Necessário haver um professor, uma turma e modalidade.
- **Pós-Condição**: É registrado no sistema informações sobre o uso de um espaço de modalidade.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Bolsista acessa sistema| Sistema é inicialzado.|  
| 2 - Bolsista acessa interface de login | Sistema exibe interface para realizar login.|  
| 3 - Bolsista insere matrícula/e-mai e senha | Sistema recebe dados de usuário inseridos. A autenticação é feita e o sistema redireciona para próxima interface.|
| 4 - Bolsista insere informações que fazem um registro. | Sistema recebe dados de usuário inseridos. É registrado no sistema, dados relacionado com o uso de um espaço de modalidades para atividades.|
| 5 - Bolsista acessa as informações de registros disponíveis. | Sistema exibe dados do uso de espaços de modalidades.|




## Fluxo Alternativo I - Alterar
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - Bolsista acessa sistema| Sistema é inicialzado.|  
| 1.2 - Bolsista acessa interface de login | Sistema exibe interface para realizar login.|  
| 1.3 - Inserir matrícula/e-mai e senha | Sistema recebe dados de usuário inseridos. A autenticação é feita e o sistema redireciona para próxima interface.|
| 1.4 - Um bolsista acessa as informações de registros disponíveis. | Sistema exibe dados do uso de espaços de modalidades.|
| 1.5 - Um bolsista Bolsista altera um registro disponível | Sistema altera dados do uso de espaços de modalidades.|

## Fluxo Alternativo II - Remover
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 2.1 - Usuário acessa sistema | Sistema é inicialzado. |  
| 2.2 - Usuário Acessa interface de login | Sistema exibe interface para realizar login. |  
| 2.3 - Usuário Insere matrícula/e-mai e senha | Sistema recebe dados de usuário inseridos. Uma exceção é lançada por conta de uma falha na autenticação. | 
| 2.4 - Um bolsista acessa as informações de registros disponíveis. | Sistema exibe dados do uso de espaços de modalidades.|
| 2.5 - Um bolsista Bolsista remove um registro disponível | Sistema remove dados do uso de espaços de modalidades.|
