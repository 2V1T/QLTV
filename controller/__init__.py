import re

import pymssql
from dotenv import dotenv_values

"""
Connects to a SQL database using pymssql
"""
config = dotenv_values('.env')
conn = pymssql.connect(server=config['SERVER'], user=config['USER'], password=config['PASSWORD'],
                       database=config['DATABASE'])


def lay_so(trang_tham_chieu):
    pattern = r'/(\d+)(?=\.html$)'
    tim_kiem = re.search(pattern, trang_tham_chieu)
    if tim_kiem:
        return int(tim_kiem.group(1))
    else:
        return None


def xc(word):
    """
    Hàm xóa cách đầu dòng trong chuỗi
    """
    return re.sub(r'^\s+', '', word, flags=re.MULTILINE)
