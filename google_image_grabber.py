from icrawler.builtin import BaiduImageCrawler 
from icrawler.builtin import BingImageCrawler 
from icrawler.builtin import GoogleImageCrawler 
"""
parser_threads：解析器线程数目，最大为cpu数目
downloader_threads：下载线程数目，最大为cpu数目
storage：存储地址，使用字典格式。key为root_dir
keyword:浏览器搜索框输入的关键词
max_num:最大下载图片数目
"""

#google image 爬虫
google_storage = {'root_dir': '/mmm/xxx/zzz/yyy/your_folder'}
google_crawler = GoogleImageCrawler(parser_threads=4, 
                                   downloader_threads=4, 
                                   storage=google_storage)
google_crawler.crawl(keyword='beauty', 
                     max_num=200)
