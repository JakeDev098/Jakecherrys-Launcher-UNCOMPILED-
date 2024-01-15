
#LIBS
import subprocess, minecraft_launcher_lib, os

# SET VALUES
user_windows = os.environ['USERNAME']
minecraft_directory = f"C://Users//{user_windows}//AppData//Roaming//.jakecherry"
L_Version = "1.4 Stable"

#PATRIC DRAW
def draw():
    print("────────────────────██████──────────\n──────────────────██▓▓▓▓▓▓██────────\n────────────────██▓▓▓▓▒▒▒▒██────────\n────────────────██▓▓▒▒▒▒▒▒██────────\n──────────────██▓▓▓▓▒▒▒▒██──────────\n──────────────██▓▓▒▒▒▒▒▒██──────────\n────────────██▓▓▓▓▒▒▒▒▒▒██──────────\n────────────████▒▒████▒▒██──────────\n────────────██▓▓▒▒▒▒▒▒▒▒██──────────\n──────────██────▒▒────▒▒██──────────\n──────────████──▒▒██──▒▒██──────────\n──────────██────▒▒────▒▒██──────────\n──────────██▒▒▒▒▒▒▒▒▒▒▒▒██──────────\n──────────████████████▒▒▒▒██────────\n────────██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──────\n──────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██────\n────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██──\n──██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██\n██▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██\n██▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒██\n██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██\n──████▐▌▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▌▐▌████──\n────██▐▌▐▌▌▌▌▌▌▌▌▌▐▌▐▌▐▌▐▌▌▌▐▌██────\n────██▌▌▐▌▐▌▌▌▐▌▌▌▌▌▐▌▌▌▌▌▌▌▌▌██────\n──────██▌▌▐▌▐▌▐▌▐▌▐▌▐▌▐▌▌▌▌▌██──────\n──────██▐▌▐▌▐▌████████▐▌▌▌▌▌██──────\n────────██▒▒██────────██▒██────────\n────────██████────────██████────────\n")

#MORE INFO SECTION
def more_info():
    os.system('cls')
    print()
    print("Launcher desarrollado por JakeDev098 y JakobDev")
    print()
    print("Mas informacion:")
    print("Skins:")
    print(" Para poner skins necesitas el mod OfflineSkins para fabric")
    print("Errores:")
    print(" Error(@):")
    print("  La instalacion de tu version de minecraft esta corrupta o mal instalada")
    print(" Error(#)")
    print("  La version que buscas no existe o no esta disponible")
    print(" Error(~)")
    print("  has sido regresado al menu por algun error desconocido o has introducido algun dato incorrecto")
    backq = input("x para salir al menu: ")
    if backq == "x":
        os.system('cls')
        menu()
    else:
        pass

#INSTALL A VERSION OF MINECRAFT
def install_minecraft():
    os.system('cls')
    try:
        print("NO SE ACEPTAN SNAPSHOTS")
        minecraft_version = input('Version: ')
        print(f"Por favor espere mientras se instala la {minecraft_version}")
        minecraft_launcher_lib.install.install_minecraft_version(minecraft_version, minecraft_directory)
        print(f'La {minecraft_version} ha sido instalada con exito')
        menu()
    except:
        print("Custom-code: Error(#)")
        menu()

#OPEN MINECRAFT
def open_minecraft():
    os.system('cls')
    versions = minecraft_launcher_lib.utils.get_installed_versions(minecraft_directory)
    print("Versiones instaladas:")
    for version in versions:
        print(f"ID: {version['id']}, de tipo: {version['type']}")

    mine_version = input('Ingrese el ID de la versión que desea jugar: ')
    mine_user = input('Nombre de usuario: ')
    print("CONSOLA DE DESARROLLADOR:")
    print()

    options = {
        'username': mine_user,
        'uuid': '',
        'token': '',
        'jvmArguments': ["-Xmx1G", "-Xms1G"]
    }

    try:
        if 'forge' in mine_version.lower() or 'fabric' in mine_version.lower():
            # No es necesario reinstalar Fabric o Forge cada vez
            print(f"Iniciando Minecraft {mine_version}")
        else:
            # Instalar la versión de Minecraft si no es Fabric ni Forge
            print(f"Por favor espere mientras se instala la {mine_version}")
            minecraft_launcher_lib.install.install_minecraft_version(mine_version, minecraft_directory)

        minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(mine_version, minecraft_directory, options)
        subprocess.run(minecraft_command)
    except Exception as e:
        os.system('cls')
        print(f"Custom-code: Error({e})")
        menu()


#MENU
def menu():
    print()
    draw()
    print(f'Jakecherry Launcher Version: {L_Version}\n▐ Instalar Minecraft (0)\n▐ Ejecutar Minecraft (1)\n▐ Mas informacion (2)')
    formulario = input('Dime que deseas: ')
    if formulario == "0":
        install_minecraft()
    if formulario == "1":
        open_minecraft()
    if formulario == "2":
        more_info()
    else:
        os.system('cls')
        print("Custom-code: Error(~)")
        menu()

#OPEN THE MENU
menu()
