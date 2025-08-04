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
                    
                    "Name": tipoPan,
                    "aut": descripPan,
                    "genero": precioPan,
                    "valora": stockPan,
            
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
                
                    "Name": tipoCarne,
                    "aut": descripCarne,
                    "genero": precioCarne,
                    "valora": stockCarne,
                    
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
                    
                    "Name": tipoQueso,
                    "aut": descripQueso,
                    "genero": precioQueso,
                    "valora": stockQueso,
                
                }
                
                if not cf.updateJson({tipoQueso: queso}, ["QUESO"]):
                    print("Tipo de queso agregado correctamente ✅")
                else:
                    print("No se pudo agregar el tipo de queso ❌ ")
                sc.pausar_pantalla()

                print(">>>Añadiendo salsas...")
                tipoSalsa = vd.validatatext("Ingrese el tipo de Salsa: ")
                descripSalsa = vd.validatatext("Ingrese una descripción: ")
                precioSalsa = vd.validateflot("Ingrese el precio: ")
                stockSalsa = vd.validateflot("Ingrese El stock: ")
                stockSalsa = float(stockSalsa)
                salsa ={ 
                    
                    "Name": tipoSalsa,
                    "aut": descripSalsa,
                    "genero": precioSalsa,
                    "valora": stockSalsa,
                
                }
                if not cf.updateJson({tipoSalsa: salsa}, ["SALSA"]):
                    print("Salsa agregada correctamente ✅")
                else:
                    print("No se pudo agregar el tipo de Salsa ❌ ")
                sc.pausar_pantalla()

                print("\n>>> Añadiendo vegetales...")
                tipoVeg = vd.validatatext("Ingrese el vegetal que desea: ")
                descripVeg = vd.validatatext("Ingrese una descripción: ")
                precioVeg = vd.validateflot("Ingrese el precio: ")
                stockVeg = vd.validateflot("Ingrese El stock: ")
                stockVeg = float(stockVeg)
                vegetales = {
                    
                    "Name": tipoVeg,
                    "aut": descripVeg,
                    "genero": precioVeg,
                    "valora": stockVeg,
                
                }
                
                if not cf.updateJson({tipoVeg: vegetales}, ["VEGETALES"]):
                    print("Vegetal agregado correctamente ✅")
                else:
                    print("No se pudo agregar el tipo de Vegetal ❌ ")
                    sc.pausar_pantalla()
                print("Desea seguir agregando vegetales (S/N)")
                respuesta = input().strip().lower()
                if respuesta == 's':
                    continue
                elif respuesta == 'n':
                    return
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
            case 3:
                while True:
                    print("\n===Actualizar Ingredientes===")
                    print("1. Actualizar Pan")
                    print("2. Actualizar Carne")
                    print("3. Actualizar Queso")
                    print("4. Actualizar Salsa")
                    print("5. Actualizar Vegetales")
                    print("6. Volver al menú principal")
                    opcion_actualizar = input("Seleccione una opción (1-6): ")
                    opcion_actualizar = int(opcion_actualizar)  

                    match opcion_actualizar:
                        case 1:
                            print(">>>Actualizando tipo de Pan...")
                            tipoPan = vd.validatatext("Ingrese el tipo de Pan a actualizar: ")
                            if cf.updateJson(tipoPan, ["PAN"]):
                                print(f"Tipo de Pan '{tipoPan}' actualizado correctamente ✅")
                            else:
                                print(f"No se pudo actualizar el tipo de Pan '{tipoPan}' ❌")
                            sc.pausar_pantalla()
                        case 2:
                            print(">>>Actualizando tipo de Carne...")
                            tipoCarne = vd.validatatext("Ingrese el tipo de Carne a actualizar: ")
                            if cf.updateJson(tipoCarne, ["CARNE"]):
                                print(f"Tipo de Carne '{tipoCarne}' actualizado correctamente ✅")
                            else:      
                                print(f"No se pudo actualizar el tipo de Carne '{tipoCarne}' ❌")
                            sc.pausar_pantalla()
                        case 3:
                            print(">>>Actualizando tipo de Queso...")
                            tipoQueso = vd.validatatext("Ingrese el tipo de Queso a actualizar: ")
                            if cf.updateJson(tipoQueso, ["QUESO"]):
                                print(f"Tipo de Queso '{tipoQueso}' actualizado correctamente ✅")
                            else:
                                print(f"No se pudo actualizar el tipo de Queso '{tipoQueso}' ❌")
                            sc.pausar_pantalla()
                        case 4:
                            print(">>>Actualizando tipo de Salsa...")
                            tipoSalsa = vd.validatatext("Ingrese el tipo de Salsa a actualizar: ")
                            if cf.updateJson(tipoSalsa, ["SALSA"]):
                                print(f"Tipo de Salsa '{tipoSalsa}' actualizado correctamente ✅")
                            else:
                                print(f"No se pudo actualizar el tipo de Salsa '{tipoSalsa}' ❌")
                            sc.pausar_pantalla()
                        case 5:
                            print(">>>Actualizando Vegetales...")
                            tipoVeg = vd.validatatext("Ingrese el vegetal a actualizar: ")
                            if cf.updateJson(tipoVeg, ["VEGETALES"]):
                                print(f"Vegetal '{tipoVeg}' actualizado correctamente ✅")
                            else:
                                print(f"No se pudo actualizar el vegetal '{tipoVeg}' ❌")
                            sc.pausar_pantalla()
                        case 6:
                            print("Seguro de que desea volver al menú principal? (S/N)")
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
            case 4:
                while True:
                    print("\n===Eliminar Ingredientes===")
                    print("1. Eliminar Pan")
                    print("2. Eliminar Carne")
                    print("3. Eliminar Queso")
                    print("4. Eliminar Salsa")
                    print("5. Eliminar Vegetales")
                    print("6. Volver al menú principal")
                    opcion_eliminar = input("Seleccione una opción (1-6): ")
                    opcion_eliminar = int(opcion_eliminar)  

                    match opcion_eliminar:
                        case 1:
                            print(">>>Eliminando tipo de Pan...")
                            tipoPan = vd.validatatext("Ingrese el tipo de Pan a eliminar: ")
                            if cf.deleteJson(tipoPan, ["PAN"]):
                                print(f"Tipo de Pan '{tipoPan}' eliminado correctamente ✅")
                            else:
                                print(f"No se pudo eliminar el tipo de Pan '{tipoPan}' ❌")
                            sc.pausar_pantalla()
                        case 2:
                            print(">>>Eliminando tipo de Carne...")
                            tipoCarne = vd.validatatext("Ingrese el tipo de Carne a eliminar: ")
                            if cf.deleteJson(tipoCarne, ["CARNE"]):
                                print(f"Tipo de Carne '{tipoCarne}' eliminado correctamente ✅")
                            else:      
                                print(f"No se pudo eliminar el tipo de Carne '{tipoCarne}' ❌")
                            sc.pausar_pantalla()
                        case 3:
                            print(">>>Eliminando tipo de Queso...")
                            tipoQueso = vd.validatatext("Ingrese el tipo de Queso a eliminar: ")
                            if cf.deleteJson(tipoQueso, ["QUESO"]):
                                print(f"Tipo de Queso '{tipoQueso}' eliminado correctamente ✅")
                            else:
                                print(f"No se pudo eliminar el tipo de Queso '{tipoQueso}' ❌")
                            sc.pausar_pantalla()
                        case 4:
                            print(">>>Eliminando tipo de Salsa...")
                            tipoSalsa = vd.validatatext("Ingrese el tipo de Salsa a eliminar: ")
                            if cf.deleteJson(tipoSalsa, ["SALSA"]):
                                print(f"Tipo de Salsa '{tipoSalsa}' eliminado correctamente ✅")
                            else:
                                print(f"No se pudo eliminar el tipo de Salsa '{tipoSalsa}' ❌")
                            sc.pausar_pantalla()
                        case 5:
                            print(">>>Eliminando Vegetales...")
                            tipoVeg = vd.validatatext("Ingrese el vegetal a eliminar: ")
                            if cf.deleteJson(tipoVeg, ["VEGETALES"]):
                                print(f"Vegetal '{tipoVeg}' eliminado correctamente ✅")
                            else:
                                print(f"No se pudo eliminar el vegetal '{tipoVeg}' ❌")
                            sc.pausar_pantalla()
                        case 6:
                            print("Seguro de que desea volver al menú principal? (S/N)")
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
            case 6:
                print("Seguro de que desea volver al menú principal? (S/N)")
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