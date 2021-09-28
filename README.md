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
- docker/docker-compose


<br/>

#### Instalar o projeto no windows

depois de clonar o projeto, abra o powershell como administrador
e digite o seguinte comando:

`Set-ExecutionPolicy RemoteSigned`

<br/>

## Após clonar o projeto digite o comando tanto no windows como no linux
`docker-compose build`

#### Iniciar no Windows

`.\up.ps1 FALSE`

caso queira iniciar em modo de produção digite "TRUE" e não "FALSE"

<br/>

#### Iniciar no linux

`chmod +x up.sh`

`chmod +x data_stone_app/wait_for_psql.sh`

`./up.sh FALSE`

caso queira iniciar em modo de produção digite "TRUE" e não "FALSE"

##### Abra o seu navegador preferido e digite:
- http://localhost:8081/ - para a documentação
- http://localhost:8000/ - para a API

<br/>

## Endpoints
`http://localhost:8000/api/?from=USD&to=BRL&amount=5`

#### Resposta
```
{
    "status": "success",
    "msg": 26.58
}
```

#A API só tem suporte para a criptomoeda bitcoin
