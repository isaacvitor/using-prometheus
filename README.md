# using-prometheus
How to instrumenting an application using Prometheus

## How to run
>Be sure you have Docker and pipenv installed.

Edit `nginx.conf` and change the ip to your network ip:
```
events {}
http {
  upstream loadbalancer {
    server 127.0.0.1:3000 weight=5; <-- here
    server 127.0.0.1:3001 weight=5; <-- here
  }

  server {
    location / {
      proxy_pass http://loadbalancer;
    }
  }
}
```

Run:
```
$ pipenv run start
```

Finally:

```
docker run -d --name my_load_balancer -v $PWD/nginx.conf:/etc/nginx/nginx.conf:ro -p 8088:80 nginx
```

##Install Prometheus Client:

Follow the instructions: https://github.com/prometheus/client_python