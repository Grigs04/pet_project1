from requests import get
from config import url, file_path, pages
from fake_useragent import UserAgent
import time

#скрапим html с каждой страницы
def fetch_html():
    page = 1
    while page <= pages:
        # для безопасности используем fake_useragent и задержку между переходами по страницам
        ua = UserAgent()
        time.sleep(2)
        response = get(url.format(page), headers={'User-Agent': ua.random}, timeout=5)
        response.raise_for_status()

        # записываем все файлы в папку
        with open(f'{file_path}{page}.html', 'w', encoding='utf-8') as f:
            f.write(response.text)

        page += 1
    print('Все готово!')

if __name__ == '__main__':
    fetch_html()