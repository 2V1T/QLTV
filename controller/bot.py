from seleniumbase import SB
from model.obj import book
from controller.connection import insert_book
# from PIL import Image
import re
import os

def lay_so(trang_tham_chieu):
    pattern = r'/(\d+)(?=\.html$)'
    tim_kiem = re.search(pattern, trang_tham_chieu)
    if tim_kiem:
        return int(tim_kiem.group(1))
    else:
        return None
def scrap_url():
    with SB(uc=True, headless=True, incognito=True) as sb:
        sb.open('https://www.dtv-ebook.com/the-loai-truyen-313.html')
        for i in range(0, lay_so(sb.get_attribute('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/div[2]/div[2]/ul/li[7]/a', 'href'))):
            if (i>0):
                sb.get(f'https://www.dtv-ebook.com/sach-truyen-ebook-313/{i+1}.html')
            for j in range(0, 12):
                try:
                    scrap(sb.get_attribute(f'/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/ul/li[{j+1}]/div[1]/h2/a', 'href'))
                except Exception as e:
                    print(e)
def scrap(url):
    with SB(uc=True, headless=True, incognito=True) as sb:
        sb.open(url)
        title = sb.get_text('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[1]/td/h2')
        author = sb.get_text('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[2]/td[2]/a')
        cate = sb.get_text('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tbody/tr[4]/td[2]/a')
        des = sb.get_text('//*[@id="chitiet"]')
        thumbnail = []
        thumbnail.append(sb.get_attribute('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/img', 'src'))
        for src in thumbnail:
            if src.split('.')[-1] not in ['png', 'jpg', 'jpeg']:
                continue
            sb.download_file(src, './downloaded_files/')
            filename = src.split('/')[-1]
            sb.assert_downloaded_file(filename)
            folder = 'downloaded_files'
            filepath = os.path.join(folder, filename)
            with open(filepath, 'rb') as f:
                img = f.read()
                img_byte = bytearray(img)
                sach=book(title, author, cate, des, img_byte)
                insert_book(sach)
        os.remove(filepath)
