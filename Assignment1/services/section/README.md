# section Service

Get the image from Docker Hub:
```
  docker pull ccuni/section-service-2022w
```

Run:
```
  docker run -p<yourport>:80 ccuni/section-service-2022w
```
or run inside your Docker network:
 ```
  docker run -p<yourport>:80 --network <my-net> --net-alias section ccuni/section-service-2022w
```

Test:
```
  curl http://<yourport>:80/probe
```
