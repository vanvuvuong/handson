# Setup newest docker build backend

## Option 1: Setup Buildkitd

Refer to [here](https://github.com/moby/buildkit/releases) to download the newest buildkit commandline tools.

- Unzip package, make executable, copy to system binary folder & link to super user binary:

```
tar -xvf buildkit-vx.x.x.linux-amd64.tar.gz
chmod +x bin/*
sudo mv bin/* /usr/local/bin/
sudo ln -Ls /usr/local/bin/build* /sbin/
```

- Setup for `buildkitd` service:

```
sudo tee /etc/systemd/system/buildkitd.service >/dev/null <<-EOF
#*************************************************
#***************  BuildKit Daemon  ***************
#*************************************************
[Unit]
Description=BuildKit Daemon
ConditionFileIsExecutable=/usr/local/bin/buildkitd
After=syslog.target network.target

[Service]
StartLimitInterval=5
StartLimitBurst=10
ExecStart=/usr/local/bin/buildkitd
Restart=always
RestartSec=120

[Install]
WantedBy=multi-user.target
EOF
sudo systemctl daemon-reload
sudo systemctl enable buildkitd
sudo systemctl start buildkitd
```

# Option 2: Add Buildkitx plugin

```
wget https://github.com/docker/buildx/releases/download/v0.14.0/buildx-v0.14.0.linux-amd64
sudo mv docker-buildx /usr/lib/docker/cli-plugins/
sudo chmod 777 /usr/lib/docker/cli-plugins/docker-buildx
```
