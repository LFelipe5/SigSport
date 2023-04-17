# CDU015. Solicitar matrícula em modalidade

- **Ator principal**: Bolsista.
- **Atores secundários**: Não há atores secundários.	 
- **Resumo**: O bolsista preenche as informações do aluno que deseja ser matriculado em uma modalidade e é enviada uma solicitação para a coordenação autorizar ou não a matrícula.
- **Pré-condição**: Logar no sistema, ter aluno definido, um professor junto com modalidade registrado e um bolsista.
- **Pós-Condição**: O sistema adiciona um pedido de matrícula de um aluno em uma modalidade, na qual será enviada para a coordenação autorizar ou não as matrículas.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Bolsista acessa o sistema na internet | Inicialização do Sistema|  
| 2 - Bolsista acessa interface de login | Sistema exibe interface para realizar login.|
| 3 - Bolsista acessa a funcionalidade solicitar matricula de aluno em modalidade | Sistema exibe as modalidades cadastradas|
| 4 - Bolsista informa dados do aluno a ser matriculado e seleciona a opção cadastrar  | Sistema exibe informações de alunos já disponíveis para matrícula e recebe um dado do tipo aluno.|
| 5 - Bolsista seleciona a modalidade desejada pelo aluno | Sistema exibe modalidades disponíveis e recebe o dado de uma modalidade selecionada|
| 6 - Bolsista seleciona a categoria de modalidade desejada pelo aluno | Sistema exibe categoria de modalidades disponíveis e recebe o dado de uma categoria de modalidade selecionada|


## Fluxo Alternativo
| Ações do ator | Ações do sistema |
| :-----------------: | :-----------------: | 
| 1 - Bolsista acessa o sistema na internet | Inicialização do Sistema|  
| 2 - Bolsista acessa interface de login | Sistema exibe interface para realizar login.|
| 3 - Bolsista acessa a funcionalidade de solicitação de matrícula em modalidade e visualiza pedidos de matrícula disponíveis  | Sistema exibe os pedidos de matrículas|
