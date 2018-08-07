import feedparser
from urllib.parse import urlencode
from mail_sender import MailSender


class RssNewsParser:

    @staticmethod
    def news_rss_parser(query):

        url = "http://newssearch.naver.com/search.naver?where=rss&"
        request_param = urlencode({'query': query})
        naver_news_rss_path = url + request_param

        parser = feedparser.parse(naver_news_rss_path)

        mail_line = "<font size='3px'><b>네이버 클라우드 플랫폼 뉴스</b></font><br/><br/>"

        for item in parser.entries:
            mail_line += "[" + item.get('authors')[0].get('name') + "] " + "<a href='" + item.get('link') + "'>" +\
                         item.get('title') + "</a>" + " <br/>"

        mail_line += "<br/><br/>" \
                     "<img src='https://static.navercorp.com/static/site/connect2/user/connect/signature/nbp_ncp.png'>"\
                     "<br><br>"

        print(mail_line)

        return mail_line


if __name__ == '__main__':
    RssNewsParser().news_rss_parser('NCP+네이버클라우드플랫폼')