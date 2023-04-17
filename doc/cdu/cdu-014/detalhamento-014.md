# CDU014. Autorizar matrícula

- **Ator principal**: CODESP.
- **Atores secundários**: Não há atores secundários.	 
- **Resumo**: A coordenação recebe uma lista de solicitações de matrícula enviada pelo bolsista com a opção de autorizar ou não.
- **Pré-condição**: Logar no sistema, ter componentes da coordenação definidos e pedidos de matrícula registrados. 
- **Pós-Condição**: O sistema adiciona uma autorização de matrícula em uma modalidade.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Coordenação acessa o sistema| Inicialização do Sistema|  
| 2 - Coordenção realiza login | O sistema realiza a autenticação do usuário|
| 3 - CODESP seleciona uma opção para abrir lista de solicitações de matrículas | Sistema exibe lista com as solicitações de matrículas que foram enviadas pelo bolsista |
| 4 - CODESP seleciona os alunos aptos por ordem de solicitação e escolhe a opção autorizar matrícula de alunos selecionados  | Sistema efetua uma ou mais autorizações de marícula |
