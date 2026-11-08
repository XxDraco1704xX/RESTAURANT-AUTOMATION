
datos = [(1, 'Entrada', 'Empanadas'), (2, 'Principio', 'Frijol🫘 con Torta de Banano'), 
         (3,'Entrada', 'Crema de pescado' )
]

index = {
    'category': 1,
    'item_name': 2
}
entradas = [e for e in datos if index['category'] == 'Entrada']

for item in entradas:
    category = index['category']
    item_name = index['item_name']
    print(f"""
          - {category} \n
          - {item_name}
        """)




        