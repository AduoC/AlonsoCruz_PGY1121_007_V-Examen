
print("Inmobiliaria CF-APP 3.0")
print("...")
print()
print()
print("|>----------------------------------------------------<|")
print("|>----------------< Bienvenido a ICF >----------------<|")

pisos = 10
departamentos_por_piso = 4
departamentos_disponibles = [[True] * departamentos_por_piso for _ in range(pisos)] 
precios = {"A": 3800, "B": 3000, "C": 2800, "D": 3500}
compradores = []

def mostrar_menu():


    print("|>----------------------------------------------------<|")
    print("|>------------ Venta de Departamentos ----------------<|")
    print("|>----------------------------------------------------<|")
    print("|>---(1)------ Comprar departamento ------------------<|")
    print("|>---(2)------ Mostrar departamentos disponibles -----<|") 
    print("|>---(3)------ Ver listado de compradores ------------<|")
    print("|>---(4)------ Mostrar ganancias totales -------------<|")
    print("|>---(5)------ Salir ---------------------------------<|")
    print("|>----------------------------------------------------<|")
    print()

def comprar_departamento():
    
    print()
    piso = int(input("Ingrese el numero de piso >>> "))
    if piso < 1 or piso > 10:
        print()
        print(">>> Dato Erroneo <<<")
        return
    print()
    tipo = input("Ingrese el tipo de departamento |A/B/C/D| >>> ").upper()
    departamento = f"{tipo}{piso}"

    if  tipo not in precios:
        print()
        print(">>> Dato Erroneo <<<")

    if not departamento_disponible(piso, tipo):
        print("(!!!) El departamento no esta disponible (!!!)")
        print()
        return

    print()
    run = input("Ingrese el RUN del comprador [sin puntos ni guion] >>> ")
    compradores.append({"departamento": departamento, "run": run})
    actualizar_disponibilidad(piso, tipo, False)
    print()
    print("($$$) Compra realizada correctamente ($$$)")
    print()

def mostrar_departamentos_disponibles():
    print()
    print("|>----- Departamentos Disponibles -----<|")
    print()
    print("        ________________________")
    print("        [ Piso | Tipo          ]")
    print("        [......| A | B | C | D ]")
    for piso in range(pisos, 0, -1):
        fila = f"        | {str(piso).ljust(3)}  |"
        for tipo in ["A", "B", "C", "D"]:
            if departamento_disponible(piso, tipo):
                fila += "   |"
            else:
                fila += " X |"
        print(fila)
    print('        """"""""""""""""""""""""')

def ver_listado_compradores():
    print()
    print("|>----- Listado de Compradores -----<|")
    print()
    compradores_ordenados = sorted(compradores, key=lambda x: x["run"])
    for comprador in compradores_ordenados:
        print(f"RUN >>> {comprador['run']} / Departamento >>> {comprador['departamento']}")

def mostrar_ganancias_totales():
    print()
    print("|>------------ Ganancias Totales -----------<|")
    print("______________________________________________")
    ventas_totales = {tipo: 0 for tipo in precios.keys()}
    for comprador in compradores:
        tipo = comprador["departamento"][0]
        ventas_totales[tipo] += precios[tipo]

    total_general = sum(ventas_totales.values())
    print("[Tipo Departamento  | Cantidad | Total       ]")
    for tipo, cantidad in ventas_totales.items():
        cantidad = sum(1 for comprador in compradores if comprador["departamento"][0] == tipo)
        total_tipo = precios[tipo] * cantidad
        print(f"|Tipo {tipo} {precios[tipo]} UF 4   | {str(cantidad).ljust(5)}    | {str(total_tipo).ljust(8)} UF |")
    print(f"[Total General      |          | {str(total_general).ljust(8)} UF ]")
    print('""""""""""""""""""""""""""""""""""""""""""""""')
    print()

def departamento_disponible(piso, tipo):
    return departamentos_disponibles[piso-1][ord(tipo)-ord("A")]

def actualizar_disponibilidad(piso, tipo, disponible):
    departamentos_disponibles[piso-1][ord(tipo)-ord("A")] = disponible

def main():
    while True:
        mostrar_menu()
        opcion = input("Ingrese una opcion >>> ")

        if opcion == "1":
            mostrar_departamentos_disponibles()
            comprar_departamento()
        elif opcion == "2":
            mostrar_departamentos_disponibles()
        elif opcion == "3":
            ver_listado_compradores()
        elif opcion == "4":
            mostrar_ganancias_totales()
        elif opcion == "5":
            print() 
            print(":( :( :( :( :(    <> Vuelva pronto <>    ): ): ): ): ):")
            print()
            print()
            print()
            print(".../Alonso_Cruz_10/07/23")
            break
        else:
            print()
            print("(!!!) Ingrese una opción valida (!!!)")
            print()

if __name__ == "__main__":
    main()
