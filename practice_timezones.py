from datetime import datetime
import pytz

def timezone(city: str):
    ciudad = city.lower().capitalize()
    timezone = pytz.timezone('America/'+ciudad)
    date = datetime.now(timezone)
    print('La hora requerida es:')
    print(f"{ciudad}: {date.strftime('%d/%m/%Y, %H:%M:%S')}")

def cities(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print('Gracias por usar la aplicación, adios!!')
    return wrapper

@cities
def city_time():
    city = input('Ingresa la ciudad de la que quieres saber su hora: ')
    timezone(city)


if __name__ == '__main__':
    city_time()
