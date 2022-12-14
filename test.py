import json


class Updating:
    title: str

    def __init__(self, obj=None):
        if obj is not None:
            for key, value in obj.items():
                setattr(self, key, value)


test_json = """
[
  {
    "id": 1,
    "title": "Анджелина Джоли",
    "content": "Анджелина Джоли (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.\r\n\r\nОбладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».\r\n\r\nДебютировала в кино в 1982 году, сыграв роль в комедийном фильме «В поисках выхода» (где снимались также её отец и мать)[8], однако известность получила после того, как сыграла героиню видеоигр Лару Крофт в фильмах «Лара Крофт: Расхитительница гробниц» и «Лара Крофт: Расхитительница гробниц 2 — Колыбель жизни».\r\n\r\nВ 2009, 2011 и 2013 годах по версии журнала Forbes Джоли была названа самой высокооплачиваемой актрисой Голливуда[9][10].\r\n\r\nЕё наиболее успешными с коммерческой стороны фильмами стали «Малефисента» (сборы в мировом прокате — 758 миллионов долларов США), «Мистер и миссис Смит» (сборы в мировом прокате — 478 миллионов долларов США), «Особо опасен» (341 миллион долларов США), «Солт» (293 миллиона долларов США), а также «Турист» (278 миллионов долларов США), «Лара Крофт: Расхитительница гробниц» (274 миллиона долларов США) и картина с участием Николаса Кейджа «Угнать за 60 секунд» (237 миллионов долларов США).",
    "time_create": "2021-12-06T09:21:35.384559+03:00",
    "time_update": "2021-12-06T09:21:35.384559+03:00",
    "is_published": true,
    "cat": 1
  },
  {
    "id": 2,
    "title": "Дженнифер Лоуренс",
    "content": "Дженнифер Шрейдер Лоуренс (англ. Jennifer Shrader Lawrence]; род. 15 августа 1990, Индиан-Хиллз, Кентукки, США) — американская актриса кино и телевидения. Лауреат премии «Оскар» (2013), трёх премий «Золотой глобус» (2013, 2014, 2016), премии BAFTA (2014), двух «Премий Гильдии киноактёров США» (2013, 2014) и премии «Сатурн» (2013).\r\n\r\nДженнифер Лоуренс начала актёрскую карьеру в 2006 году, сыграв в телепроекте «Городская компания». Свою первую главную роль она исполнила в драме «Дом покера (англ.)русск.». Признание в актёрской среде она получила после роли Тиффани в комедийной драме «Мой парень — псих», а массовому зрителю стала известна как молодая Мистик в фантастических фильмах «Люди Икс: Первый класс» (2012), «Люди Икс: Дни минувшего будущего» (2014) и «Люди Икс: Апокалипсис» (2016). Наибольшую популярность актрисе принесла роль Китнисс Эвердин в экранизации книжной трилогии «Голодные игры».\r\n\r\nВ 2011 году Дженнифер в двадцатилетнем возрасте была номинирована на премию «Оскар» и «Золотой глобус» в категориях «Лучшая женская роль» и «Лучшая женская роль в драматическом фильме» за исполнение роли Ри Долли в драме «Зимняя кость», но обе статуэтки тогда выиграла Натали Портман. В периоде между 2012 и 2013 годами Дженнифер получила множество наград за роль в комедийной драме «Мой парень — псих», в их числе «Оскар», «Золотой глобус» и Премия Гильдии киноактёров США в номинациях «Лучшая женская роль». Актёрская работа Лоуренс в криминальной трагикомедии «Афера по-американски» принесла ей первую статуэтку BAFTA (2014), второй «Золотой глобус» (2014) и номинации на «Оскар» и «Премию Гильдии киноактёров США». Самая высокооплачиваемая актриса 2014—2015 года по версии журнала Forbes.",
    "time_create": "2021-12-06T09:22:02.064606+03:00",
    "time_update": "2021-12-06T09:22:02.064606+03:00",
    "is_published": true,
    "cat": 1
  },
  {
    "id": 3,
    "title": "Ариана Гранде",
    "content": "Ариана Гранде-Бутера[3] (англ. Ariana Grande-Butera; род. 26 июня 1993, Бока-Ратон, Флорида, США[1][4]) — американская певица, актриса, автор песен, музыкальный продюсер[5][6], обладательница премии «Грэмми»[7].\r\n\r\nПрофессиональную карьеру в шоу-бизнесе Ариана Гранде начала в 2008 году в бродвейском мюзикле «13». В 2009 году она получила роль Кэт Валентайн в телевизионном сериале «Виктория-победительница» на канале Nickelodeon, потом продолжила играть её же в телесериале «Сэм и Кэт», выходившем в 2013—2014 годах. Ариана также принимала участие в записи саундтреков и озвучивании мультфильмов (в частности, мультсериала «Клуб Винкс»). В 2015 году она вернулась на телеэкраны с эпизодической ролью Сони Херфман в сериале «Королевы крика».\r\n\r\nМузыкальная карьера Арианы началась в 2011 году с записи саундтрека к сериалу «Виктория-победительница». В том же году она заключила контракт со звукозаписывающей компанией Republic Records. В 2013 году у неё вышел дебютный альбом Yours Truly, дебютировавший на первом месте в американском чарте Billboard 200. Песня «The Way» с этого альбома занимала уверенные позиции в первой десятке чарта Billboard Hot 100 и была положительно встречена музыкальными критиками.\r\n\r\nСледующий альбом Арианы Гранде, My Everything (2014), также дебютировал на первой позиции в американском чарте. Альбом имел мировой успех благодаря хитам «Problem», «Break Free», «Bang Bang» и «Love Me Harder». C несколькими песнями с него певица 34 недели непрерывно находилась в первой десятке американского чарта Billboard Hot 100. В 2015 году она отправилась в мировой тур в поддержку этого альбома, озаглавленный The Honeymoon Tour.\r\n\r\nВ 2016 году Ариана выпустила альбом Dangerous Woman (2016, 2-е место в США), клип на сингл «Side To Side» с данного альбома имеет более миллиарда просмотров на YouTube. В следующем году певица отправилась в мировое турне Dangerous Woman Tour. 22 мая 2017 года на концерте Арианы в Манчестере произошёл теракт. Гранде приостановила тур и устроила благотворительный концерт, чтобы собрать деньги для пострадавших в теракте.\r\n\r\nСледующий альбом — Sweetener — вышел в 2018 году и занял 1-е место в США. Альбом был признан Американской академией звукозаписи лучшим поп-альбомом 2018 года. Через несколько месяцев после релиза альбома Sweetener, Ариана Гранде выпустила альбом Thank U, Next (2019), который так же занял первую строчку американского чарта Billboard 200. Альбом повторил рекорд группы The Beatles: три сингла из Thank U, Next («7 Rings», «Break Up With Your Girlfriend, I’m Bored» и «Thank U, Next») заняли первые три позиции чарта Billboard Hot 100 одновременно. Песни Арианы Гранде часто бьют рекорды на стриминг-сервисе Spotify. 18 марта 2019 певица отправилась в мировое турне Sweetener World Tour в поддержку двух своих последних альбомов.",
    "time_create": "2021-12-06T09:22:21.385416+03:00",
    "time_update": "2021-12-06T09:22:21.385416+03:00",
    "is_published": true,
    "cat": 2
  },
  {
    "id": 4,
    "title": "Бейонсе",
    "content": "Бейонсе Жизель Ноулз-Картер (англ. Beyonce Giselle Knowles-Carter; род. 4 сентября 1981[7], Хьюстон), более известная просто как Бейо?нсе (произносится /bi?j?nse?/ би-йон-сей) — американская певица в стиле R’n’B, актриса, танцовщица, музыкальный продюсер. Будучи ребёнком, участвовала в разных вокальных и танцевальных конкурсах, принимала участие в школьной художественной самодеятельности. Ноулз прославилась в конце 1990-х годов, будучи солисткой женской R&B-группы Destiny’s Child.\r\n\r\nВо время раскола Destiny’s Child Ноулз выпустила свой дебютный сольный альбом Dangerously in Love (2003), в который вошли такие хиты, как «Crazy in Love» и «Baby Boy». Пластинка стала одним из самых успешных релизов 2003 года. За этот альбом Ноулз получила рекордные пять «Грэмми»[8][9]. В 2006 году, спустя год после окончательного развала группы, Бейонсе выпустила альбом B’Day, который занял первую строчку в чарте Billboard 200 и включал хиты «Deja Vu», «Irreplaceable» и «Beautiful Liar». Её третий сольный альбом I Am… Sasha Fierce, выпущенный в ноябре 2008 года, включал хит «Single Ladies (Put a Ring on It)». Альбом и его синглы одержали победу в шести номинациях «Грэмми», что стало рекордом для певицы[10][11][12]. Бейонсе — одна из самых успешных артисток «Грэмми», получившая 20 наград, 17 из которых получены ею как сольной исполнительницей и три — как участницей группы Destiny’s Child.\r\n\r\nНоулз начала актёрскую карьеру в 2001 году, появившись в музыкальном фильме «Кармен: Хип-хопера». В 2006 году она снялась в главной роли в фильме-адаптации бродвейского мюзикла 1981 года «Девушки мечты», за который она была номинирована на «Золотой глобус». В 2004 году Ноулз запустила семейную линию одежды House of Dereon и подписала контракт с такими брендами, как Pepsi, Tommy Hilfiger, Armani и L’Oreal. В 2010 году журнал Forbes поместил Ноулз на вторую строку в списке 100 самых влиятельных знаменитостей в мире[13][14]; она также была включена в список самых влиятельных музыкантов в мире[15]. Журнал Time включил Ноулз в список 100 самых влиятельных людей мира[16].\r\n\r\nНоулз заняла пятое место в Hot 100 синглов номер один как сольная исполнительница и четвёртое место с Destiny’s Child, как сольная артистка она распродала более 35 миллионов альбомов и синглов в США[17]. Согласно данным звукозаписывающей компании Sony, её общие продажи записей в составе группы превзошли 100 миллионов[18]. 11 декабря 2009 года Billboard объявил Ноулз самой успешной исполнительницей 2000-х годов и главной радио-исполнительницей десятилетия[19]. В феврале 2010 RIAA зарегистрировал её как артистку с самым большим количеством сертификатов RIAA за десятилетие[20][21]. В 2019 году вошла в список самых высокооплачиваемых музыкантов по версии журнала Forbes. Заработанная сумма составила $81 млн, это шестое место в рейтинге[22], которое певица разделила с Jay-Z.",
    "time_create": "2021-12-06T09:22:36.527751+03:00",
    "time_update": "2021-12-06T09:22:36.527751+03:00",
    "is_published": true,
    "cat": 2
  }
]
"""
test_json_1 = """
{
    "id": 1,
    "title": "Анджелина Джоли",
    "content": "Анджелина Джоли (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.\r\n\r\nОбладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».\r\n\r\nДебютировала в кино в 1982 году, сыграв роль в комедийном фильме «В поисках выхода» (где снимались также её отец и мать)[8], однако известность получила после того, как сыграла героиню видеоигр Лару Крофт в фильмах «Лара Крофт: Расхитительница гробниц» и «Лара Крофт: Расхитительница гробниц 2 — Колыбель жизни».\r\n\r\nВ 2009, 2011 и 2013 годах по версии журнала Forbes Джоли была названа самой высокооплачиваемой актрисой Голливуда[9][10].\r\n\r\nЕё наиболее успешными с коммерческой стороны фильмами стали «Малефисента» (сборы в мировом прокате — 758 миллионов долларов США), «Мистер и миссис Смит» (сборы в мировом прокате — 478 миллионов долларов США), «Особо опасен» (341 миллион долларов США), «Солт» (293 миллиона долларов США), а также «Турист» (278 миллионов долларов США), «Лара Крофт: Расхитительница гробниц» (274 миллиона долларов США) и картина с участием Николаса Кейджа «Угнать за 60 секунд» (237 миллионов долларов США).",
    "time_create": "2021-12-06T09:21:35.384559+03:00",
    "time_update": "2021-12-06T09:21:35.384559+03:00",
    "is_published": true,
    "cat": 1
  }
"""
# print(type(test_json_1))
data = json.loads(test_json, strict=False)
djoli = Updating(data[0])
print(djoli.title)
