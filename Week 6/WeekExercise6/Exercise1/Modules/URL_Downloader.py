import wget
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

# Create a module containing a class with the following methods:
# 1. init(self, url_list)
# 2. download(url,filename) raises NotFoundException when url returns 404
# 3. multi_download() uses threads to download multiple urls as text and stores filenames as a property
# 4. iter() returns an iterator
# 5. next() returns the next filename (and stops when there are no more)
# 6. urllist_generator() returns a generator to loop through the urls
# 7. avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
# 8. hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer for this work.

#https://www.geeksforgeeks.org/python-map-function/
#https://www.geeksforgeeks.org/python-dictionary/
#https://www.geeksforgeeks.org/zip-in-python/

class NotFoundException(ValueError):
    def __init__(self, *args):
        ValueError.__init__(self, *args)


class URLDownloader:

    # 1.

    def __init__(self, url_list):
        self.url_list = url_list
        self.downloaded_files = []
        self.texts = []

    # 2.

    def download(self, url, filename):
        try:
            return wget.download(url, filename)
        except:
            raise NotFoundException('Error: File not found')

    # 3.

    def multi_download(self):
        self.downloaded_files = self.multi_thread_list(self.download(), self.url_list)

    def multi_thread_list(self, method, jobs):
        with ThreadPoolExecutor(os.cpu_count()) as pool:
            result = pool.map()
        return list(result)

    # 4.

    def __iter__(self):
        self.index = 0
        return self

    # 5.

    def __next__(self):
        index = self.index
        self.index += 1
        if index < len(self.downloaded_files):
            return self.downloaded_files[index]
        else:
            raise StopIteration

    # 6.

    def url_list_generator(self):
        for file in self.downloaded_files:
            # https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
            yield file

    # 7.

    def avg_amount_vowels(self, text):
        return sum([*map(text.lower().count, 'aeiYouæøå')]) / len(text.split())

    # 8.

    def hardest_read(self):
        for filename in self.downloaded_files:
            with open(filename, 'rb') as file:
                texts = self.texts.append(file.read().decode())
        return {filename: vowel_score for filename, vowel_score in sorted(self.multi_thread_dictionary(
            self.avg_amount_vowels, texts, self.downloaded_files), key=lambda item: item[1], reverse=True)}


    def multi_thread_dictionary(self, method, jobs, names, workers=os.cpu_count()):
        with ProcessPoolExecutor(workers) as pool:
            result = pool.map(method, jobs)
        return dict(zip(names, result))
