# CDU010. Gerenciar Professor

- **Ator principal**: CODESP
- **Atores secundários**: Não há atores secundários.	 
- **Resumo**: Uma pessoa da secretaria da CODESP possui algumas funcionalidades relacionadas com professores. Dentre elas, o registro de um professor, editar os dados de um professor, visualizar a quantidade de professores e excluir um professor do total registrado.
- **Pré-condição**: Alguém da secretaria da CODESP precisa fazer login no sistema.
- **Pós-Condição**: Um professor pode ser registrado no sistema. Um professor pode ter os dados atualizados no sistema. Um professor pode ser deletado do sistema.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 -  O usuário da CODESP faz login no sistema. | A funcionalidade do login é acionada no sistema.|  
| 2 -  O usuário da CODESP acessa a funcionalidade que permite realizar ações com professores. | O sistema exibe uma interface relacionada com o gerenciamento de professores.|  
| 3 -  O usuário insere dados de um professor (Nome, matrícula, identificação, descrição) | Sistema recebe dados de usuário inseridos. É armazenado dados de um professor no sistema.| 



## Fluxo Alternativo I - Registrar
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário da CODESP faz login no sistema. | A funcionalidade do login é acionada no sistema.|  
| 1.2 - O usuário da CODESP acessa a funcionalidade que permite realizar ações com professores. | O sistema exibe uma interface relacionada com o gerenciamento de professores. |
| 1.3 - O usuário seleciona uma opção para exibir os professores no sistema | O sistema exibe todos os professores disponíveis. |
| 1.4 - O usuário deleta um professor escolhido no sistema. | Um dado de um professor é deletado do sistema. |

## Fluxo Alternativo II - Remover
| Ações do ator | Ações do sistema |
| :-----------------: |:-----------------: | 
| 1.1 - O usuário da CODESP faz login no sistema. | A funcionalidade do login é acionada no sistema.|  
| 1.2 - O usuário da CODESP acessa a funcionalidade que permite realizar ações com professores. | O sistema exibe uma interface relacionada com o gerenciamento de professores. |
| 1.3 - O usuário seleciona uma opção para exibir os professores no sistema | O sistema exibe todos os professores disponíveis. |
| 1.4 - O usuário deleta um professor escolhido no sistema. | Um dado de um professor é deletado do sistema. |

## Fluxo Alternativo III - Alterar
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 3.1 - O usuário da CODESP faz login no sistema. | A funcionalidade do login é acionada no sistema.|  
| 3.2 - O usuário da CODESP acessa a funcionalidade que permite realizar ações com professores. | O sistema exibe uma interface relacionada com o gerenciamento de professores. |
| 3.3 - O usuário seleciona uma opção para exibir os professores no sistema | O sistema exibe todos os professores disponíveis. |
| 3.4 - O usuário altera um professor escolhido no sistema. | Um dado de um professor é alterado do sistema. | 
