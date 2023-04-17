# CDU007. Desligamento de Aluno

- **Ator principal**: Professor
- **Atores secundários**: Aluno	 
- **Resumo**: O professor poderá realizar o desligamento de um aluno de sua turma. Esse desligamento poderá ocorrer em razão da baixa frequência do aluno, infrações cometidas, ou outro motivo. O desligamento implica na remoção do aluno da turma. 
- **Pré-condição**: Logar no sistema; O professor deve estar alocado em uma turma; A turma deve possuir alunos matriculados.
- **Pós-Condição**: Após realizar o desligamento do aluno, ele não deverá mais aparecer na turma, assim como não deverá aparecer na lista de frequência.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :----------------- | :----------------- | 
| 1 - Acessar interface de login | Sistema exibe interface para realizar login |  
| 2 - O(a) professor(a) seleciona o campo turmas | Sistema exibe as turmas que o professor esta alocado |
| 3 - O(a) professor(a) seleciona uma turma | Sistema exibe informações da turma e alunos |
| 4 - O(a) professor(a) seleciona um aluno em específico | Sistema exibe a opção de desligamento|
| 5 - O(a) professor(a) clica em desligamento de aluno | Sistema exibe o campo de texto para justificar o desligamento |
| 6 - O(a) professor(a) clica em salvar | Sistema remove aluno da turma |


## Fluxo Alternativo I - Busca por nome

| Ações do ator | Ações do sistema |
| :----------------- | :----------------- | 
| 1 - Acessar interface de login | Sistema exibe interface para realizar login |  
| 2 - O(a) professor(a) seleciona o campo turmas | Sistema exibe as turmas que o professor esta alocado |
| 3 - O(a) professor(a) seleciona uma turma | Sistema exibe os alunos matriculados nesta turma |
| 4 - O(a) professor(a) seleciona insere o nome de um aluno na barra de pesquisa | Sistema exibe os alunos matriculados nesta turma|
| 5 - O(a) professor(a) seleciona o aluno pesquisado | Sistema exibe a opção de desligamento|
| 6 - O(a) professor(a) clica em desligamento de aluno | Sistema exibe o campo de texto para justificar o desligamento |
| 7 - O(a) professor(a) clica em salvar | Sistema remove aluno da turma |


## Fluxo de Exceção 

| Ações do ator | Ações do sistema |
| :----------------- | :----------------- |  
| 1 - Acessar interface de login | Sistema exibe interface para realizar login |  
| 2 - O(a) professor(a) seleciona o campo turmas | Sistema exibe as turmas que o professor esta alocado |
| 3 - O(a) professor(a) seleciona uma turma | Sistema exibe os alunos matriculados nesta turma |
| 4 - O(a) professor(a) seleciona insere o nome de um aluno na barra de pesquisa | Sistema exibe os alunos matriculados nesta turma|
| 5 - O(a) professor(a) seleciona o aluno pesquisado | Sistema exibe a opção de desligamento|
| 6 - O(a) professor(a) clica em desligamento de aluno | Sistema exibe o campo de texto para justificar o desligamento |
| 7 - O(a) professor(a) não insere descrição e clica em salvar | Sistema exibe a mensagem de que é necessário inserir a justificativa para realizar o desligamento |
