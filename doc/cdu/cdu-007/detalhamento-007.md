# CDU007. Controle de Fluxo

- **Ator principal**: Professor
- **Atores secundários**: Aluno	 
- **Resumo**: O Professor realiza o controle de fluxo dos alunos presentes em uma determinada aula. Irá criar uma aula, inserir informações como descrição da aula como atividades desenvolvidas, outras observações, e inserir as presença e falta dos alunos. 
- **Pré-condição**: Logar no sistema; O professor deve estar alocado em uma turma; A turma deve possuir alunos alocados.
- **Pós-Condição**: Após criar a aula e inserir as presenças e faltas dos alunos, devem estar visíveis a turma com suas respectivas aulas cadastradas, alunos e os dias de aulas recentes; Irá aparecer opções de gerenciamento das aulas criadas, como editar, excluir etc.

## Fluxo Principal
| Ações do ator | Ações do sistema |
| :----------------- | :----------------- | 
| 1 - Acessar interface de login | Sistema exibe interface para realizar login |  
| 2 - O(a) professor(a) seleciona o campo turmas | Sistema exibe as turmas que o professor esta alocado |
| 3 - O(a) professor(a) seleciona uma turma | Sistema exibe as aulas registradas nesta turma |
| 4 - O(a) professor(a) clica em criar nova aula | Sistema cria uma nova aula |
| 5 - O(a) professor(a) insere o título da aula | Sistema salva o título da aula |
| 6 - O(a) professor(a) pode inserir descrição para a aula | Sistema salva a descrição da aula caso haja |
| 7 - O(a) professor(a) realiza a chamada inserindo presença ou falta | Sistema salva o fluxo de presença |
| 8 - O(a) professor(a) clica em salvar | Sistema registra a aula |


## Fluxo Alternativo I - Editar

| Ações do ator | Ações do sistema |
| :----------------- | :----------------- | 
| 1 - Acessar interface de login | Sistema exibe interface para realizar login |  
| 2 - O(a) professor(a) seleciona o campo turmas | Sistema exibe as turmas que o professor esta alocado |
| 3 - O(a) professor(a) seleciona uma turma | Sistema exibe as aulas registradas nesta turma |
| 4 - O(a) professor(a) seleciona uma aula e clica em editar | Sistema exibe as informações da aula |
| 5 - O(a) professor(a) realiza as alterações e clica em salvar | Sistema salva as alterações |

## Fluxo de Exceção 

| Ações do ator | Ações do sistema |
| :----------------- | :----------------- |  
| 1 - Acessar interface de login | Sistema exibe interface para realizar login |  
| 2 - O(a) professor(a) seleciona o campo turmas | Sistema exibe as turmas que o professor esta alocado |
| 3 - O(a) professor(a) seleciona uma turma | Sistema exibe as aulas registradas nesta turma |
| 4 - O(a) professor(a) clica em criar nova aula | Sistema cria uma nova aula |
| 5 - O(a) professor(a) insere não insere o título da aula | Sistema exibe mensagem para inserir o titulo |
