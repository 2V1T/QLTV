# from model.model import book
from seleniumbase import SB
import re

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
                    print(sb.get_attribute(f'/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/ul/li[{j+1}]/div[1]/h2/a', 'href'))
                except Exception as e:
                    print(e)
scrap_url()
# def scrap(url):
#     with SB(uc=True, headless=True, incognito=True) as sb: