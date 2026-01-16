from bs4 import BeautifulSoup
from config import file_path, pages

# проходим по каждому html файлу и собираем необходимую информацию
def fill_cards():
    mazda_cards = []
    page = 1
    while page <= pages:
        with open(f'{file_path}{page}.html', 'r', encoding='utf-8') as f:
            html = f.read()

        root = BeautifulSoup(html, 'lxml')
        # проходим по каждому авто
        for car in root.find_all('div', {'data-ftid': 'bulls-list_bull'}):
            # записываем марку, модель и год автомобиля
            brand, model, year = car.find('h3').text.split(' ')

            # не все пользователи указывают все параметры, поэтому прибегаем к дополнительным проверкам
            tag = car.find('div', {'data-ftid': "bull_subtitle"})
            equipment = tag.text if tag else None
            fuel, transmission, drive, mileage, displacement, power = None, None, None, None, None, None
            for parametr in car.find_all('span', {'data-ftid': 'bull_description-item'}):
                parametr = parametr.text.strip(',').lower()
                if parametr in ('бензин', 'электро', 'дизель', 'гибрид', 'гбо'): fuel = parametr
                elif 'л.с.' in parametr: displacement, power = parametr.strip(')').split(' (')
                elif 'км' in parametr: mileage = int(parametr.replace(' ', '')[:-2])
                elif parametr in ('4wd', 'передний', 'задний'): drive = parametr
                elif parametr.lower() in ('акпп', 'автомат' ,'механика', 'робот', 'вариатор'): transmission = parametr


            price = int(car.find('span', {'data-ftid': 'bull_price'}).text.replace('\xa0', ''))

            city = car.find('span', {'data-ftid':"bull_location"}).text

            url = car.find('a', {'data-ftid':"bull_title"})['href']

            #сохраняем все в список для дальнейшей работы
            mazda_cards.append({'brand': brand, 'model': model.strip(','), 'year': int(year),
                                'equipment': equipment, 'displacement': displacement, 'power': power,
                                'fuel': fuel, 'transmission': transmission, 'drive': drive,
                                'mileage': mileage, 'price': price, 'city': city, 'url': url})

        page += 1
    return mazda_cards

if __name__ == '__main__':
    data_mazda = fill_cards()
