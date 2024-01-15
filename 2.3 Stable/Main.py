#LIBRERIAS
import customtkinter, os, minecraft_launcher_lib, subprocess, datetime, subprocess, tkinter, Saves, ast
from tkinter import messagebox
from PIL import Image

#OTROS
customtkinter.set_appearance_mode("dark")

#VALORES
user_windows = os.environ['USERNAME']
L_Version = "2.3 Stable"

#PERSONALIZAR
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.jakecherry" #GAME DIRRECTORY

#OTHERS
versiones = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
todas_las_versiones = [version.get('id', 'N/A') for version in versiones]

#GUARDADO DE CONFIGURACION
with open('Saves.py', 'r') as save:
    contenido_saves = save.read()

#AVISO
print(f"Fecha: {datetime.datetime.utcnow()}, ESTA ES LA CONSOLA DE DESARROLLADOR, SI LA CIERRAS, SE CIERRA EL JUEGO/LAUNCHER:\nPD: SI PUEDES VER ESTO ESTAS EN LA VERSION DE DESARROLLO/CODIGO ABIERTO (DESCOMPILADA):")

#INTERFAZ
class RoundedComboboxFrame(customtkinter.CTkFrame): #VAR VERSIONS
    def __init__(self, master=None, width=100, height=10, **kwargs):
        super().__init__(master, width=width, height=height, **kwargs)

