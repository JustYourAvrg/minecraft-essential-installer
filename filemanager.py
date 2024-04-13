import os
import shutil

from getpass import getuser


class fileManager:
    def __init__(self):
        self.curseforge_packs_path = f"C:/Users/{getuser()}/curseforge/minecraft/Instances/"
        self.cur_path = os.getcwd()

        self.fabric_files = []
        self.forge_files = []
        self.curseforge_modpacks = []
        self.curseforge_modpack_names = []


        self.get_files(f"{self.cur_path}/essentialpacks/fabric")
        self.get_files(f"{self.cur_path}/essentialpacks/forge")
        self.get_curseforge_mod_path(f"{self.curseforge_packs_path}")

    
    def get_files(self, path):
        files = os.listdir(path)
        for file_name in files:
            if "fabric" in file_name:
                self.fabric_files.append(f"{path}/{file_name}")
            
            else:
                self.forge_files.append(f"{path}/{file_name}")

    
    def get_curseforge_mod_path(self, path):
        for folder_name in os.listdir(path):
            self.curseforge_modpacks.append(f"{path}{folder_name}/mods/")
            self.curseforge_modpack_names.append(folder_name)
    

    def copy_files(self, source, destination):
        source = source.replace("\\", "/")
        destination = destination.replace("\\", "/")

        shutil.copy(source, destination)


if __name__ == "__main__":
    fileManager()