import pymssql
import os
from dotenv import load_dotenv
load_dotenv()
"""
Connects to a SQL database using pymssql
"""
conn = pymssql.connect(
    server=os.getenv('SERVER'),
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database=os.getenv('DATABASE'),
    as_dict=True
)  
def insert_book(book):
    cursor = conn.cursor()
    params = {
        "name": book.title,
        "author": book.author,
        "category": book.category,
        "description": book.description,
        "book_img": book.thumbnail
    }
    cursor.execute("EXEC them_sach @name=%(name)s , @author=%(author)s , @category=%(category)s , @description=%(description)s , @book_image=%(book_img)s", params)
    conn.commit()
    cursor.close()