import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from wordcloud import WordCloud

driver_path = '/Users/eunhui/PycharmProjects/gameCrawler/chromedriver'
browser = webdriver.Chrome(executable_path=driver_path)


def game_crawler(input_game_url_list, preference):
    game_dict = {}
    name_list = []
    genre_list = []
    description_list = []
    install_list = []
    review_list = []
    star_list = []

    for url in input_game_url_list:
        browser.get(url)
        page = browser.page_source
        soup = BeautifulSoup(page, 'html.parser')

        # 게임 이름 얻어오기
        name_sub = soup.find('h1', {'class': 'AHFaub'})
        name = name_sub.find('span')
        name_list.append(name.text)
        game_dict['name'] = name_list

        # 게임 장르 얻어오기
        genre = soup.find('a', itemprop='genre')
        genre_list.append(genre.text)
        game_dict['genre'] = genre_list

        # 게임 설명 얻어오기 (워드클라우드로 만들어보고 싶음)
        description_sub = soup.find('div', {'class': 'W4P4ne'})
        description = description_sub.find('meta', itemprop='description')
        # print(description['content'])
        description_list.append(description['content'])
        game_dict['description'] = description_list

        # 설치 수 얻어오기
        install_sub = soup.find_all('div', {'class': 'IQ1z0d'})
        install_list.append(install_sub[4].text)
        game_dict['install'] = install_list

        # 리뷰 수 얻어오기
        sub_review = soup.find('span', {'class': 'AYi5wd TBRnV'})
        review_num = sub_review.find('span')
        review = float(review_num.text.replace(',', ''))
        review_list.append(review)
        game_dict['review'] = review_list

        # 별점 수 얻어오기
        star = soup.find('div', {'class': 'BHMmbe'})
        star = float(star.text.replace(',', ''))
        star_list.append(star)
        game_dict['star'] = star_list

    df = pd.DataFrame(game_dict)
    print(df)
    df.to_csv(f'{preference}.csv')
    return df


def data_summary(input_df):
    # print(input_df.shape)
    print('장르:', input_df['genre'].mode().iloc[0])
    print(input_df['genre'].value_counts())
    print('설치수:', input_df['install'].mode().iloc[0])
    print(input_df['install'].value_counts())
    print('평균리뷰수:', input_df['review'].mean())
    print('평균별점:', input_df['star'].mean())
    # print('장르 수: ', input_df['genre'].unique())


fav_game_url_list = ['https://play.google.com/store/apps/details?id=com.sushirolls.app',
                     'https://play.google.com/store/apps/details?id=com.smilegate.magicshop.stove.google',
                     'https://play.google.com/store/apps/details?id=com.unicostudio.whois',
                     'https://play.google.com/store/apps/details?id=com.nianticlabs.pokemongo',
                     'https://play.google.com/store/apps/details?id=com.nexon.kart',
                     'https://play.google.com/store/apps/details?id=com.loltap.freezerider',
                     'https://play.google.com/store/apps/details?id=com.playrix.homescapes',
                     'https://play.google.com/store/apps/details?id=com.ketchapp.rider',
                     'https://play.google.com/store/apps/details?id=com.rubygames.slingdrift',
                     'https://play.google.com/store/apps/details?id=com.ncsoft.lineagem19',
                     'https://play.google.com/store/apps/details?id=com.ncsoft.lineage2m19',
                     'https://play.google.com/store/apps/details?id=com.nexon.fmk',
                     'https://play.google.com/store/apps/details?id=gg.sunday.catescape',
                     'https://play.google.com/store/apps/details?id=linkdesks.pop.bubblegames.bubbleshooter',
                     'https://play.google.com/store/apps/details?id=com.devsisters.gb',
                     'https://play.google.com/store/apps/details?id=com.supersolid.penguin',
                     'https://play.google.com/store/apps/details?id=com.healingjjam.skycastle',
                     'https://play.google.com/store/apps/details?id=com.raongames.growcastle',
                     'https://play.google.com/store/apps/details?id=com.gma.water.sort.puzzle',
                     'https://play.google.com/store/apps/details?id=com.rawhand.dts.gl',
                     'https://play.google.com/store/apps/details?id=com.hutchgames.rebelracing',
                     'https://play.google.com/store/apps/details?id=com.netmarble.sknightsmmo',
                     'https://play.google.com/store/apps/details?id=com.cjenm.ModooMarbleKakao',
                     'https://play.google.com/store/apps/details?id=com.netmarble.koongyacm',
                     'https://play.google.com/store/apps/details?id=games.artisticode.gomokuclan',
                     'https://play.google.com/store/apps/details?id=kr.aos.com.aprogen.hng.fortressm',
                     'https://play.google.com/store/apps/details?id=com.nexon.nsc.maplem',
                     'https://play.google.com/store/apps/details?id=com.nexon.baram',
                     'https://play.google.com/store/apps/details?id=com.kakaogames.gdtskr',
                     'https://play.google.com/store/apps/details?id=com.kakaogames.friendsracing']
hate_game_url_list = ['https://play.google.com/store/apps/details?id=com.nani.ego.kr.aos',
                      'https://play.google.com/store/apps/details?id=com.iclubjoy.fzrfthg',
                      'https://play.google.com/store/apps/details?id=com.yaking.google',
                      'https://play.google.com/store/apps/details?id=com.miHoYo.GenshinImpact',
                      'https://play.google.com/store/apps/details?id=kr.xdg.rs.android',
                      'https://play.google.com/store/apps/details?id=com.szckhd.jwgly.azkr',
                      'https://play.google.com/store/apps/details?id=com.stove.epic7.google',
                      'https://play.google.com/store/apps/details?id=com.carolgames.moemoegirls',
                      'https://play.google.com/store/apps/details?id=com.krbn.jinsanguo',
                      'https://play.google.com/store/apps/details?id=com.braindom2riddle',
                      'https://play.google.com/store/apps/details?id=com.qjzj4399kr.google',
                      'https://play.google.com/store/apps/details?id=com.sstl.yjzx.google',
                      'https://play.google.com/store/apps/details?id=com.ag.lwkr',
                      'https://play.google.com/store/apps/details?id=com.gsm.google',
                      'https://play.google.com/store/apps/details?id=com.eternalone.google',
                      'https://play.google.com/store/apps/details?id=com.freelyfree.google.miraclefantasy',
                      'https://play.google.com/store/apps/details?id=com.digging.tk.gp',
                      'https://play.google.com/store/apps/details?id=com.monawa.gswordgg'
                      ]

fave_game_df = game_crawler(fav_game_url_list, 'favorite_game')
hate_game_df = game_crawler(hate_game_url_list, 'hate_game')

data_summary(fave_game_df)
data_summary(hate_game_df)
