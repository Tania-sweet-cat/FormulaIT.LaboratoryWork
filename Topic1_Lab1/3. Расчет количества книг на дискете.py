# TODO Найдите количество книг, которое можно разместить на дискете
floppy_disk_size = 1.44 # информационный размер дискеты в Мб
number_of_pages = 100 # число страниц в книге
number_of_rows = 50 # число строк на страниц
number_of_symbols = 25 # число символов в строке
size_of_symbol = 4 # размер одного символа в байтах

size_of_book_in_bytes = size_of_symbol * number_of_symbols * number_of_rows * number_of_pages
floppy_disk_size_in_bytes = floppy_disk_size * (1024 ** 2)
count_of_books = int(floppy_disk_size_in_bytes // size_of_book_in_bytes)

print("Количество книг, помещающихся на дискету:", count_of_books)
