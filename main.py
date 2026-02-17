from utils import book_list_view


def main(library):
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
