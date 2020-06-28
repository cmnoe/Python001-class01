import requests
from bs4 import BeautifulSoup as bs

#用户代理
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'



# 请求头
header = {'user-agent': 'my-app/0.0.1'}

# 目标网址
targetUrl = 'https://maoyan.com/films?showType=3'

# 拿到目标网页
response = requests.get(targetUrl, headers=header)

# 处理html
bs_info = bs(response.text, 'html.parser')

movie_list = [('电影名', '类型', '上映日期')]
for tags in bs_info.find_all('div', attrs={'class', 'movie-hover-info'})[0:10]:
    # 电影名称
    film_name = tags.find('span', {'class', 'name'}).get_text(strip = True)
    for i, attrs in enumerate(tags.find_all('div', attrs={'class', 'movie-hover-title'})):
        if i == 1:
            # 电影类型
            film_type = attrs.contents[-1].strip()
        if i == 3:
            # 上映时间
            plan_date = attrs.contents[-1].strip()
    movie_list += [(film_name, film_type, plan_date)]

import pandas as pd

movie = pd.DataFrame(data = movie_list)

movie.to_csv('./movie.csv', encoding='utf_8_sig', index=False, header=False)


