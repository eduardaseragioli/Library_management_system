# Library_management_system
<img align="right" src="https://prowly-prod.s3.eu-west-1.amazonaws.com/uploads/landing_page/template_background/216005/ca9c16d3f4f72edbc3efd6b86f253019.jpg" width="400">

### Sistema de Gestão da Biblioteca EMMA

----------------------------------------

##  Índice
| | | |
| :--- | :--- | :--- |
|  [Sobre o Projeto](#sobre-o-projeto) |  [Objetivos](#objetivos) |  [Tecnologias](#tecnologias-utilizadas) |
|  [Como Rodar](#como-rodar-o-projeto) |  [Estrutura](#estrutura-do-repositório) |  [Autores](#autores---grupo-gr7) |
----------------------------------------

## Sobre o Projeto

Este projeto foi desenvolvido como parte do Projeto Multidisciplinar da faculdade IADE - Lisboa. O objetivo principal é a criação de um software para automatizar os processos de uma biblioteca, substituindo controles manuais por um sistema digital eficiente que otimiza o tempo e a organização das informações.

O sistema permite o gerenciamento completo de acervos, usuários, funcionários e movimentações (empréstimos e devoluções), garantindo maior confiabilidade nos dados e agilidade no atendimento ao leitor.

----------------------------------------

## Objetivos

 - Automatização: Eliminar o uso de registros manuais e processos burocráticos.

 - Controle de Acervo: Facilitar o cadastro, a consulta e a manutenção de livros e materiais.

 - Gestão de Usuários: Registrar e gerenciar leitores e funcionários com diferentes níveis de acesso.

 - Otimização de Processos: Reduzir o tempo de espera em empréstimos e devoluções, melhorando a experiência do usuário.

----------------------------------------

## Tecnologias Utilizadas

 - Linguagem: Python 

 - Interface Gráfica: PyQt5 (arquivos .ui convertidos/carregados)

 - Banco de Dados: MySQL (para armazenamento persistente de dados)

 - Persistência de Dados: Arquivo SQL para criação da estrutura do banco

----------------------------------------

## Como Rodar o Projeto

Pré-requisitos
Certifique-se de ter o Python instalado e um servidor MySQL ativo.

1. Instalação das Dependências
No terminal, instale as bibliotecas necessárias:

Bash

pip install PyQt5 mysql-connector-python <br>
(Nota: No macOS, pode ser necessário usar a flag --break-system-packages se você não estiver em um ambiente virtual).

2. Configuração do Banco de Dados
Importe o arquivo Mat_Discreta.sql para o seu servidor MySQL.

Verifique as credenciais de conexão no arquivo databaseManager.py.

3. Execução
Para iniciar o sistema, execute o arquivo principal:

Bash

python main.py <br>

----------------------------------------

## Estrutura do Repositório

 - main.py: Ponto de entrada do sistema.

 - databaseManager.py: Gerenciamento da conexão e queries do banco de dados.

 - login.py / menu.py: Lógica das interfaces de acesso e navegação.

 - *.ui: Arquivos de interface desenvolvidos no Qt Designer.

 - Relatório Final.pdf: Documentação técnica completa do projeto.

----------------------------------------

## Autores - Grupo GR7
Eduarda Seragioli, Miriam Martins e margarida Tinoco.
