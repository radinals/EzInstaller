from RunPromptWrapper.RunPromptWrapper import RunPromptWrapper
from RunPromptWrapper.MenuEntry import MenuEntry
from .SpecialButtons import DownloadBtn, ExitBtn

import csv

import subprocess


class DownloaderScriptEntry(MenuEntry):
    def __init__(self, label, description, script_path, index=0):
        super().__init__(label)
        self.selected = False
        self.checklist = "[ ]"
        self.desc = description
        self.script_path = script_path
        self.index = index

    def onSelected(self):
        if (self.selected):
            self.checklist = "[ ]"
            self.selected = False
        else:
            self.checklist = "[✔️]"
            self.selected = True

    def getLabel(self):
        return f"{self.label} ({self.desc}) {self.checklist}"


class SelectionMenu(RunPromptWrapper):
    def __init__(self, run_prompt_cmd, script_index_csv_path, script_path):
        super().__init__(run_prompt_cmd)
        self.selected_scripts = []
        self.script_index_csv_path = script_index_csv_path
        self.script_path = script_path
        self.start_download = False
        self.last_sel_row = 0
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
            # TODO: Magic Number '2'
            if type(menu_entry) is DownloaderScriptEntry:
                self.last_sel_row = abs(
                    (len(self.menu_entries) - 2) - menu_entry.index)
            return super().onMenuEntrySelected(menu_entry)

    def _execMenuCmd(self):
        return subprocess.run(self.run_prompt_cmd + f" -selected-row {self.last_sel_row}",
                              input=self._generateExecStr(),
                              text=True,
                              shell=True,
                              capture_output=True)

    def _captureEvent(self, exit_string):
        if (exit_string):
            menu_entry = self._getMenuEntry(
                str(exit_string.stdout).strip("\n"))
            if (menu_entry != None):
                self.onMenuEntrySelected(menu_entry)
            else:
                exit()

    def generateMenuEntries(self):

        self.addMenuEntry(ExitBtn())
        self.addMenuEntry(DownloadBtn())

        with open(self.script_index_csv_path, mode="r") as f:
            csvfile = csv.reader(f)
            i = 1
            for lines in csvfile:
                label = lines[0]
                desc = lines[1]
                script = f"{self.script_path}/{lines[2]}"
                self.addMenuEntry(
                    DownloaderScriptEntry(label, desc, script, i))
                i += 1

    def getSelectedScripts(self):
        return self.selected_scripts
