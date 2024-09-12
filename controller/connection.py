from . import conn, xc


def insert_book(book):
    cursor = conn.cursor()
    params = {"name": book.title, "author": book.author, "category": book.category, "description": book.description,
              "book_img": book.thumbnail}
    cursor.execute(
        "EXEC them_sach @name=%(name)s , @author=%(author)s , @category=%(category)s , @description=%(description)s , @book_image=%(book_img)s, @quantity=1",
        params)
    conn.commit()
    cursor.close()


def check(book):
    cursor = conn.cursor()
    params = {"name": xc(book.title), "author": xc(book.author), "category": xc(book.category)}
    cursor.execute(
        "SELECT cnt = COUNT(*) FROM vwBook WHERE name=%(name)s AND author=%(author)s AND category=%(category)s", params)
    result = cursor.fetchall()
    if result[0][0] > 0:
        cursor.close()
        return True
    else:
        cursor.close()
        return False
