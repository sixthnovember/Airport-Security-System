# Description

You can use this folder as a structure for your solution. You can put your services in the subfolders (`collector` and `human-detection`). 
The rest of the subfolders are not in use by `docker-compose.yml` here.

Make sure that you have **Docker** installed on your system. You can enable local **Kubernetes** via **Docker** as well. 

## Run all:
```
  docker-compose up 
```

or 

```
  docker-compose --compatibility up 
```
Running with the compatibility flas will allow you to specify resource constraints in docker-compose.yml without going into container orchestration mode (Swarm).


### Some other useful docker-compose switches:

```
--build           - Builds images before starting containers, very useful during development.
--force-recreate  - Recreates containers even if their configuration and image have not changed. Also useful, as sometimes the changes aren't detected.
```

### Stopping and cleaning up:

You can stop docker-compose by pressing `CTRL+C`, if you want to completelly remove created containers, networks, volumes, and images created by up `docker-compose.yml` then run: 

```
docker-compose down --rmi --remove-orphans 
```

See more here: https://docs.docker.com/compose/reference/

### Trying Out

To send a request to a service in your local environment, e.g., the camera service you can do the following: 

`curl http://localhost:31100/frame `

To try the image analysis, send an example json from the `test` folder like this: 

`curl -X POST -H "Content-Type: application/json" -d @test-base64-image.json http://localhost:31200/frame`

The service should return: 

```
{
    "image": "<base64-image-data>",
    "persons": [
        {
            "age": "25-32",
            "gender": "Male"
        }
    ]
}
```


## Without Docker Compose

### To pull existing services  

Get the image from Docker Hub into your local environment:
```
    docker pull ccuni/camera-service-2022w
    docker pull ccuni/image-analysis-service-2022w
    docker pull ccuni/face-recognition-service-2022w
    docker pull ccuni/section-service-2022w
    docker pull ccuni/alert-service-2022w
```

### To run a service:
```
  docker run -p<yourport>:80 ccuni/<service-name>-service-2022w
```

Choose network if you need it, e.g., `--network <my-net>`.

Choose network aliasses as you need the, e.g., `--net-alias <service-name>`.

Create docker-compose files as you need them...
