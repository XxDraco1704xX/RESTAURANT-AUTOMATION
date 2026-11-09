import os
import time
import mysql.connector; from mysql.connector import errorcode
import string
try:

    conn = mysql.connector.connect(
        host= '127.0.0.1',
        user= 'root',
        password=os.environ['SQL_PASSWORD'],
        database= 'restaurants_automation',  
        auth_plugin = 'mysql_native_password' 
    ) 

    cursor = conn.cursor()
#BLOQUE DE EXCEPCIONES-----
except mysql.connector.Error as err:
   if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
   elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
   else:
     print(err)

def get_or_create_client(client_data):
  cursor.execute( "SELECT id,names, whatsapp FROM clients WHERE names = %s",(client_data["names"],))
  results = cursor.fetchall()    

  if not results: 
        query_insert = "INSERT INTO clients (names, whatsapp) VALUES (%s, %s);"
        cursor.execute(query_insert, (client_data['names'], client_data['whatsapp']))
        conn.commit() 
        
    
def return_menu(restaurant): 
     #Seleccionar el menú diario
     """According to the restaurant data, I'll put a query for seek a generic restaurant
     menu as 'Special' with a unique price if the case is presented"""
   
     #Show menu
     cursor.execute(
     """
     SELECT names FROM restaurants
     WHERE id = %s
     """,
     (restaurant['id'],),)
     restaurant_name = cursor.fetchone()

     cursor.execute('''SELECT id,category,item_name FROM menu_items
                    WHERE day=%s
                    ''',
                    (restaurant['day'],))        
     cursor.fetchall()
     print(
        f'¡ Hoy se come rico en {restaurant_name}! este es nuestro menú \n {cursor.fetchall()} ')

     ask_order()

def ask_order():
     items_ordered = input('Coloca los IDs de lo que deseas pedir:')
     items_ordered.split(' ')

     return_price(restaurant['id'])

     if return_price == 'No te he entendido, ¿podrías específicar si es para llevar o para mesa?':
       items_ordered = input("Coloca los ID's separados por comas: \n")


def return_price(restaurant):
  """
  This method takes a unique price for local or taking the order for house because some restaurants can 
  bill a plain billing independtly what protein you order.
  Returns:
  The price of the order taking into account if it's for eating at restaurant or for home, also returns a messague
  indicating where to pay.
  """
  nequi_num = '+57 300 255 3901'
  davi_num = '+57 322 199 2034'
  pay_method_messague = f"Puedes pagar al Nequi {nequi_num} o al Daviplata {davi_num}"

  print('para llevar o mesa?')
  is_take_away = 'mesa por favor' #input("Para llevar o para mesa?: ")

  if 'llevar' in is_take_away.lower().split():
    cursor.execute("""
                   SELECT amount FROM prices
                   WHERE sale_type = 'llevar' 
                   AND day_id=%s AND restaurant_id = %s
                   """,
                   (2,restaurant))
    
    total = cursor.fetchall()
    print(f"El precio es: {total}\n {pay_method_messague }")
    return f"El total es: {cursor.fetchall()}\n {pay_method_messague }"
                  
  elif 'mesa' in is_take_away.lower().split():
   cursor.execute(f"""
                 SELECT amount FROM prices
                 WHERE sale_type = 'mesa' 
                 AND day_id =%s AND restaurant_id = %s
                 """, (2, restaurant),         
                 );print(f"Tú total es ${cursor.fetchall()} \n{pay_method_messague}") 
   
   return f"""Tú total es ${cursor.fetchone()} \n {pay_method_messague}"""
  else:
    return 'No te he entendido, ¿podrías específicar si es para llevar o para mesa?'



def confirm(items_ordered):
  """
  This method will prevent for user digitation mistakes. If the user
  entered a wrong id of a menu accidentally it will let him enter them again
  restarting the order.
  """
  formated = ','.join(['%s'] * len(items_ordered))
  cursor.execute(f"""
    SELECT item_name FROM menu_items
    WHERE category = 'entrada' AND id = {formated}
    """,
    items_ordered)  
  apperitive = cursor.fetchall()  # Extraes el dato real con el cursor

  return f"Confirmo tú orden {client_data['names']}. Tú orden es {apperitive[0]}"

client_data = {
    'names': 'Andrea Gómez',
    'whatsapp': '+573209876543'
}
restaurant= {
   'id' : 2, 'day': 1,
}
 #Marmita 
import string
user_messague = 'hola, carta por favor.'
standarized_messague = user_messague.lower()
standarized_messague.translate(str.maketrans('','', string.punctuation))

print(standarized_messague)
def greet(user_messague, client_data, restaurant_data):
 get_or_create_client(client_data)

 KEY_WORDS = {'menú','menu','carta','comidas','comida'}
 if any(w in user_messague.lower() for w in KEY_WORDS): 
   print(f'Hola {client_data["names"]} gracias por comunicarte con {restaurant_data['id']}')

   return_menu(restaurant)
   return 'Ok'
 else: 
       print(f'Hola {client_data['names']}, ¿deseas el menú?')  #temporal
       get_user_menu_request()
       return f'Hola {client_data['names']}, ¿deseas el menú?' 

def get_user_menu_request():
   #input de twilio
   menu_request = input('si/no: ')
   if menu_request:
      if 'si' in menu_request.lower().split(' '):
        get_or_create_client(client_data)
      else:
        return 'muchas gracias'
        #TWILIO CERRAR SESIÓN
   else:
       return 'has mandado un mensaje vacío \n ingresa si quieres el menú o no'

greet(user_messague, client_data, restaurant)

"""
if greet(messague)==f'Hola {client_data['names']}, ¿deseas el menú?':
  if input('').lower().split() in ('menú','menu','sí',
                                   'si','no',):
    return_menu(client_data)      
else:
  pass
"""