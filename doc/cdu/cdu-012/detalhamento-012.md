# CDU012. Gerenciar modalidade

- **Ator principal**: CODESP
- **Atores secundários**: Não há atores secundários.
- **Resumo**: Uma pessoa da secretaria da CODESP possui algumas funcionalidades relacionadas com modalidades. Dentre elas, o registro de uma modalidade, editar os dados de uma modalidade, visualizar a modalidade e excluir uma modalidade do total registrado.

- **Pré-condição**: AO usuário da CODESP precisar estar logado no sistema para executar uma das funções.

- **Pós-Condição**: Uma modalidade pode ser registrada no sistema. Uma modalidade pode ter os dados atualizados no sistema. Uma modalidade pode ser deletada do sistema.

## Fluxo Principal

|                                                         Ações do ator                                                         |                     Ações do sistema                      |
| :---------------------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------: |
|                                         1 - O usuário da CODESP faz login no sistema.                                         |         Sistema é inicialzado com usuário logado.         |
|                  2 - O usuário da CODESP acessa a funcionalidade que permite realizar ações com modalidades                   |     Sistema exibe interface referente as modalidades.     |
| 3 - O usuário insere dados de um professor (nome da modalidade, identificação, descrição de modalidade, espaço da modalidade) | Sistema recebe os dados e cadastra em seu banco de dados. |
|                                   4 - O usuário deleta uma modalidade escolhido no sistema.                                   | Sistema deleta os dados referente amodalidade solicitado. |
