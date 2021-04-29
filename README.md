# aiohttp, rabbitmq, redis and peewee project scaffolding

## run the project
command: 
```shell script
$ docker-compose up --build --remove-orphans
$ docker-compose exec app bash
$ python create_table.py
```

sample request:

```shell script
curl --request GET \
  --url http://localhost:8040/ \
  --header 'Content-Type: application/json'
```

```shell script
curl --request POST \
  --url http://localhost:8040/api/v1/users \
  --header 'Content-Type: application/json' \
  --data '{
	"username": "rhasan33",
	"password": "16031989",
	"name": "Rakib Hasan Amiya",
	"email": "rhasan.amiya@gmail.com"
}'
```

