
#LIBRERIAS
import customtkinter, os, minecraft_launcher_lib, subprocess
from tkinter import messagebox
from PIL import Image

#OTROS
customtkinter.set_appearance_mode("dark")

# SET VALUES
user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.jakecherry"
L_Version = "2.0 Stable"
ready_versions = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
tesxinst = "Se esta instalando la version de minecraft que pediste!, es normal que tarde."

#INTERFAZ
class App(customtkinter.CTk):

    #RESOLUCION
    width = 900
    height = 600

    #IRSE AL MENU
    def men_event(self):
        self.ins_frame.grid_forget()
        self.MAIN_frame.grid(row=0, column=0, sticky="ns")

    #IRSE A INSTALACION
    def ins_event(self):
        self.MAIN_frame.grid_forget()
        self.ins_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    #MENSAJE DE INFORMACION
    def inf_ung(self, mensaje):
        messagebox.showinfo("Informe!", mensaje)

    #INSTALACION
    def install_minecraft(self):
        self.ins_event()
        version_inst = self.version_entry.get()
        if not version_inst:
            self.inf_ung("Por favor, ingresa una versión de Minecraft.")
            self.men_event()
        else:
            try:
                self.inf_ung(f"Se está instalando la versión {version_inst}!")
                minecraft_launcher_lib.install.install_minecraft_version(version_inst, minecraft_directory)
                self.inf_ung(f"¡Se instaló correctamente la {version_inst}!")
                self.men_event()
            except Exception as e:
                self.inf_ung(f"¡Ha ocurrido un error! Detalles: {e}")
                self.men_event()
            
    #INICIADOR
    def launch_event(self):
        mine_user = self.username_entry.get()
        mine_version = self.version_entry.get()
        if not mine_version:
            self.inf_ung("Por favor, ingresa una versión de minecraft.")
            self.men_event()
        if not mine_user:
            self.inf_ung("Por favor, ingresa un nombre de usuario.")
            self.men_event()
        else:
            options = {
                'username': mine_user,
                'uuid': '',
                'token': '',
                'jvmArguments': ["-Xmx1G", "-Xms1G"]  # ATRIBUTOS DE JAVA
            }
            try:
                if 'forge' in mine_version.lower() or 'fabric' in mine_version.lower():
                   self.inf_ung(f"Se esta iniciando minecraft {mine_version}!, porfavor, no cierre el launcher.")
                else:
                    self.inf_ung(f"Se esta iniciando minecraft {mine_version}!, porfavor, no cierre el launcher.")
                    minecraft_launcher_lib.install.install_minecraft_version(mine_version, minecraft_directory)
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(mine_version, minecraft_directory, options)
                subprocess.run(minecraft_command)
            except Exception as e:
                os.system('cls')
                print(f"Custom-code: Error({e})")

    #NUCLEO (INTERFAZ)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #DATOS BASICOS
        self.title(f"Jakecherry Launcher {L_Version}")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        current_pato = os.path.dirname(os.path.realpath(__file__))
        self.iconbitmap(os.path.join(current_pato, "images", "ico.ico"))

        #BG
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/images/bg.png"), size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        #MAIN FRAME
        self.MAIN_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.MAIN_frame.grid(row=0, column=0, sticky="ns")
        self.MAIN_label = customtkinter.CTkLabel(self.MAIN_frame, text="Jakecherry's Launcher", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.MAIN_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.MAIN_frame, width=200, placeholder_text="Tu nombre de usuario?")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.version_entry = customtkinter.CTkEntry(self.MAIN_frame, width=200, placeholder_text="La version de minecraft?")
        self.version_entry.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.install_button = customtkinter.CTkButton(self.MAIN_frame, text="Lanzar", command=self.launch_event, width=200)
        self.install_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.launch_button = customtkinter.CTkButton(self.MAIN_frame, text="Instalar", command=self.install_minecraft, width=200)
        self.launch_button.grid(row=4, column=0, padx=30, pady=(15, 15))
        labelimain = customtkinter.CTkLabel(self.MAIN_frame, text=f"Jakecherry's Launcher\nVersion: {L_Version}")
        labelimain.grid(row=9, column=0)

        #ICON
        image_path = os.path.join(current_path, "images", "ico.ico") #UBICA LA IMAGEN
        bg_image = customtkinter.CTkImage(Image.open(image_path), size=(245, 254))
        image_label = customtkinter.CTkLabel(self.MAIN_frame, image=bg_image, text="")
        image_label.grid(row=0, column=0, sticky="nsew")

        #INSTALL MINECRAFT
        self.ins_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.ins_frame.grid_columnconfigure(0, weight=1)
        self.ins__label = customtkinter.CTkLabel(self.ins_frame, text="Jakecherry's\nInstalacion de minecraft", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.ins__label.grid(row=0, column=0, padx=30, pady=(30, 15))
        labelinst = customtkinter.CTkLabel(self.ins_frame, text=tesxinst)
        labelinst.grid(row=4, column=0)
        self.back_button = customtkinter.CTkButton(self.ins_frame, text="Back", command=self.men_event, width=200)
        self.back_button.grid(row=1, column=0, padx=30, pady=(15, 15))

        #INSTALACION
        def install_minecraft(self):
            self.login_frame.grid_forget()
            self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)
            version_inst = self.version_entry.get()
            try:
                print(f"Se está instalando la versión {version_inst}")
                minecraft_launcher_lib.install.install_minecraft_version(version_inst, minecraft_directory)
                print("¡Se instaló correctamente!")
            except Exception as e:
                print("¡Ha ocurrido un error! Asegúrate de tener conexión a Internet o haber escrito correctamente la versión.")
                print(f"Detalles del error: {e}")
            
        #INICIADOR
        def launch_event(self):
            mine_version = self.username_entry.get()
            options = {
                'username': mine_version,
                'uuid': '',
                'token': '',
                'jvmArguments': ["-Xmx1G", "-Xms1G"]  # ATRIBUTOS DE JAVA
            }
            try:
                if 'forge' in mine_version.lower() or 'fabric' in mine_version.lower():
                   print(f"Iniciando Minecraft {mine_version}")
                else:
                    print(f"Por favor, espere mientras se instala la {mine_version}")
                    minecraft_launcher_lib.install.install_minecraft_version(mine_version, minecraft_directory)
                minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(mine_version, minecraft_directory, options)
                subprocess.run(minecraft_command)
            except Exception as e:
                os.system('cls')
                print(f"Custom-code: Error({e})")

        #IR A ATRAS
        def back_event(self):
            self.main_frame.grid_forget()
            self.login_frame.grid(row=0, column=0, sticky="ns")

#COMPROBACION
if __name__ == "__main__":
    app = App()
    app.mainloop()
