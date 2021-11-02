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

## GET ALL MOVIES

[http://127.0.0.1:5000/v1/movies](http://127.0.0.1:5000/v1/movies)

## Method: GET
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
