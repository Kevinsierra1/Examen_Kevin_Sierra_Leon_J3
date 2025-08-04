from utils import screenController as sc
import menus.agregar_ingredientes as ai
import menus.registro_y_gestion_categorias as rg
import menus.registro_y_gestion_chef as rgc
import menus.registro_y_gestion_hamburguesas as rgh
from config import AGREGAR
if __name__ == "__main__":
    sc.limpiarPantalla()
def main_menu():
    print("============================================")
    print("               Menu Principal  ")
    print("============================================")
    print("1.Registro y gestión de ingredientes ")
    print("2.Seguimiento del historial de ingredientes")
    print("3.Registro y gestión por categorias")
    print("4.Registro y gestión de chefs")
    print("5.Registro y gestion de hamburguesas ")
    print("6.Modulo de reportes ")
    print("7.Salir del programa")

def main():
    while True:
        main_menu()
        opcion = int(input("Selecciona una opcion (1-7): "))
        match opcion:
            case 1:
                ai.aniadir_ingredientes()
            case 2:
                pass
            case 3:
                rg.agregar_hamburguesa()
            case 4:
                rgc.agregar_chef()
            case 5:
                pass
            case 6: 
                pass
            case 7:
                respuesta = input("¿Está seguro que desea salir? (s/n): ")
                if respuesta.lower() == "s":
                    return
                else:
                    print("Regresando al menú principal...")
            case _:
             print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
      main()