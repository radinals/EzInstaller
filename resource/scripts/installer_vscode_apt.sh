#!/usr/bin/env bash
#
printf "%s\n" "Installing Dependencies"

apt update

apt install software-properties-common apt-transport-https wget gpg -y

printf "%s\n" "Installing Microsoft Repositories and gpg key"

wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > packages.microsoft.gpg

install -D -o root -g root -m 644 packages.microsoft.gpg /etc/apt/keyrings/packages.microsoft.gpg

echo "deb [arch=amd64,arm64,armhf signed-by=/etc/apt/keyrings/packages.microsoft.gpg] https://packages.microsoft.com/repos/code stable main" | \
    tee /etc/apt/sources.list.d/vscode.list > /dev/null

rm -f packages.microsoft.gpg

printf "%s\n" "Installing Visual Studio Code"

apt update

apt install code -y
