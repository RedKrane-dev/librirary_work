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
    try:
        new_book_dict = {
            title: {
                'author': author.title(),
                'publication_year': int(year),
                'is_available': None
            }
        }

        if title in library:
            update_choice = input(f'\nКнига "{title}" уже есть в библиотеке.\n'
                                  'Обновить информацию о ней? (да/нет):\n')

            if update_choice.lower() == 'да':
                library[title] = new_book_dict
                print('Информация о книге обновлена')
            else:
                print('Книга в библиотеке осталась в первозданном виде. Новая книга удалена')
            return library

        library.update(new_book_dict)
        print(f'\nКнига "{title}" успешно добавлена в библиотеку')
        return library

    except ValueError:
        print('Ошибка. Передан неподходящий тип данных')


def remove_book(title: str, library: dict) -> dict:
    """
    - Удаляет книгу из словаря library_dict
    - Если книга не найдена, выводит сообщение об этом
    - Возвращает словарь library_dict
    """
    if title in library:
        del library[title]
        print(f'\nКнига "{title}" успешно удалена из библиотеки')
    else:
        print(f'\nКажется, книги "{title}" нет в нашей библиотеке. Операция отменена.')
    return library


def issue_book(title: str, library: dict) -> dict:
    """
    - Отмечает книгу как выданную, 'is_available' становится 'False'
    - Возвращает словарь library_dict
    """
    if title in library:
        library[title]['is_available'] = False
        print(f'\nКнига "{title}" успешно выдана')
    else:
        print(f'\nКажется, книги "{title}" нет в нашей библиотеке. Операция отменена.')
    return library


def return_book(title: str, library: dict) -> dict:
    """
    - Отмечает книгу как вернувшуюся в библиотеку, 'is_available' становится 'True'
    - Возвращает словарь library_dict
    """
    if title in library:
        library[title]['is_available'] = True
        print(f'\nКнига "{title}" успешно возвращена')
    else:
        print(f'\nКажется, книги "{title}" нет в нашей библиотеке. Операция отменена.')
    return library
