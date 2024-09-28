from EzInstaller.SelectionMenu import SelectionMenu
from EzInstaller.DownloadProcess import DownloadProcess

import os


SelMenu = SelectionMenu(
    f"{os.getcwd()}/InstallerScripts/index.csv", f"{os.getcwd()}/InstallerScripts")

while not SelMenu.hasStartDownload():
    SelMenu.start()

Downloader = DownloadProcess(
    SelMenu.getSelectedScripts(), f"{os.getcwd()}/InstallerScripts/ScriptRunner.sh")

Downloader.runScripts()
