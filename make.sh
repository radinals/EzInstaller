#!/bin/env bash


echo "Building EzInstaller"
#
[ ! -f "./dist" ] && mkdir -p ./dist
shiv --site-packages dist --output-file ezinstaller.pyz -e "EzInstaller.main:main" .

program_name="EzInstaller"
theme_file="theme.rasi"
download_script_folder="scripts"
download_script_index_file="index.csv"
download_script_runner="runner.sh"

config_dir="$XDG_CONFIG_HOME"

[ -z "$config_dir" ] && config_dir="$HOME/.config"

if [ ! -d "$config_dir" ]; then
    echo "Creating Program Directory at '$(basename $config_dir)'"
    mkdir -p "$config_dir"
fi

prg_config_path="$config_dir/$program_name"

if [ ! -d "$prg_config_path" ]; then 
    echo "Copying Over Configuration Files to '$(basename $prg_config_path)'"
    cp -r -f "./resource" "$prg_config_path"
fi

echo "Done.. Now please move the EzInstaller executable to your system path directory"
