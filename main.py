from EzInstaller.SelectionMenu import SelectionMenu
from EzInstaller.DownloadProcess import DownloadProcess

import os

if __name__ == "__main__":
    rofi_theme = f"{os.getcwd()}/EzInstallerRofi.rasi"
    SelMenu = SelectionMenu(f"rofi  -dmenu -theme '{rofi_theme}' -p '' -markup -no-sort - hover-select - me-select-entry '' - me-accept-entry MousePrimary",
                            f"{os.getcwd()}/InstallerScripts/index.csv",
                            f"{os.getcwd()}/InstallerScripts")

    while not SelMenu.hasStartDownload():
        SelMenu.start()

    Downloader = DownloadProcess(
        SelMenu.getSelectedScripts(),
        f"{os.getcwd()}/InstallerScripts/ScriptRunner.sh")

    Downloader.runScripts()
