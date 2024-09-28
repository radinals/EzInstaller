import subprocess


class DownloadProcess:
    def __init__(self, download_script_list, script_runner_path):
        self.download_script_list = download_script_list
        self.script_runner_path = script_runner_path

    def runScripts(self):
        subprocess.run(self.generateDownloadCommand(), text=True, shell=True)

    def generateDownloadCommand(self):
        return f"{self.getTerminal()} -e bash -c  \"{self.script_runner_path} {" ".join(self.download_script_list)}\""

    def getTerminal(self):
        return "xterm -hold"
