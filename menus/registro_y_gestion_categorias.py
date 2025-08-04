import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf

def agregar_hamburguesa():
    while True:
        print("===================================")
        print("        Tipo de hamburguesa        ")
        print("1.Asignele un nombre a su Hamburguesa")
        print("2.Asignele una descripción")
        print("3.Volver al menu Principal")
        print("===================================")

        opcion_sub = input("Seleccione una opcion (1-3): ")
        opcion_sub = int(opcion_sub)

        match opcion_sub:
            case 1: 
                print(">>>Agregando Hamburguesa...")
                tipoHam = vd.validatatext("Ingrese el nombre de la Hamburguesa: ")
                descripHam = vd.validatatext("Ingrese una descripción: ")
                hamburguesa =[
                    {
                        "Name": tipoHam,
                        "Descripción": descripHam
                    }

                ]

                if not cf.updateJson({tipoHam: hamburguesa},"HAMBURGUESA"):
                    print("Hamburguesa agregada correctamente ✅")
                else:
                    print("No se pudo agregar la Hamburguesa ❌")
                sc.pausar_pantalla()