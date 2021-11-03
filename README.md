# SERVER ON: [https://github.com/andrersp/grpc_server](https://github.com/andrersp/grpc_server)

## Get started


### How to run this project


#### Configure environment variables
Create a **settings.toml** file on the root project and put this variables:
```
[default]
SQLALCHEMY_TRACK_MODIFICATIONS=false


FLASK_ENV="development"


EXTENSIONS = [
    "grpc_client.blueprints.v1",    
    
]

```
You can change variables per environment. See more about [Dynaconf](https://www.dynaconf.com/).

Create a file **.env** to store secrets.

```
FLASK_ENV=development
FLASK_APP=grpc_client/app.py
TZ=America/Sao_Paulo
GRPC_HOST='YOUR SERVER IP ADDRESS'
GRP_PORT = 'YOUR SERVER PORT' # 50051

```

#### Run Project

```
docker-compose up --build
```
### Endpoints

## INSERT MOVIES
[http://127.0.0.1:5000/v1/movies](http://127.0.0.1:5000/v1/movies)
## Method: POST
> RESPONSE
```javascript
{
    "success": true,
}
```


## GET ALL MOVIES

[http://127.0.0.1:5000/v1/movies](http://127.0.0.1:5000/v1/movies)
## Method: GET
## url params
```javascript
{
    "page": 1, #default
    "limit": 20 #default
}
```


> RESPONSE
```javascript
{
    "reponse_time": "1.23",
    "data": [
        {
            "title": "Toy Story",
            "language": "en",
            "adult": false
        }
    ]
}
```
## GET ONE MOVIE

[http://127.0.0.1:5000/v1/movies/movie_id](http://127.0.0.1:5000/v1/movies/1)
## Method: GET
## url params

> RESPONSE
```javascript
{
    "id": 4545,
    "title": "Tango & Cash",
    "language": "en",
    "adult": false,
    "genres": [
        {
            "id": 28,
            "name": "Action"
        },
        {
            "id": 12,
            "name": "Adventure"
        },
        {
            "id": 35,
            "name": "Comedy"
        }
    ],
    "success": true
}
```