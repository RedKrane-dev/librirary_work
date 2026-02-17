def book_list_view(library: dict[str]):
    """
    Процедура
    - Принимает словарь с книгами
    - Выводит в консоль названия всех книг
    - Если книг нет, то информирует об этом
    """

    if library:
        start_message = 'Книги нашей библиотеки:'

        print(f'{start_message}\n{"-" * len(start_message)}')
        for book in library:
            print(book)
    else:
        print('В данный момент в библиотеке нет книг')

