import os

from seleniumbase import SB

from model import Book
from . import lay_so, xc
from .connection import insert_book, check
from .log import logfile


def scrap_url():
    with SB(uc=True, headless=True, incognito=True) as sb:
        sb.open('https://www.dtv-ebook.com/the-loai-truyen-313.html')
        for i in range(0, lay_so(sb.get_attribute(
                '/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/ul/li[7]/a', 'href'))):
            if i > 0:
                sb.get(f'https://www.dtv-ebook.com/sach-truyen-ebook-313/{i + 1}.html')
            for j in range(0, 12):
                try:
                    scrap(sb.get_attribute(
                        f'/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/ul/li[{j + 1}]/div[1]/h2/a',
                        'href'))
                except Exception as e:
                    logfile(str(e))
    os.remove('./downloaded_files/')


def scrap(url):
    with SB(uc=True, headless=True, incognito=True) as sb:
        sb.open(url)
        title = sb.get_text('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/h2')
        author = sb.get_text(
            '/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/a')
        cate = sb.get_text('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[2]/a')
        des = sb.get_text('//*[@id="chitiet"]')
        thumbnail = [sb.get_attribute('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/img', 'src')]
        folder = 'downloaded_files'
        filepath = ''
        for src in thumbnail:
            if src.split('.')[-1] not in ['png', 'jpg', 'jpeg']:
                continue
            sb.download_file(src, './downloaded_files/')
            filename = src.split('/')[-1]
            sb.assert_downloaded_file(filename)
            filepath = os.path.join(folder, filename)
        img = open(filepath, 'rb').read()
        img_byte = bytearray(img)
        sach = Book(xc(title), xc(author), xc(cate), xc(des), img_byte)
        if not check(sach):
            insert_book(sach)
            img = None
            img_byte.clear()
            logfile(f'Book {title} inserted')
        else:
            img = None
            img_byte.clear()
            logfile(f'Book {title} already exists')
