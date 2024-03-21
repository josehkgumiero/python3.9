# Docker Engine

Docker Engine is an open source containerization technology for building and containerizing your applications.

Docker Engine acts as a client-server application with:

- A server with a long-running daemon process dockerd.

- APIs which specify interface that programs can use to talk to and instruct the Docker daemon.

- A command line interace (CLI) client docker.

The CLI uses Docker APIs to control or interact with the Docker daemon through scripting or direct CLI commands. Many other Docker applications use the underlying API and CLI. The daemon creates and manages Docker ojects, such as images, containers, networks, and volumes.