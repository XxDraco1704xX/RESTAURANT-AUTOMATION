from simulation import greet


assert greet('Hola, carta por favor', 
          { 'names': 'Andrea Gómez',
          'whatsapp': '+573209876543'},
          2) == 'ok'

assert greet('hola, qué hacen?',
         { 'names': 'Andrea Gómez',
          'whatsapp': '+573209876543'}, 2) == f'Hola Andrea Gómez, ¿deseas el menú?'

