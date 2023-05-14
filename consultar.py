import psycopg2

password_x = ""
user_x = ""

Contrato = ["ID","Fecha_firma","Fecha_fin","Dias_adicionados","Valor","Valor_pagado","Nit_EntidadPublica","Codigo_Producto","Num_Doc_Proveedor"]
Entidadpublica = ["Nit","Nombre","Departamento"]
Proveedor = ["Num_Doc","Nombre"]
Producto = ["Codigo","Nombre"]
tables = [Contrato,Entidadpublica,Proveedor,Producto]
table_names = ["Contrato","EntidadPublica","Proveedor","Producto"]
print("escribe tu usuario de postgresql: ")
user_x = input()

print("escribe tu contraseña: ")
password_x = input()

print("""
SELECCIONA LA TABLA QUE QUE QUIERES CONSULTAR:
   0. CONTRATO
   1. ENTIDAD_PUBLICA
   2. PROVEEDOR
   3. PRODUCTO
""")

selected_table = int(input("SELECCIONA EL NUMERO CORRESPONDIENTE A LA TABLA: "))


final = ""
table_name = table_names[selected_table]

if(selected_table == 0):
    print("""
    SELECCIONA LA COLUMNA QUE QUIERES CONSULTAR O * PARA VER TODOS LOS DATOS:
       0. ID
       1. FECHA DE FIRMA
       2. FECHA DE FIN
       3. DIAS ADICIONADOS
       4. VALOR
       5. VALOR PAGADO
       6. NIT ENTIDAD PUBLICA
       7. CODIGO PRODUCTO
       8. NUMERO DE DOCUMENTO DEL PROVEEDOR
       9. *
    """)
    selected_column = input("Tu selección: ")
    if(selected_column != "*"):
        selected_column = int(selected_column)
    if(selected_column != 9):
        final = tables[selected_table][selected_column]
elif selected_table == 1:
    print("""SELECCIONA LA COLUMNA QUE QUIERES CONSULTAR O * PARA VER TODOS LOS DATOS:
       0. NIT
       1. NOMBRE
       2. DEPARTAMENTO
       3. *
    """)
    selected_column = input("Tu selección: ")
    if(selected_column != "*"):
        selected_column = int(selected_column)
    if(selected_column != 3):
        final = tables[selected_table][selected_column]
elif selected_table == 2:
    print("""SELECCIONA LA COLUMNA QUE QUIERES CONSULTAR O * PARA VER TODOS LOS DATOS:
       0. NUMERO DE DOCUMENTO
       1. NOMBRE
       2. *
    """)
    selected_column = input("Tu selección: ")
    if(selected_column != "*"):
        selected_column = int(selected_column)
    if(selected_column != 2):
        final = tables[selected_table][selected_column]
elif selected_table == 3:
    print("""SELECCIONA LA COLUMNA QUE QUIERES CONSULTAR O * PARA VER TODOS LOS DATOS:
       0. CODIGO
       1. NOMBRE DEL PRODUCTO
       2. *
    """)
    selected_column = input("Tu selección: ")
    if(selected_column != "*"):
        selected_column = int(selected_column)
    if(selected_column != 2):
        final = tables[selected_table][selected_column]

sql1 = "SELECT * FROM " + table_name + ";"
sql2 = "SELECT " + final + " FROM " + table_name

print(sql2)

try:
    conexion = psycopg2.connect(user= user_x, password= password_x, database="IcbfContracts", host="localhost", port="5432")
    cursor = conexion.cursor()
    
    if selected_column != "*":
        cursor.execute(sql2)
        selection = cursor.fetchone()
        while selection:
            print(selection[0])
            selection = cursor.fetchone()
    else:
        cursor = conexion.cursor()
        cursor.execute(sql1)
        selections = cursor.fetchall()
        for selection in selections:
            for i in range(len(tables[selected_table])):
                print(selection[i])

except psycopg2.Error as e:
    print("Ocurrio un error al consultar")
finally:
    cursor.close()
    conexion.close()






