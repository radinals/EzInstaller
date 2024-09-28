from RunPromptWrapper.MenuEntry import MenuEntry


class ExitBtn(MenuEntry):
    def __init__(self):
        super().__init__("Exit")

    def onSelected(self):
        return exit()


class DownloadBtn(MenuEntry):
    def __init__(self):
        super().__init__("StartDownload")
