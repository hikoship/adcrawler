# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import urllib2, codecs
from bs4 import BeautifulSoup
from collections import namedtuple
import logging


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, majorFilter):
        self.majorFilter = majorFilter

    def get(self):
        #items = ["Item 1", "Item 2", "Item 3"]
        #self.render("template.html", title="My title", items=items)

        Notice = namedtuple('Notice', [
            'threadID',
            'term',
            'degree',
            'res',
            'major',
            'appSchool',
            'date',
            'toefl',
            'gre',
            'bsMajor',
            'bsGpa',
            'bsSchool',
            'title',
            'postDate',
            'isNew'
            ], verbose=False)

        bsDict = {
            None: '',
            u'海本': u'海本',
            u'本科：北大，清华，科大，中科院，特色学校牛专业': u'清北科',
            u'本科：南大，浙大，复旦，上交': u'南浙复交',
            u'本科Top15 211': u'Top 15',
            u'本科Top30 211': u'Top 30',
            u'本科其他211': u'其他211',
            u'本科非211': u'非211',
            }

        #userTerm = '[' + '16Fall'
        #userDegree = 'MS'
        notices = []

        header = { 'Use-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6' }

        url = "http://www.1point3acres.com/bbs/forum.php?mod=forumdisplay&fid=82&filter=author&orderby=dateline&sortid=164"
        req = urllib2.Request(url, headers = header)
        content = urllib2.urlopen(req).read()

        soup = BeautifulSoup(content, 'html.parser')
        for thread in soup.find_all('tbody'):
            if thread['id'][0] != 'n':
                # filter normal thread
                continue

            threadID = thread['id'].split('normalthread_')[1]
            fonts = thread.find_all('font')

            major = fonts[3].string
            if self.majorFilter != '' and major != self.majorFilter:
                continue
            term = fonts[0].string[1:]
            degree = fonts[1].string
            res = fonts[2].b.string
            appSchool = fonts[4].string
            date = fonts[5].string
            toefl = fonts[6].b.next_sibling.string[2:]
            gre = fonts[7].b.next_sibling.string[2:]
            bsMajor = fonts[8].string
            if bsMajor is None:
                bsMajor = ''

            bsGpa = fonts[9].string[1:-1]
            bsSchool = bsDict[fonts[10].string]
            title = thread.find_all('a')[3].string
            postDate = thread.select('em > span > span')[0].string
            isNew = True if postDate[-1] == u'前' and postDate[-2] != u'天' else False

            notices.append(Notice(
                int(threadID),
                term,
                degree,
                res,
                major,
                appSchool,
                date,
                toefl,
                gre,
                bsMajor,
                bsGpa,
                bsSchool,
                title,
                postDate,
                isNew
            ))

        self.render("template.html", title="My title", items=notices)


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler, dict(majorFilter='')),
        (r"/cs", MainHandler, dict(majorFilter='CS')),
        (r"/mis", MainHandler, dict(majorFilter='MIS')),
        (r"/ee", MainHandler, dict(majorFilter='EE')),
        (r"/bme", MainHandler, dict(majorFilter='BME')),
        (r"/me", MainHandler, dict(majorFilter='ME')),
        (r"/ieor", MainHandler, dict(majorFilter='IEOR')),
        (r"/stat", MainHandler, dict(majorFilter='Stat/Biostat')),
        (r"/bioinfo", MainHandler, dict(majorFilter='BioInfo')),
        (r"/mfe", MainHandler, dict(majorFilter='MFE/Fin/FinMath')),
        (r"/econ", MainHandler, dict(majorFilter='Econ/Biz')),
        (r"/math", MainHandler, dict(majorFilter='Math/AppliedMath')),
        (r"/physics", MainHandler, dict(majorFilter='Physics')),
        (r"/accounting", MainHandler, dict(majorFilter='Accounting')),
        (r"/chem", MainHandler, dict(majorFilter='Chem/CEng')),
        (r"/material", MainHandler, dict(majorFilter='Material')),
        (r"/liberalarts", MainHandler, dict(majorFilter='LiberalArts')),
        (r"/civileng", MainHandler, dict(majorFilter='CivilEng')),
        (r"/envir", MainHandler, dict(majorFilter='Envir')),
        (r"/bio", MainHandler, dict(majorFilter='Bio')),
        (r"/earth", MainHandler, dict(majorFilter='Earth')),
        (r"/edu", MainHandler, dict(majorFilter='Edu')),
        (r"/other", MainHandler, dict(majorFilter='Other')),
        (r"/cis", MainHandler, dict(majorFilter='CIS')),
        (r"/ce", MainHandler, dict(majorFilter='CE')),
        (r"/datascience", MainHandler, dict(majorFilter='DataScience/Analytics')),
    ])

if __name__ == "__main__":
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S', filename='post.log',level=logging.INFO)
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
