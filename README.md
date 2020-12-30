# Flask
Microservice/API

## Running MYSQL Docker
`docker run --rm -d --name mysql -p 3306:3306 -e MYSQL_ROOT_PASSWORD=test -e MYSQL_DATABASE=authz -e MYSQL_USER=authz -e MYSQL_PASSWORD=authz mysql`

## Define Connection String
`export AUTHZ_DATABASE_URI=mysql+pymysql://authz:authz@localhost:3306/authz`

## DB Migration and Getting Started
`flask db init`

`flask db migrate -m "initial migrate" ` 

`flask db upgrade`

## Run Flask
`flask run`

## Create a User
`Curl -i -H ‘Content-Type: application/json’ localhost:5000/api/v1/users -d ‘{“username”:”admin”,”password”:”123”}’ `

`Curl -i -H ‘Content-Type: application/json’ localhost:5000/api/v1/users -d ‘{“username”:”test”,”password”:”123”}’`

## Get a Token
`Curl -i -H ‘Content-Type: application/json’ localhost:5000/api/v1/auth/tokens -d ‘{“username”:”admin”,”password”:”123”}’ `

## Get List of Users
`curl -i -H 'Content-Type: application/json' localhost:5000/api/v1/auth/tokens -H 'X-Auth-Token: {token}’ `


