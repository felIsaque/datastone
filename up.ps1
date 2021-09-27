$EnvApp = $args[0]

(Get-Content .env) -replace 'DEB.*', "DEB=$($EnvApp)" | Set-Content .env

if ($EnvApp -eq "FALSE")
{
    docker-compose up
}
else
{
    docker-compose -f docker-compose.prod.yml up
}
