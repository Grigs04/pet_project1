
# ссылка на страницу с которой берем данные
url = 'https://auto.drom.ru/mazda/mazda6/page{}/?minyear=2010&unsold=1'

# путь файла, где хранятся страницы
file_path = 'C:\\projects\\pet_project1\\data\\html_files\\page'

# количество непустых страниц сайта
pages = 88

trim_score = {'low level' : 1,
              'low medium level': 2,
              'medium level': 3,
              'high medium level': 4,
              'high level': 5,
              'top level': 6,
              'premium level': 7}

car_levels = {
    '2.0 20S': 'low level',
    '1.8 MT Comfort': 'low level',
    '2.0 MT Prime-Line': 'low level',
    '1.8 MT Prime-Line': 'low level',
    '1.8 MT Center-Line': 'low level',
    '2.0 AT Center-Line': 'low level',
    '1.8 MT Direct': 'low level',

    '2.0 AT Active': 'low medium level',
    '2.0 MT Active': 'low medium level',
    '2.5 AT Active': 'low medium level',
    '2.0 AT Drive': 'low medium level',
    '2.0 MT Drive': 'low medium level',
    '1.8 MT Touring': 'low medium level',
    '1.8 MT Touring Plus': 'low medium level',
    '2.0 MT Touring Plus': 'low medium level',
    '2.5 AT Touring': 'low medium level',
    '2.5 AT High': 'low medium level',
    '2.0 AT Dynamic': 'low medium level',
    '2.0 AT Impulse Line': 'low medium level',

    '2.0 MT Sport': 'medium level',
    '2.5 MT Sport': 'medium level',
    '2.0 AT Sport': 'medium level',
    '2.5 AT Sport': 'medium level',
    '2.5i AT Sport': 'medium level',
    '2.0 AT Sports-Line': 'medium level',
    '2.5 AT Sports-Line': 'medium level',
    '2.0 AT Exclusive': 'medium level',
    '2.0 AT Exclusive-Line': 'medium level',
    '1.8 MT Exclusive': 'medium level',
    '1.8 MT Exclusive-Line': 'medium level',

    '2.0 AT Touring Plus': 'high medium level',
    '2.0 AT Supreme': 'high medium level',
    '2.0 AT Supreme Plus': 'high medium level',
    '2.0 AT Supreme Plus (пакет 1)': 'high medium level',
    '2.0 AT Supreme Plus (пакет 2)': 'high medium level',

    '2.5 AT Supreme': 'high level',
    '2.5 AT Supreme Plus': 'high level',
    '2.5 AT Supreme Plus (пакет 1)': 'high level',
    '2.5 AT Supreme Plus (пакет 2)': 'high level',
    '2.5 AT Executive': 'high level',
    '2.5 AT Executive Plus': 'high level',

    '2.5T AT Executive Plus': 'top level',
    '2.5 AT Grand Touring': 'top level',
    '2.5 AT 20th Anniversary': 'top level',
    '2.5T AT Carbon Edition': 'top level',

    'Atenza 2.0 AT Luxury': 'premium level',
    'Atenza 2.0 AT Honorable': 'premium level',
    '2.2 XD PROACTIVE': 'premium level',
    '2.2 AT Exclusive-Line': 'premium level',
    '2.2 AT Sports-Line 4WD': 'premium level',
    '2.2 XD L Package 4WD': 'premium level',
    '2.0 20S PROACTIVE': 'premium level'
}
