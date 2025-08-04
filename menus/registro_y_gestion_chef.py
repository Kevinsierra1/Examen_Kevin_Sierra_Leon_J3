import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf

def agregar_chef():
    while True:
        print("====================================")
        print("         Menu chefs        ")
        print("1. Añadir Chef ")
        print("2. Volver al menu principal")
        print("====================================")

        opciones_sub = input("Selecccione una opción (1-2): ")
        opciones_sub = int(opciones_sub)

        match opciones_sub:
            case 1:
                print(">>>Añadiendo Chef...")
                nomChef = vd.validatatext("Ingrese el nombre del chef: ")
                especialidadChef = vd.validatatext("Ingrese la especialidad del chef: ")
                chef = [
                    {
                        "Name":nomChef,
                        "Especialidad":especialidadChef
                    }
                ]

                if not cf.updateJson({nomChef:[]}, ["CHEF"]):
                    print("Chef agregado exitosamente ✅")
                else:
                    print("No se pudo agregar al chef ❌")
                sc.pausar_pantalla()
            case 2:
                print('Seguro de que desea volver al menú principal? (S/N)')
                respuesta = input().strip().lower()
                if respuesta == 's':
                    return
                elif respuesta == 'n':
                    continue
                else:
                    print('Opción no válida. Regresando al menú principal.')
                    return
            case _:
                print("Opción no válida, por favor intente de nuevo.")
                sc.pausar_pantalla()
                continue