from utils import book_list_view, add_book, remove_book


def main(library):
    # Просмотр всех книг
    book_list_view(library)

    # Добавить новую книгу
    add_book('Ведьмак. Последнее желание.', 'Анджей Сапковский', 1986, library)
    book_list_view(library)

    # Удалить книгу
    remove_book('Властелин Колец. Братство кольца.', library)
    book_list_view(library)


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
