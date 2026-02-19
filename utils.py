def book_list_view(library: dict):
    """
    Процедура
    - Принимает словарь с книгами
    - Выводит в консоль названия всех книг
    - Если книг нет, то информирует об этом
    """

    if library:
        start_message = '\nКниги нашей библиотеки:'

        print(f'{start_message}\n{"-" * len(start_message)}')
        for book in library:
            print(book)
    else:
        print('В данный момент в библиотеке нет книг')


def add_book(title: str, author: str, year: int, library: dict) -> dict:
    """
    - Добавляет книгу в словарь library_dict
    - Если книга с таким названием уже существует, обновляет информацию о ней
    - Возвращает словарь library_dict
    """
    new_book_dict = {
        title.capitalize(): {
            'author': author.title(),
            'publication_year': int(year),
            'is_available': None
        }
    }

    for book_title in library:

        if title.lower() == book_title.lower():
            update_choice = input(f'\nКнига "{title}" уже есть в библиотеке.\n'
                                  'Обновить информацию о ней? (да/нет):\n')

            if update_choice.lower() == 'да':
                library[title] = new_book_dict
                print('Информация о книге обновлена')
                return library
            else:
                print('Книга в библиотеке осталась в первозданном виде. Новая книга удалена')
                return library

    library.update(new_book_dict)
    print(f'\nКнига "{title}" успешно добавлена в библиотеку')

    return library

