from parser import OzoneParser
from pathlib import Path


SEARCH_QUERY = 'ноутбук'

my_parser = OzoneParser(search_query=SEARCH_QUERY)
my_parser.run_process()
print("Итого по заданному запросу: ")
for item in my_parser.results:
    print(item)

data_dir = Path(__file__).parent.resolve() / 'data'
data_dir.mkdir(exist_ok=True)
file_xlsx = data_dir / 'ozon_laptops.xlsx'

try:
    my_parser.save_to_xlsx(xlsx_path=file_xlsx)
    print(f"\n--- [Успех] Данные сохранены в файл {file_xlsx} ---")
except Exception as e:
    print(f"\n--- [Ошибка] Не удалось сохранить данные. Ошибка {e}")
print("\n--- Итоговый результат ---")
for item in my_parser.results:
    print(item)


    # --- "СТОП-КРАН" ---
    # input("!!! ПОИСК ВЫПОЛНЕН. press Enter...")
    # --- ---
