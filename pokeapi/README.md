## Installation
You can run demo of the app with Docker and Docker Compose:

```bash
docker-compose up --build
```

##### Create User
Post username and password for next url:
 ```bash 
http://localhost:8080/api/auth/users/
``` 
You can get an authorization token(jwt) for an address(Need post your username and password)
 ```bash 
http://localhost:8080/api/auth/jwt/create/
```


### Added pokemons
in order to add a pokemon you need to log(Bearer token), as well as change it by post request pokemon_name
 ```bash 
http://localhost:8080/api/home/
```
you can get players list by 
 ```bash 
http://localhost:8080/api/list-player/
```