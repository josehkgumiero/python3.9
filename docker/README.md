# Docker

# Install on Ubuntu
- Meet the system requirements;
- Have a 64-bit version of either the latest LTS version or the current non-LTS version;
- Docker Desktop is supported on x86_64 or amd64;
- For non-Gnome Desktop environments, gnome-erminal must be installed: ``sudo apt install gnome-terminal``
- Update the apt: `` sudo apt-get update ``
- Install
```
sudo apt-get update
sudo apt-get install \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo apt-get install docker-ce
```
- Download the latest DEB package;
- Install the package with apt: `` sudo apt-get install ./docker-desktop-4.28.0-amd64.deb``
- The post-install script:
    - Sets the ports
    - Sets resource limits
    - Adds DNS name for KUbernetes to ``/etc/hosts``
    - Creates a symink from ``/usr/local/bin/com.docker.cli`` to ``/usr/bin/docker``.

# Launch Docker Desktop
- ``systemctl --user start docker-desktop``
- Checks the versions of binaries:
    - ``docker comppose version``
    - ``docker --version``
    - ``docker version``
- To stop Docker Desktop: ``systemctl --user stop docker-desktop``

# Upgrade Docker Desktop
- ``sudo apt-get install ./docker-desktop-<version>-<arch>.deb``
