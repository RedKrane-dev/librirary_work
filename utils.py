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


def add_book(library: dict) -> dict:
    """
    - Добавляет книгу в словарь library_dict
    - Если книга с таким названием уже существует, обновляет информацию о ней
    - Возвращает словарь library_dict
    """
    new_book_title = input('Введите название новой книги:\n')
    new_book_author = input('Введите автора новой книги:\n')
    new__book_year = input('Введите год публикации новой книги:\n')

    try:
        new_book_dict = {
            new_book_title: {
                'author': new_book_author.title(),
                'publication_year': int(new__book_year),
                'is_available': None
            }
        }

        if new_book_title in library:
            update_choice = input(f'\nКнига "{new_book_title}" уже есть в библиотеке.\n'
                                  'Обновить информацию о ней? (да/нет):\n')

            if update_choice.lower() == 'да':
                library[new_book_title] = new_book_dict
                print('Информация о книге обновлена\n')
            else:
                print('Книга в библиотеке осталась в первозданном виде. Новая книга удалена\n')
            return library

        library.update(new_book_dict)
        print(f'Книга "{new_book_title}" успешно добавлена в библиотеку\n')
        return library

    except ValueError:
        print('Ошибка. Передан неподходящий тип данных\n')


def remove_book(library: dict) -> dict:
    """
    - Удаляет книгу из словаря library_dict
    - Если книга не найдена, выводит сообщение об этом
    - Возвращает словарь library_dict
    """
    to_remove_book_title = input('Введите название книги на удаление:\n')

    if to_remove_book_title in library:
        del library[to_remove_book_title]
        print(f'Книга "{to_remove_book_title}" успешно удалена из библиотеки\n')
    else:
        print(f'Кажется, книги "{to_remove_book_title}" нет в нашей библиотеке. Операция отменена.\n')
    return library


def issue_book(library: dict) -> dict:
    """
    - Отмечает книгу как выданную, 'is_available' становится 'False'
    - Возвращает словарь library_dict
    """
    issue_book_title = input('Введите название книги на выдачу:\n')

    if issue_book_title in library:

        if library[issue_book_title]['is_available']:
            library[issue_book_title]['is_available'] = False
            print(f'Книга "{issue_book_title}" успешно выдана\n')
        else:
            print(f'Книга {issue_book_title} уже выдана. Попробуйте в другой день\n')

    else:
        print(f'Кажется, книги "{issue_book_title}" нет в нашей библиотеке. Операция отменена.\n')
    return library


def return_book(library: dict) -> dict:
    """
    - Отмечает книгу как вернувшуюся в библиотеку, 'is_available' становится 'True'
    - Возвращает словарь library_dict
    """
    return_book_title = input('Введите название книги на возврат:\n')

    if return_book_title in library:

        if not library[return_book_title]['is_available']:
            library[return_book_title]['is_available'] = True
            print(f'Книга "{return_book_title}" успешно возвращена\n')
        else:
            print(f'Книгу {return_book_title} уже вернули. Кажется, вы ошиблись библиотекой\n')

    else:
        print(f'Кажется, книги "{return_book_title}" нет в нашей библиотеке. Операция отменена.\n')
    return library


def find_book(library: dict):
    """
    Процедура
    - Выводит информацию о книге по ее названию
    - Если книга не найдена, выводит соответствующее сообщение
    """
    to_find_book_title = input('Введите название книги для поиска:\n')

    if to_find_book_title in library:
        print(f'\nНазвание: {to_find_book_title}\n'
              f'Автор: {library[to_find_book_title]["author"]}\n'
              f'Дата публикации: {library[to_find_book_title]["publication_year"]}')

        if library[to_find_book_title]["is_available"] is None:
            print('Книга в библиотеке, но ее статус не определен\n')
        elif library[to_find_book_title]["is_available"]:
            print('Книга доступна\n')
        elif not library[to_find_book_title]["is_available"]:
            print('Книга выдана\n')
    else:
        print(f'Кажется, книги "{to_find_book_title}" нет в нашей библиотеке. Операция отменена.\n')
