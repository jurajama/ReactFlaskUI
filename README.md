# ReactFlaskUI
Demo application with React UI and Flask backend.
The basic structure originates from https://github.com/jovanni-hernandez/docker-compose-nginx-flask-react-boilerplate

## Build and run

Start in dev mode:
```
docker-compose -f docker-compose.dev.yaml up
```

After this the UI can be accessed via port 5050 of the dockerhost.
This port is defined in *docker-compose.dev.yaml*

Cleanup including deletion of the volume:
```
docker-compose -f docker-compose.dev.yaml down -v
```

## Cleanup

Remove all built images and volume:
```
docker-compose -f docker-compose.dev.yaml down -v --rmi local
```
