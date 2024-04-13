import customtkinter as ctk

from filemanager import fileManager
from tkinter import messagebox, StringVar


# CTK Config
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class EssentialInstallerGUI:
    def __init__(self):
        # Get the users directory
        self.curdir = fileManager().cur_path

        # Get the paths for the fabric mods, forge mods, and curseforge modpacks
        self.fabric = fileManager().fabric_files
        self.forge = fileManager().forge_files
        self.curseforge = fileManager().curseforge_modpacks
        self.curseforge_modpack_names = fileManager().curseforge_modpack_names

        self.fabric, self.forge, self.curseforge = reversed(self.fabric), sorted(self.forge), sorted(self.curseforge_modpack_names)

        # Other variables
        self.cur_pack = []
        self.cur_mod = []

        # Run the GUI
        self.installer_gui()


    def install(self):
        fabric_pack = ""
        forge_pack = ""
        curseforge_pack = ""

        if len(self.cur_pack) == 0:
            messagebox.showerror("Error", "Please select a pack to install.")
            return
        
        if len(self.cur_mod) == 0:
            messagebox.showerror("Error", "Please select a mod to install the pack to.")
            return
        
        if "fabric" in self.cur_pack[0]:
            fabric_pack = f"{self.curdir}/essentialpacks/fabric/{self.cur_pack[0]}"
        elif "forge" in self.cur_pack[0]:
            forge_pack = f"{self.curdir}/essentialpacks/forge/{self.cur_pack[0]}"
        else:
            messagebox.showerror("Error", "Please select a pack to install.")
            return

        curseforge_pack = f"{fileManager().curseforge_packs_path}{self.cur_mod[0]}/mods/"

        if (fabric_pack and curseforge_pack):
            fileManager().copy_files(fabric_pack, curseforge_pack)
            messagebox.showinfo("Success", f"Successfully installed {self.cur_pack[0]} to {self.cur_mod[0]}")
        elif (forge_pack and curseforge_pack):
            fileManager().copy_files(forge_pack, curseforge_pack)
            messagebox.showinfo("Success", f"Successfully installed {self.cur_pack[0]} to {self.cur_mod[0]}")
        else:
            messagebox.showerror("Error", "Please select a pack and mod to install.")

    
    def chosen_essential_path(self, pack_name):
        self.cur_pack = [pack_name]

   
    def chosen_curseforge_path(self, pack_name):
        self.cur_mod = [pack_name]


    def installer_gui(self):
        # Main window
        self.window = ctk.CTk()
        self.window.title("Essential Installer")
        self.window.geometry("310x300")
        self.window.resizable(False, False)

        # Radio Button Variable
        self.radiovar = StringVar()

        # GUI Frames
        self.path_frames = ctk.CTkFrame(master=self.window)
        self.path_frames.grid(row=0, column=0)
        self.path_frames.propagate(False)

        # Tabview
        self.fabric_or_forge_tabview = ctk.CTkTabview(self.path_frames, width=300)
        self.fabric_or_forge_tabview.grid(row=0, column=0)
        self.fabric_or_forge_tabview.add("fabric")
        self.fabric_or_forge_tabview.add("forge")
        self.fabric_or_forge_tabview.add("modpack")

        # Tabview configuration 
        self.fabric_or_forge_tabview.tab("fabric").grid_columnconfigure(0, weight=1)
        self.fabric_or_forge_tabview.tab("fabric").grid_rowconfigure(0, weight=1)
        self.fabric_or_forge_tabview.tab("forge").grid_columnconfigure(0, weight=1)
        self.fabric_or_forge_tabview.tab("forge").grid_rowconfigure(0, weight=1)
        self.fabric_or_forge_tabview.tab("modpack").grid_columnconfigure(0, weight=1)
        self.fabric_or_forge_tabview.tab("modpack").grid_rowconfigure(0, weight=1)

        # Radio Buttons
        self.fabric_listbox = ctk.CTkScrollableFrame(self.fabric_or_forge_tabview.tab("fabric"), width=270)
        self.fabric_listbox.grid(row=0, column=0)

        for i in self.fabric:
            i = i.split("/")[-1]
            ctk.CTkRadioButton(self.fabric_listbox, text=i, variable=self.radiovar, value=i, command=lambda: self.chosen_essential_path(self.radiovar.get()), width=800/4).pack()

        self.forge_listbox = ctk.CTkScrollableFrame(self.fabric_or_forge_tabview.tab("forge"), width=270)
        self.forge_listbox.grid(row=0, column=0)

        for i in self.forge:
            i = i.split("/")[-1]
            ctk.CTkRadioButton(self.forge_listbox, text=i, variable=self.radiovar, value=i, command=lambda: self.chosen_essential_path(self.radiovar.get()), width=800/4).pack()
            

        self.modpack_listbox = ctk.CTkScrollableFrame(self.fabric_or_forge_tabview.tab("modpack"), width=270)
        self.modpack_listbox.grid(row=0, column=0)

        for i in self.curseforge:
            ctk.CTkRadioButton(self.modpack_listbox, text=i, variable=self.radiovar, value=i, command=lambda: self.chosen_curseforge_path(self.radiovar.get()), width=800/4).pack()


        # Install Button
        self.install_button = ctk.CTkButton(master=self.window, width=300, height=30, text="Install", font=("Arial", 20), command=self.install)
        self.install_button.grid(row=1, column=0, pady=(5, 0))


        # Run the GUI
        self.window.mainloop()


    
if __name__ == "__main__":
    EssentialInstallerGUI()


