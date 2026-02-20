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

        print(f'{"-" * len(start_message)}')
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
                print('Информация о книге обновлена\n')
            else:
                print('Книга в библиотеке осталась в первозданном виде. Новая книга удалена\n')
            return library

        library.update(new_book_dict)
        print(f'Книга "{title}" успешно добавлена в библиотеку\n')
        return library

    except ValueError:
        print('Ошибка. Передан неподходящий тип данных\n')


def remove_book(title: str, library: dict) -> dict:
    """
    - Удаляет книгу из словаря library_dict
    - Если книга не найдена, выводит сообщение об этом
    - Возвращает словарь library_dict
    """
    if title in library:
        del library[title]
        print(f'Книга "{title}" успешно удалена из библиотеки\n')
    else:
        print(f'Кажется, книги "{title}" нет в нашей библиотеке. Операция отменена.\n')
    return library


def issue_book(title: str, library: dict) -> dict:
    """
    - Отмечает книгу как выданную, 'is_available' становится 'False'
    - Возвращает словарь library_dict
    """
    if title in library:

        if library[title]['is_available']:
            library[title]['is_available'] = False
            print(f'Книга "{title}" успешно выдана\n')
        else:
            print(f'Книга {title} уже выдана. Попробуйте в другой день\n')

    else:
        print(f'Кажется, книги "{title}" нет в нашей библиотеке. Операция отменена.\n')
    return library


def return_book(title: str, library: dict) -> dict:
    """
    - Отмечает книгу как вернувшуюся в библиотеку, 'is_available' становится 'True'
    - Возвращает словарь library_dict
    """
    if title in library:

        if not library[title]['is_available']:
            library[title]['is_available'] = True
            print(f'Книга "{title}" успешно возвращена\n')
        else:
            print(f'Книгу {title} уже вернули. Кажется, вы ошиблись библиотекой\n')

    else:
        print(f'Кажется, книги "{title}" нет в нашей библиотеке. Операция отменена.\n')
    return library


def find_book(title: str, library: dict):
    """
    Процедура
    - Выводит информацию о книге по ее названию
    - Если книга не найдена, выводит соответствующее сообщение
    """
    if title in library:
        print(f'Название: {title}\n'
              f'Автор: {library[title]["author"]}\n'
              f'Дата публикации: {library[title]["publication_year"]}')

        if library[title]["is_available"] is None:
            print('Книга в библиотеке, но ее статус не определен')
        elif library[title]["is_available"]:
            print('Книга доступна')
        elif not library[title]["is_available"]:
            print('Книга выдана')
    else:
        print(f'Кажется, книги "{title}" нет в нашей библиотеке. Операция отменена.\n')