class App(customtkinter.CTk): #APP

    #RESOLUCION
    width = 900
    height = 600

    #JV_ARGUMENTS RESTAURAR
    def restaurar_texto_predefinido(self, event):
        if not self.jv_entry.get().strip():
            self.jv_entry.delete(0, "end")
            self.jv_entry.insert(0, '["-Xmx1G", "-Xms1G"]')

    #GUARDAR CONFIGUACION
    def save_configuracion(self):
        jvmar = self.jv_entry.get()
        try:
            ram_ = ast.literal_eval(jvmar)
            Saves.ram = ram_
        except ValueError as e:
            self.inf_ung(e)

    #IRSE A CONFIGURACION
    def conf_frame_event(self):
        self.MAIN_frame.grid_forget()
        self.conf_frame.grid(row=0, column=0, sticky="ns")

    #SUGERENCIAS VERSIONES
    def actualizar_sugerencias(self, event):
        self.combobox_version['values'] = self.todas_las_versiones

    #IRSE AL MENU (FRAME)
    def men_event(self):
        self.conf_frame.grid_forget()
        self.ins_frame.grid_forget()
        self.MAIN_frame.grid(row=0, column=0, sticky="ns")
    
    #MENSAJE DE INFO
    def inf_ung(self, mensaje=None):
        messagebox.showinfo("Informe!", mensaje)

    #IRSE A INSTALACION (FRAME)
    def install_minecraft(self):
        version_inst = self.combobox_version.get()
        if not version_inst:
            self.inf_ung("Por favor, ingresa una versión de Minecraft.")
            self.men_event()
        elif not version_inst.isdigit():
            self.inf_ung("La versión ingresada debe contener solo números.")
            self.men_event()
        elif version_inst in todas_las_versiones:
            self.inf_ung(f"La versión {version_inst} ya está instalada.")
            self.men_event()
        else:
            try:
                self.inf_ung(f"Se está instalando la versión {version_inst}!")
                minecraft_launcher_lib.install.install_minecraft_version(version_inst, minecraft_directory)
                self.inf_ung(f"¡Se instaló correctamente la {version_inst}!")
                self.men_event()
            except Exception as e:
                self.inf_ung(f"¡Ha ocurrido un error!, asegurate de haber puesto bien la version!: {e}")
                return

    #INICIADOR
    def launch_event(self):
        mine_user = self.username_entry.get()
        mine_version = self.combobox_version.get()
        if not mine_version:
            self.inf_ung("Por favor, ingresa una versión de minecraft.")
            self.men_event()
        elif len(mine_user) < 4:
            self.inf_ung("El nombre de usuario debe tener al menos 4 caracteres.")
            self.men_event()
        elif not mine_user.isalnum():
            self.inf_ung("El nombre de usuario solo puede contener letras y números.")
            self.men_event()
        elif mine_user.isdigit():
            self.inf_ung("El nombre de usuario no puede consistir solo en números.")
            self.men_event()
        else:
            try:
                options = {
                    'username': mine_user,
                    'uuid': '',
                    'token': '',
                    'jvmArguments': Saves.ram
                }
                try:
                    if 'forge' in mine_version.lower() or 'fabric' in mine_version.lower():
                        self.inf_ung(f"Se esta iniciando minecraft {mine_version}!, porfavor, no cierre el launcher.")
                    else:
                        self.inf_ung(f"Se esta iniciando minecraft {mine_version}!, porfavor, no cierre el launcher.")
                        minecraft_launcher_lib.install.install_minecraft_version(mine_version, minecraft_directory)
                    minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(mine_version, minecraft_directory, options)
                    self.destroy()
                    subprocess.run(minecraft_command)
                except Exception as e:
                    self.inf_ung(f"¡Ha ocurrido un error!, asegurate de haber puesto bien la version o configuracion!: {e}")
                    self.men_event()
            except Exception as e:
                self.inf_ung(f"¡Ha ocurrido un error!, revisa tu configuracion!: {e}")
                self.men_event()

    #NUCLEO (INTERFAZ)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        #DATOS BASICOS
        self.title(f"Jakecherry Launcher {L_Version}")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)
        current_path_ = os.path.dirname(os.path.realpath(__file__))
        self.iconbitmap(os.path.join(current_path_, "images", "icon.ico"))

        #BG
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/images/bg.png"), size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        #MAIN FRAME
        self.MAIN_frame = customtkinter.CTkFrame(self, corner_radius=50)
        self.MAIN_frame.grid(row=0, column=0, sticky="ns")
        self.MAIN_label = customtkinter.CTkLabel(self.MAIN_frame, text="Jakecherry's Launcher", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.MAIN_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.username_entry = customtkinter.CTkEntry(self.MAIN_frame, width=200, placeholder_text="Usuario?")
        self.username_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        combobox_frame = RoundedComboboxFrame(self.MAIN_frame, width=210, height=31, corner_radius=10)
        combobox_frame.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.combobox_version = tkinter.ttk.Combobox(self.MAIN_frame, values=todas_las_versiones, width=30)
        self.combobox_version.set("Version?")
        self.combobox_version['values'] = todas_las_versiones
        self.combobox_version.bind('<KeyRelease>', self.actualizar_sugerencias)
        self.combobox_version.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.launch_button = customtkinter.CTkButton(self.MAIN_frame, text="Lanzar", command=self.launch_event, width=200, height=32)
        self.launch_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.install_button = customtkinter.CTkButton(self.MAIN_frame, text="Instalar", command=self.install_minecraft, width=200, height=32)
        self.install_button.grid(row=4, column=0, padx=30, pady=(15, 15))
        self.conf_button = customtkinter.CTkButton(self.MAIN_frame, text="Configuracion", command=self.conf_frame_event, width=200, height=32)
        self.conf_button.grid(row=5, column=0, padx=30, pady=(15, 15))
        labelimain = customtkinter.CTkLabel(self.MAIN_frame, text=f"Jakecherry's Launcher\nHecho por JakeDev098")
        labelimain.grid(row=9, column=0)

        #ICON
        image_path = os.path.join(current_path, "images", "logo.ico")
        bg_image = customtkinter.CTkImage(Image.open(image_path), size=(245, 254))
        image_label = customtkinter.CTkLabel(self.MAIN_frame, image=bg_image, text="")
        image_label.grid(row=0, column=0, sticky="nsew")

        #INSTALL MINECRAFT
        self.ins_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.ins_frame.grid_columnconfigure(0, weight=1)
        self.ins__label = customtkinter.CTkLabel(self.ins_frame, text="Jakecherry's\nInstalacion de minecraft", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.ins__label.grid(row=0, column=0, padx=30, pady=(30, 15))
        labelinst = customtkinter.CTkLabel(self.ins_frame, text="Se esta instalando la version de minecraft que pediste!, es normal que tarde.")
        labelinst.grid(row=4, column=0)
        self.back_button_ins = customtkinter.CTkButton(self.ins_frame, text="Back", command=self.men_event, width=200)
        self.back_button_ins.grid(row=9, column=0, padx=30, pady=(15, 15))

        #CONFIGURAR MINECRAFT
        self.conf_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.conf_frame.grid_columnconfigure(0, weight=1)
        self.conf__label = customtkinter.CTkLabel(self.conf_frame, text="Jakecherry's\nConfiguracion", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.conf__label.grid(row=0, column=0, padx=30, pady=(30, 15))
        labelconf_jv = customtkinter.CTkLabel(self.conf_frame, text="Argumentos JVM:")
        labelconf_jv.grid(row=1, column=0)
        jv_entry = customtkinter.CTkEntry(self.conf_frame, width=200, placeholder_text='["-Xmx1G", "-Xms1G"]')
        jv_entry.grid(row=2, column=0, padx=30, pady=(15, 15))
        jv_entry.bind('<FocusIn>', self.restaurar_texto_predefinido)
        self.jv_entry = jv_entry
        self.save_button_conf = customtkinter.CTkButton(self.conf_frame, text="Guardar", command=self.save_configuracion, width=200)
        self.save_button_conf.grid(row=8, column=0, padx=30, pady=(15, 15))
        self.back_button_conf = customtkinter.CTkButton(self.conf_frame, text="Back", command=self.men_event, width=200)
        self.back_button_conf.grid(row=9, column=0, padx=30, pady=(15, 15))

#RUN THE UI
if __name__ == "__main__":
    app = App()
    app.mainloop()