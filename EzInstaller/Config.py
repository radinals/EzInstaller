from dataclasses import dataclass


@dataclass
class Config:
    program_name = "EzInstaller"
    theme_file = f"{program_name}/theme.rasi"
    download_script_folder = f"{program_name}/scripts"
    download_script_index_file = f"{download_script_folder}/index.csv"
    download_script_runner = f"{download_script_folder}/runner.sh"
