import wget
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

#Create a module containing a class with the following methods:
# 1. init(self, url_list)
# 2. download(url,filename) raises NotFoundException when url returns 404
# 3. multi_download() uses threads to download multiple urls as text and stores filenames as a property
# 4. iter() returns an iterator
# 5. next() returns the next filename (and stops when there are no more)
# 6. urllist_generator() returns a generator to loop through the urls
# 7. avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
# 8. hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.

class NotFoundException(ValueError):
    def __init__(self, *args):
        ValueError.__init__(self, *args)

class URLDownloader:

    # 1.

    def __init__(self, url_list):
        self.url_list = url_list
        self.downloaded_files = []

    # 2.

    def download(self, url, filename):
        try:
            return wget.download(url, filename)
        except:
            raise NotFoundException('Error: File not found')

    # 3.

    def multi_download(self):
        self.downloaded_files = self.multi_thread(self.download(), self.url_list)

    def multi_thread(self, method, jobs, workers=4):
        with ThreadPoolExecutor(workers) as pool:
            result = pool.map()
        return list(result)

    # 4.

    def __iter__(self):
        return self

    # 5.

    def __next__(self):

    # 6.

    def url_list_genrator(self):

    # 7.

    def avg_amount_vowels(self, text):

    # 8.

    def hardest_read(self   ):