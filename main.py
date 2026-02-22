from utils import book_list_view, add_book, remove_book, issue_book, return_book, find_book


def main(library, main_menu):
    print('Добро пожаловать в нашу библиотеку!')

    while True:
        try:
            for operation in main_menu:
                print(*operation)

            user_input = int(input('Выберете интересующий пункт меню (1 - 0):\n'))

            if user_input == 0:
                print('Выход из программы... Не отключайте компьютер от сети...')
                break

            for line in main_menu.keys():
                if user_input in line:
                    main_menu[line](library)
                    break

            else:
                print('\nВведена не существующая команда\n'
                      'Воспользуйтесь цифрами от 1 до 0\n'
                      'или обратитесь к системному администратору, если проблема сохранилась\n')

        except ValueError:
            print('\nОшибка\n'
                'Воспользуйтесь цифровой клавиатурой от 1 до 0\n'
                'или обратитесь к системному администратору, если проблема сохранилась\n'
            )

library_dict = {
    'Гарри Поттер и философский камень': {
        'author': 'Джоан Роулинг',
        'publication_year': 1997,
        'is_available': True
    },
    'Властелин Колец. Братство кольца.': {
        'author': 'Дж. Р. Р. Толкин',
        'publication_year': 1954,
        'is_available': True
    }
}

main_menu_dict = {
    (1, '- Просмотр всех книг'): book_list_view,
    (2, '- Добавить книгу в библиотеку'): add_book,
    (3, '- Удалить книгу из библиотеки'): remove_book,
    (4, '- Выдать книгу читателю'): issue_book,
    (5, '- Вернуть книгу от читателя'): return_book,
    (6, '- Найти книгу по названию'): find_book,
    (0, '- Выход из программы'): None
}


if __name__ == '__main__':
    main(library_dict, main_menu_dict)
