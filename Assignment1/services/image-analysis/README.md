# ImageAnalysis Service

Get the image from Docker Hub:
```
  docker pull ccuni/image-analysis-service-2022w
```

Run:
```
  docker run -p<yourport>:80 ccuni/image-analysis-service-2022w
```
or run inside your Docker network:
 ```
  docker run -p<yourport>:80 --network <my-net> --net-alias image-analysis ccuni/image-analysis-service-2022w
```

Test:
```
  curl http://<yourport>:80/probe
```
