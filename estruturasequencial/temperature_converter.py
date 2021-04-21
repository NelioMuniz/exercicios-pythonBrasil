def celsius_to_fahrenheit():
    celsius = float(input('Digite aqui a temperatura em Celsius: '))
    fahrenheit = ((celsius * (9 / 5)) + 32)
    print('A temperatura em graus Fahrenheit é {:.1f}°F'.format(fahrenheit))

def fahrenheit_to_celsius():
    fahrenheit = float(input('Digite aqui a temperatura em Fahrenheit: '))
    celsius = 5 * ((fahrenheit - 32) / 9)
    print('A temperatura em graus Celsius é {:.1f}°C'.format(celsius))

if __name__ == '__main__':
    celsius_to_fahrenheit()
    fahrenheit_to_celsius()
