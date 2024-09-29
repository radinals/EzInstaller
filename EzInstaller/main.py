from .SelectionMenu import SelectionMenu
from .DownloadProcess import DownloadProcess
from .Config import Config


import os


def getConfigPath():
    config_dir = os.getenv("XDG_CONFIG_HOME")

    if (config_dir and os.path.exists(f"{config_dir}/{Config.program_name}")):
        return config_dir
    else:
        return f"{os.getenv("HOME")}/.config/{Config.program_name}"


def main():
    config_path = getConfigPath()

    if not os.path.exists(config_path):
        print("Error: cannot find required configuration files")
        exit()

    SelMenu = SelectionMenu(f"rofi  -dmenu -theme '{config_path}/{Config.theme_file}' -p '' -markup -no-sort - hover-select - me-select-entry '' - me-accept-entry MousePrimary",
                            f"{config_path}/{Config.download_script_index_file}",
                            f"{config_path}/{Config.download_script_folder}")

    while not SelMenu.hasStartDownload():
        SelMenu.start()

    Downloader = DownloadProcess(
        SelMenu.getSelectedScripts(),
        f"{config_path}/{Config.download_script_runner}")

    Downloader.runScripts()


if __name__ == "__main__":
    main()
