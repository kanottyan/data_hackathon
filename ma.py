#! /usr/bin/python
# -*- coding: utf-8 -*-

from urllib import urlopen
import json
import urllib
import time

import MeCab

myMecab = MeCab.Tagger ("-Ochasen")
# sys.setdefaultencoding('utf-8')

# query = u'カレー'
# .encode('ascii')
# query = urllib.quote(query.encode('utf-8'))

# for page in range(1, 100):
    # myPage = str(page)
    #src = urlopen('https://app.rakuten.co.jp/services/api/IchibaItem/Search/20140222?format=json&keyword=' + query + '&applicationId=1055895049225824262&pages=' + urllib.quote(myPage.encode('utf-8'))).read()
src = urlopen("http://dac2.snnm.net/api/xsearch?keyword=%E5%B0%B1%E6%B4%BB&fields=body&application_id=168cb0d447bb493eba07555973b3fc70").read()

    # time.sleep(1)

# http://api.gnavi.co.jp/ver1/RestSearchAPI/?keyid=8929cbba7321fa9abab89f4671718354&pref=PREF13&sort=1&freeword=%E3%82%AB%E3%83%AC%E3%83%BC
    # if page == 4:
        # continue
    # print page

myJson = json.loads(src)
# import pdb; pdb.set_trace()
items = myJson['hits']

# myStr = ''

for myArray in items:

            # import pdb; pdb.set_trace()
            myContent = myArray['body'].encode('utf-8')
            myKijiId = myArray['news_id'].encode('utf-8')

            txt_wakati = myMecab.parse(myContent)

            myPublishDate = myArray['display_time'].encode('utf-8')

            wakati_list = txt_wakati.strip("\r\n").split()

            myTitle = myArray['title'].encode('utf-8')

            myIsCook = "0"
            if "クックパッド" in wakati_list: myIsCook = "1"
            myIsNikkei = "0"
            if "日経" in wakati_list: myIsNikkei = "1"

            f = open('kijizennpann.csv', 'w') # 書き込みモードで開く
            f.write(myKijiId+ ","+ myContent+","+ myTitle+","+myPublishDate+","+myIsCook+","+myIsNikkei ) # 引数の文字列をファイルに書き込む
            f.close() # ファイルを閉じる

            # print myMessage
            # myStr = myStr+"\n"+myMessage




# for rest in rests:
    # print rest['tel']
    # print rest['name']
    # myImage = rest['image_url']
    # for myShopUrl in myImage.keys():
        # print myImage[myShopUrl]


