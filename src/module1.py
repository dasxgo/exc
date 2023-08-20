def city(country):
    if country == 'Colombia':
        return 'Bogota'
    elif country == 'Brasil':
        return 'Sao Paulo'
    elif country == 'Peru':
        return 'Lima'
    elif country == 'Ecuador':
        return 'Quito'
    else:
        return 'Desconocido'

if __name__ == '__main__':
    print(f'The city is =>',city('Peru'))

