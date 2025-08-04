import utils.screenController as sc
import utils.validateData as vd
import utils.corefiles as cf

def aniadir_ingredientes():
     while True:
        print("\n======Submenú: Añadir Nuevo Elemento =======")
        print("1. Agregar ingredientes")
        print("2. Ver ingredientes")
        print("3. Actualizar ingredientes")
        print("4. Eliminar ingredientes")
        print("6. Volver al menu principal")
        print("==============================================")

        opcion_sub = input("Seleccione una opcion (1-4): ")
        opcion_sub = int(opcion_sub)

        match opcion_sub:
            case 1:
                print("\n>>> Añadiendo tipo de Pan...")
                tipoPan = vd.validatatext("Ingrese el tipo de Pan: ")
                descripPan = vd.validatatext("Ingrese una descripción: ")
                precioPan = vd.validateflot("Ingrese el precio: ")
                stockPan = vd.validateflot("Ingrese El stock: ")
                stockPan = float(stockPan)
                pan ={
                    {
                    "Name": tipoPan,
                    "aut": descripPan,
                    "genero": precioPan,
                    "valora": stockPan,
                    }
                }
                
                if not cf.updateJson({tipoPan: pan}, ["PAN"]):
                    print("Tipo de pan agregado correctamente ✅")
                else:
                    print("No se pudo agregar el tipo de pan ❌ ")
                sc.pausar_pantalla()

                print("\n>>> Añadiendo tipo de Carne...")
                tipoCarne = vd.validatatext("Ingrese el tipo de Carne: ")
                descripCarne = vd.validatatext("Ingrese una descripción: ")
                precioCarne = vd.validateflot("Ingrese el precio: ")
                stockCarne = vd.validateflot("Ingrese El stock: ")
                stockCarne = float(stockCarne)
                carne ={
                    {
                    "Name": tipoCarne,
                    "aut": descripCarne,
                    "genero": precioCarne,
                    "valora": stockCarne,
                    }
                }
                
                if not cf.updateJson({tipoCarne: carne}, ["CARNE"]):
                    print("Tipo de carne agregada correctamente ✅")
                else:
                    print("No se pudo agregar el tipo de carne ❌ ")
                sc.pausar_pantalla()

                print("\n>>> Añadiendo tipo de Queso...")
                tipoQueso = vd.validatatext("Ingrese el tipo de Queso: ")
                descripQueso = vd.validatatext("Ingrese una descripción: ")
                precioQueso = vd.validateflot("Ingrese el precio: ")
                stockQueso = vd.validateflot("Ingrese El stock: ")
                stockQueso = float(stockPan)
                queso ={
                    {
                    "Name": tipoQueso,
                    "aut": descripQueso,
                    "genero": precioQueso,
                    "valora": stockQueso,
                    }
                }
                
                if not cf.updateJson({tipoQueso: queso}, ["QUESO"]):
                    print("Tipo de queso agregado correctamente ✅")
                else:
                    print("No se pudo agregar el tipo de queso ❌ ")
                sc.pausar_pantalla()

                print("\n>>> Añadiendo vegetales...")
                tipoVeg = vd.validatatext("Ingrese el vegetal que desea: ")
                descripVeg = vd.validatatext("Ingrese una descripción: ")
                precioVeg = vd.validateflot("Ingrese el precio: ")
                stockVeg = vd.validateflot("Ingrese El stock: ")
                stockVeg = float(stockVeg)
                vegetales = {
                    {
                    "Name": tipoVeg,
                    "aut": descripVeg,
                    "genero": precioVeg,
                    "valora": stockVeg,
                }
                }
                
                if not cf.updateJson({tipoVeg: vegetales}, ["VEGETALES"]):
                    print("Vegetal agregado correctamente ✅")
                else:
                    print("No se pudo agregar el tipo de Vegetal ❌ ")
                    sc.pausar_pantalla()
                print("Desea seguir agregando vegetales (S/N)")
                respuesta = input().strip().lower()
                if respuesta == 's':
                    return 
                elif respuesta == 'n':
                    continue
                else:
                    print('Opción no válida. Regresando al menú principal.')
                    return
            case 2:
                ingredientes = cf.readJson()
                if not ingredientes:
                    print("No hay ingredientes.")
                    return
                categorias = list(ingredientes.keys())
                print("\n===Menu de categorias===")
                for idx, categoria in enumerate(categorias, 1):
                    print(f"{idx}. {categoria}")
                print(f"{len(categorias)+1}. Volver al menú principal")
                try:
                    opcion = int(input("Seleccione una categoría: "))
                    if opcion == len(categorias) + 1:
                        return
                    if opcion < 1 or opcion > len(categorias):
                        print("Opción no válida.")
                        sc.pausar_pantalla()
                        return
                except ValueError:
                    print("Entrada no valida.")
                    sc.pausar_pantalla()
                    return
                
                categoria = categorias[opcion - 1]
                items = ingredientes.get(categoria, {})
                print(f"\n===Elementos en la categoria {categoria}===")
                for nombre, detalles in items.items():
                    print(f"Nombre: {nombre}")
                    for clave, valor in detalles.items():
                        print(f"{clave.capitalize()}: {valor}")
                        print("---------------------------")
                sc.pausar_pantalla()
                   