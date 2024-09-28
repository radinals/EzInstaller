from RunPromptWrapper.RunPromptWrapper import RunPromptWrapper
from RunPromptWrapper.MenuEntry import MenuEntry
from .SpecialButtons import DownloadBtn, ExitBtn

import csv


class DownloaderScriptEntry(MenuEntry):
    def __init__(self, label, description, script_path):
        super().__init__(label)
        self.selected = False
        self.checklist = "[ ]"
        self.desc = description
        self.script_path = script_path

    def onSelected(self):
        if (self.selected):
            self.checklist = "[ ]"
            self.selected = False
        else:
            self.checklist = "[X]"
            self.selected = True

    def getLabel(self):
        return f"{self.label} ({self.desc}) {self.checklist}"


class SelectionMenu(RunPromptWrapper):
    def __init__(self, script_index_csv_path, script_path):
        super().__init__("rofi -dmenu -no-sort")
        self.selected_scripts = []
        self.script_index_csv_path = script_index_csv_path
        self.script_path = script_path
        self.start_download = False
        self.generateMenuEntries()

    def hasStartDownload(self):
        return self.start_download

    def onMenuEntrySelected(self, menu_entry: MenuEntry):
        if type(menu_entry) is DownloadBtn:
            for entry in self.menu_entries:
                if type(entry) is DownloaderScriptEntry and entry.selected:
                    self.selected_scripts.append(entry.script_path)

            self.start_download = True

        else:
            return super().onMenuEntrySelected(menu_entry)

    def generateMenuEntries(self):

        self.addMenuEntry(ExitBtn())
        self.addMenuEntry(DownloadBtn())

        with open(self.script_index_csv_path, mode="r") as f:
            csvfile = csv.reader(f)
            for lines in csvfile:
                label = lines[0]
                desc = lines[1]
                script = f"{self.script_path}/{lines[2]}"
                self.addMenuEntry(
                    DownloaderScriptEntry(label, desc, script))

    def getSelectedScripts(self):
        return self.selected_scripts
