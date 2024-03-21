# Manage data in Docker

By default all files created inside a container are stored on a writable container layer. This means that:

- The data does not persist when tht container no onger exists, and it can be difficult to get the data out of the container if another proces needs it.

- A ctaoniner's writable layer is tightly coupled to te host machine, where the container is running. ou can not easily move the data somewhere else.

- Writing into a container's writable layer requires a storage driver to manage the filesystem. The storage driver provides a union filesystem, using the Linux kernel. This extra abstraction reduces performance as compared to using data volumes, which write directly to the host filesystem.

Docker has two options for containers to store files on the host machine, so that the files are persisted even after the container stops: volumes, and bind mounts.

Docker also supports containers storing files in-memory on the host machine. Such files are not persisted. If you are running Dokcer on Linux, tmpfs mount is used to store files in the host's system memory. If you are running Docker on Windows, named pipe is used to store files in the host's system memory.

# Choose the right type of mount

No matter which type of moount you choose to use, the data looks the same from within the container. It is exposed as either a directory or an individual file in the container's filesystem.

- Volumes are stored in a part of the host filesystem which is maanged by Docker. Non-Docker processes should not modify this part f the filesystem. Volumes are the best way to persist data in Docker.

- Bind mounts may be stored anywhere on te host system. They may even be important system files or directories. Non-Docker processes on the Docker host or a Docker container can modify them at any time.

- tmpfs mounts are stored in the host system's memory only, and are never written to the host system's filesystem.

# Volumes

Volumes are created and managed by Docker. You can create a volume explicitly using the docker volume create command, or Docker can create a volume during container or service creation.

When you create a volume, it is stored within a directory on the Docker host. When you mount the volume into a container, this directory is what is mounted into the container. This is similar to the way that bind mounts work, except that volumes are managed by Docker and are isolated from the core functionality of the host machine.

A given volume can be mounted into multiple containers simultaneously. When no running container is using a volume, the volume is still available to Docker and is not removed automatically. You can remove unused volumes using docker volume prune.

When you mount a volume, it may be named or anonymous. Anonymous volumes are given a random name that is guaratnteed to be unique within a given Docker host. Just like named volumes, anonymous volumes persist even if you remove the container that uses them, except if you use the --rm flag when creating the container, in which case the anonymous volume is destroyed.If you create multiple cotainers after each other that use anonymous volumes, ech container creates its own volume. Anonymous volumes are not reused or shared between containers automatically. To share an anonymous volume between two or more containers, you must mount the anonymous volume using the random volume ID.

Volumes also support the use of volume drivers, which allow you to store your data on remote hosts or cloud providers, among other possibilities.

# Bind mounts

Bind mounts have limited functionality compared to volumes. When you use a bind mount, a file or directory on the host machine is mounted into a container. The file or directory is referenced by its full path o the host machine. The file or directory does not need to exist on the Docker host already. It is created on demand if it does not yet exist. Bind mounts are fast, but they rely on the host machine's filesystem having a specific directory structure avialable. If you are developing new Docker applications, consider using named volumes instead. You can not use Docker CLi commands to directly manage bind mounts.

# tmpfs

A tmpfs mount is not perssited on disk, either on the Docker host or within a container. It can be used by a container during the lifetime of the container, to store non-persistent state or sensitive information. For instance, inernally, Swarm services use tmpfs mounts to mount secrets into a service's containers.

# Good use cases for volumes

Volumes are the preferred way to persist data in Docker containers and services. Some use cases for volumes include:

Sharing data among multiple running containers. If you don't explicitly create it, a volume is created the first time it is mounted into a container. When that container stops or is removed, the volume still exists. Multiple containers can mount the same volume simultaneously, either read-write or read-only. Volumes are only removed when you explicitly remove them.

When the Docker host is not guaranteed to have a given directory or file structure. Volumes help you decouple the configuration of the Docker host from the container runtime.

When you want to store your container's data on a remote host or a cloud provider, rather than locally.

When you need to back up, restore, or migrate data from one Docker host to another, volumes are a better choice. You can stop containers using the volume, then back up the volume's directory (such as /var/lib/docker/volumes/<volume-name>).

When your application requires high-performance I/O on Docker Desktop. Volumes are stored in the Linux VM rather than the host, which means that the reads and writes have much lower latency and higher throughput.

When your application requires fully native file system behavior on Docker Desktop. For example, a database engine requires precise control over disk flushing to guarantee transaction durability. Volumes are stored in the Linux VM and can make these guarantees, whereas bind mounts are remoted to macOS or Windows, where the file systems behave slightly differently.

# Good use cases for bind mounts

In general, you should use volumes where possible. Bind mounts are appropriate for the following types of use case:

Sharing configuration files from the host machine to containers. This is how Docker provides DNS resolution to containers by default, by mounting /etc/resolv.conf from the host machine into each container.

Sharing source code or build artifacts between a development environment on the Docker host and a container. For instance, you may mount a Maven target/ directory into a container, and each time you build the Maven project on the Docker host, the container gets access to the rebuilt artifacts.

If you use Docker for development this way, your production Dockerfile would copy the production-ready artifacts directly into the image, rather than relying on a bind mount.

When the file or directory structure of the Docker host is guaranteed to be consistent with the bind mounts the containers require.

# Good use cases for tmpfs mounts

tmpfs mounts are best used for cases when you do not want the data to persist either on the host machine or within the container. This may be for security reasons or to protect the performance of the container when your application needs to write a large volume of non-persistent state data.