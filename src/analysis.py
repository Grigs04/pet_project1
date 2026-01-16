import pandas as pd

# определяем самые выгодные авто
def most_profitable_car():
    df = pd.read_excel('C:\\projects\\pet_project1\\data\\mazda_cars.xlsx')
    # разбиваем их по поколениям
    generation_GH = df[df['year'] <= 2012]
    generation_GJ = df[(df['year'] > 2012) & (df['year'] <= 2018)]
    generation_GL = df[df['year'] > 2018]
    point_counter(generation_GL)[['year', 'price', 'equipment', 'power', 'mileage', 'url']].to_excel('C:\\projects\\pet_project1\\data\\best_mazda_cars.xlsx', sheet_name='Самые выгодные авто', index=False)

# считаем для каждого авто количество поинтов выгоды
def point_counter(generation_data: pd.DataFrame) -> pd.DataFrame:
    from config import car_levels, trim_score
    generation_data = generation_data.copy()
    generation_data['points'] = generation_data['year'] % (generation_data['year'].min() - 1)
    generation_data['points'] += generation_data['equipment'].map(car_levels).map(trim_score).fillna(0)
    generation_data.loc[generation_data['transmission'].isin(['автомат', 'акпп']), 'points'] += 3

    mask = generation_data['mileage'] < 100000
    generation_data.loc[mask, 'points'] += (
            (100000 - generation_data.loc[mask, 'mileage']) / 10000
    ).round()

    # считаем сколько стоит каждый поинт
    generation_data['points'] = generation_data['price'] // generation_data['points']
    # определяем 5 самых выгодных авто
    generation_data = generation_data.sort_values(by='points')
    return generation_data.head(5)

if __name__ == '__main__':
    most_profitable_car()
