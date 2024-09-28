#!/usr/bin/env bash

printf "%s\n" "Syncing repositories"

apt update

printf "%s\n" "Installing Dependencies"

apt install software-properties-common apt-transport-https wget -y

printf "%s\n" "Installing Microsoft Repositories gpg key"

apt install wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | apt-key add -

printf "%s\n" "Adding Microsoft Visual Studio Code Repositories"

add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"

printf "%s\n" "Installing Visual Studio Code"

apt install code -y
