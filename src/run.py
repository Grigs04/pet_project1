from fetch import fetch_html
from pet_project1.src.analysis import most_profitable_car
from unloading import loading_data
from analysis import most_profitable_car


def run():
    # fetch_html()
    loading_data()
    most_profitable_car()

if __name__ == "__main__":
    run()
