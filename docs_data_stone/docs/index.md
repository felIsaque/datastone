# DataStone

<br/>
## Sobre a API

API desenvolvida para disponibilizar dados sobre organizações que trabalham
com código aberto.

<br/>
## Como executar o projeto


#### Pré-requisitos

- Python >= 3.7
- poetry
- powershell: caso esteja no windows


<br/>

#### Instalar o projeto no windows

depois de clonar o projeto, abra o powershell como administrador
e digite o seguinte comando:

`Set-ExecutionPolicy RemoteSigned`

<br/>

#### Iniciar no linux

`chmod +x up.sh FALSE`

caso queira iniciar em modo de produção digite "TRUE" e não "FALSE"

`chmod +x data_stone_app/wait_for_psql.sh`

`./up.sh`


##### Abra o seu navegador preferido e digite:
- http://localhost:8081/ - para a documentação
- http://localhost:8000/ - para a API