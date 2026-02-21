from utils import book_list_view, add_book, remove_book, issue_book, return_book, find_book


def main(library):

    run_program = True
    print('Добро пожаловать в нашу библиотеку!')

    while run_program:
        print('\n1. Просмотр всех книг\n'
              '2. Добавить книгу в библиотеку\n'
              '3. Удалить книгу из библиотеки\n'
              '4. Выдать книгу читателю\n'
              '5. Вернуть книгу от читателя\n'
              '6. Найти книгу по названию\n'
              '7. Выход. Остановить программу\n'
              )
        try:
            user_input = int(input('Выберете интересующий пункт меню (1 - 7):\n'))

            if user_input == 1:
                book_list_view(library)

            elif user_input == 2:
                new_book_title = input('Введите название новой книги:\n')
                new_book_author = input('Введите автора новой книги:\n')
                new__book_year = input('Введите год публикации новой книги:\n')

                add_book(new_book_title, new_book_author, new__book_year, library)

            elif user_input == 3:
                to_remove_book_title = input('Введите название книги на удаление:\n')
                remove_book(to_remove_book_title, library)

            elif user_input == 4:
                issue_book_title = input('Введите название книги на выдачу:\n')
                issue_book(issue_book_title, library)

            elif user_input == 5:
                return_book_title = input('Введите название книги на возврат:\n')
                return_book(return_book_title, library)

            elif user_input == 6:
                to_find_book_title = input('Введите название книги для поиска:\n')
                find_book(to_find_book_title, library)

            elif user_input == 7:
                print('Выход из программы... Не отключайте компьютер от сети...')
                run_program = False

            else:
                print('\nВведена не существующая команда\n'
                      'Воспользуйтесь цифрами от 1 до 7\n'
                      'или обратитесь к системному администратору, если проблема сохранилась')

        except ValueError:
            print('\nВведена не существующая команда\n'
                'Воспользуйтесь цифровой клавиатурой от 1 до 7\n'
                'или обратитесь к системному администратору, если проблема сохранилась'
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


if __name__ == '__main__':
    main(library_dict)
