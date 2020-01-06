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

## How it works

### UI

UI-application has originally been created with *create-react-app* tool,
see https://reactjs.org/docs/create-a-new-react-app.html

In dev mode the ui-container both builds and serves the content of UI using React
development server.

In prod mode the ui container is only used for building the ui content to docker volume
and after that the container stops. The compiled ui files are statically served by nginx.

### API server
When the stack is started up in dev-mode, api-server uses Flask development server
and takes the code at runtime from the dockerhost directory via volume mapping.
This implies that when you modify api code on dockerhost, the api-server is automatically
reloaded with the new code.

When the stack is created in prod-mode, the api-server is run with gunicorn and the code
is copied inside the container image so it cannot be modified at runtime and can be executed
anywhere where the image is taken.

### nginx proxy

nginx acts as a proxy in front of UI and API, so that a single IP/port can be used to access both
statically served UI components and the API endpoints.

nginx serves UI files from a docker volume *static-ui-content* that is created by docker-compose.
ui-container build process produces the files to the volume.

Connection between nginx and api-server goes via Docker overlay network *web_nw* created
by docker-compose. Only the TCP-port that nginx itself listens is exposed to outside world.


## UI development

Installing new npm components to ui requires node installation on your development workstation.
In *demo-app* some components have been installed as an example with these commands:
```
npm install --save bootstrap
npm install --save reactstrap react react-dom
```

That example is from https://reactstrap.github.io.
Installing a new component updates package.json and package-lock.json that shall both be
committed to git.

## Cleanup

Remove all built images and volume:
```
docker-compose -f docker-compose.dev.yaml down -v --rmi local
```
