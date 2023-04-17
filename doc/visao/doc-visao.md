# Documento de Visão

## Histórico de Revisões

| Data                |  Versão             |          Descrição  |  Autores            |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| 22/11/2022 | 01 | Versão inicial |  Luiz Felipe, Lívia, Valtércio, Mayra e Renato Berna |
| - | - | - |  - |


## 1. Objetivo do projeto

O objetivo do projeto SIGSPORTS, Sistema de Gestão da CODESP, é facilitar e propôr mais eficiência quanto às atividades comuns que são praticadas na secretaria da CODESP, como gerenciar matrículas e turmas nos esportes. Facilitar as localizações dos espaços de modalidades e da codesp para os alunos. Melhorar atividades realizadas por professores.   

## 2. Descrição do problema

|     |      |
| --- | --- |
| **Problema**            | Informações não claras o suficientes de espaços de modalidades e da secretaria da CODESP. Ausência de métodos mais eficientes de controle de fluxo de alunos. Ausência de melhorias quanto a execução de atividades da secretaria da CODESP. |
| **Afeta**               | Alunos, Bolsistas, Professores e Secretaria da CODESP. |  
| **Impacta**             | Alunos não possuem a informação da localização dos espaços das modalidades ou da secretaria da CODESP. Professores não possuem ferramentas  que facilitam o controle de fluxo de alunos. Secretaria da CODESP não possui ferramentas que facilitam ou modernize atividades realizadas com muita frequência. |
| **Solução**             | Um sistema Web que possa solucionar esses problemas e viabilizar as necessidades da secretaria da CODESP. | 

## 3. Descrição dos usuários 

| Nome                |  Descrição          |   Responsabilidade  |
| -----------------   | -----------------   | -----------------   |
| CODESP| Coordenação de esportes. | Pessoas que fazem atividades na secretaria da CODEP | Gerenciar professores, modalidade de esportes e alunos. Fazem e autorizam o registro, matrícula de alunos em modalidades desejadas. |
| Professor | Pessoas responsáveis pela execução das práticas das modalidades. | Registrar aulas dos esportes. Realiza frequência dos alunos. Decidem a quantidade de vagas nesta modalidade de esportes.  |
| Aluno | Pessoas que frequentam as aulas de modalidade de esportes. | Tem acesso a localização das aulas de esportes. Tem acesso aos conteúdos relacionados com as modalidades. |
| Bolsista | Pessoas que fazem atividades indicadas pela secretaria da codesp. | Salvar e solicitar cadastro de alunos que são associados com modalidades. Inserir e atualizar localização das aulas de esportes. |

## 4. Descrição do ambiente dos usuários

- O ambiente é composto pela CODESP, ginásio, campos de futebol, piscinas, salas de esportes e demais ambientes para realização das práticas esportivas.
- As tarefas realizadas vão desde reuniões, aulas e outras práticas esportivas.
- A quantidade de alunos varia de acordo com o preenchimento de vagas das modalidades esportivas.


## 5. Principais necessidades dos usuários

- Dificuldade no acesso a localização da codesp e dos locais de práticas. Será disponibilizado as orientações para encontrar os locais de aulas.
- Dificuldade no acesso aos horários. Será disponibilizado os horários no sistema.
- Preenchimentos das vagas nos esportes. Será cadastrado no sistema a quantidade de vagas disponíveis aos alunos interessados e preenchimento de vagas.


## 6. Alternativas concorrentes

Atualmente, não se encontra concorrrentes. A comparação é dada por medidas analógicas.

## 7. Visão geral do produto

- A solução é imprescindível para o funcionamento da coordenação de esportes, pois através dela, pode-se otimizar o controle de matrículas e fluxo das presenças dos alunos nos esportes do IFRN. 
- Com o auxílio do sistema, os alunos e professores terão uma maior facilidade de encontrar os horários e a localização das áreas de realização das práticas de esporte. 

## 8. Requisitos funcionais

| Código              |  Nome               |          Descrição  |  Prioridade         |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| F001 | Efetuar login usuário. | A secretaria da CODESP, professores e bolsistas possuem a opção de efetuar login no sistema. | Máxima |
| F002 | Exibir Modalidades. | Um aluno pode acessar a funcionalidade que permite exibir as informações relacionadas de uma ou várias modalidades. | Moderada |
| F003 | Exibir localização da CODESP. | Um aluno pode acessar a funcionalidade que permite exibir informações quanto a localização da CODESP. | Moderada |
| F004 | Solicitar atuação em modalidade | Um professor tem a funcionalidade de realizar a solicitação da atuação de uma modalidade. | Máxima |
| F005 | Registrar horários de disponibilidade | Um professor registra os horários disponíveis com base na atuação em uma modalidade. | Máxima |
| F006 | Controle de fluxo de alunos | Um professor define o controle de fluxo de alunos durante as práticas de modalidade. | Moderada |
| F007 | Desligamento de um aluno em uma modalidade | Um professor, opcionalmente, possui a opção de remover um aluno de uma devida modalidade. | Moderada |
| F008 | Gerenciar espaço de modalidade | A secretaria da CODESP é responsável por registrar, alterar, acessar ou remover um espaço de modalidade. | Máxima |
| F009 | Gerenciar turmas | A secretaria da CODESP é responsável por registrar, alterar, acessar ou remover uma turma. | Máxima |
| F010 | Gerenciar professor | A secretaria da CODESP é responsável por registrar, alterar, acessar ou remover um espaço de uma turma. | Máxima |
| F011 | Gerenciar bolsista | A secretaria da CODESP é responsável por registrar, alterar, acessar ou remover um bolsista. | Máxima |
| F012 | Gerenciar modalidade | A secretaria da CODESP é responsável por registrar, alterar, acessar ou remover uma modalidade. | Máxima |
| F013 | Gerenciar categorias de uma modalidade. | A secretaria da CODESP é responsável por registrar, alterar, acessar ou remover as categorias de uma modalidade | Máxima |
| F014 | Autorizar matrícula | A secretaria da CODESP possui a funcionalidade de autorizar uma matrícula com base na solicitação de matrículas | Máxima |
| F015 | Solicitar matrícula em modalidades | Um bolsista possui a funcionalidade de solicitar a matrícula em uma modalidade. | Máxima |
| F016 | Registrar uso de espaço de atividade | Um bolsista possui a funcionalidade de registrar e catalogar o controle de fluxo sobre a execução de atividades em um espaço de modalidade. | Moderada |

## 9. Requisitos não-funcionais

| Código              |  Nome               |          Descrição  |  Categoria          |  Classificação      |
| :-----------------: | :-----------------: | :-----------------: | :-----------------: | :-----------------: |
| NF01 | Controle de acesso Usuário | Bolsistas relacionadas com a CODESP e professores podem efetuar o login. | Segurança | Obrigatório |
| NF02 | Usabilidade | Boa eficiência de atividades realizadas no sistema. | Performance | Desejável |
| NF03 | Acessibilidade | O sistema fornece um formato fácil para executar as funcionalidades | Performance | Desejável |
| NF04 | Curva de aprendizado | O sistema é simples de se compreender. | Performance | Desejável |
| NF05 | Uso simultâneo | Múltiplos usuários podem fazer um login e acessar as funcionalidades do sistema | Performance | Obrigatório |
