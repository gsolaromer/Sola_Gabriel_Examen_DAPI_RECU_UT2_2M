diccionario = {}

while True:

    alimento = str(input('Ingresa el nombre del alimento: '))
    
    cantidad = str(input('Ingresa la cantidad consumida (en gramos): '))
    
    otro = str(input('¿Quieres registrar otro alimento? (si/no)'))

    diccionario[alimento]

    diccionario[cantidad]

    if otro == 'si':

        alimento2 = str(input('Ingresa el nombre del alimento: '))
        
        cantidad2 = str(input('Ingresa la cantidad consumida (en gramos): '))
        
        otro2 = str(input('¿Quieres registrar otro alimento? (si/no)'))

        diccionario[alimento2]

        diccionario[cantidad2]

    if otro2 == 'si':

        alimento3 = str(input('Ingresa el nombre del alimento: '))
        
        cantidad3 = str(input('Ingresa la cantidad consumida (en gramos): '))
        
        otro3 = str(input('¿Quieres registrar otro alimento? (si/no)'))

        diccionario[alimento3]
        
        diccionario[cantidad3]

    if otro3 == 'no':
        print('Resumen del consumo diario: \n' + str(alimento) + ':' + str(cantidad) + '\n' + str(alimento2) + ':' + str(cantidad2) + '\n' + str(alimento3) + ':' + str(cantidad3) + '\n')