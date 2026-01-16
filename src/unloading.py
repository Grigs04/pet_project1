import pandas as pd
import sqlite3

def loading_data():
    from parser import fill_cards

    mazda_data = fill_cards()
    mazda_data = pd.DataFrame(mazda_data)
    mazda_data.index += 1

    loading_data_to_excel(mazda_data)
    loading_data_to_sql(mazda_data)

def loading_data_to_excel(data: pd.DataFrame) -> None:
    data.to_excel(
        'C:\\projects\\pet_project1\\data\\mazda_cars.xlsx',
        index=False,
        sheet_name='Cars_Mazda6')

def loading_data_to_sql(data: pd.DataFrame) -> None:
    conn = sqlite3.connect('C:\\projects\\pet_project1\\data\\mazda_cars.db')
    data.to_sql(
        name='Cars_Mazda6',
        index=False,
        con=conn,
        if_exists='replace'
    )
    conn.close()

if __name__ == '__main__':
    loading_data()
