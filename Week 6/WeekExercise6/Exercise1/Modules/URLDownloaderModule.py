import wget
import os
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import concurrent.futures
import concurrent.futures.process
import multiprocessing
from urllib.parse import urlparse


# Create a module containing a class with the following methods:
# 1. init(self, url_list)
# 2. download(url,filename) raises NotFoundException when url returns 404
# 3. multi_download() uses threads to download multiple urls as text and stores filenames as a property
# 4. iter() returns an iterator
# 5. next() returns the next filename (and stops when there are no more)
# 6. urllist_generator() returns a generator to loop through the urls
# 7. avg_vowels(text) - a rough estimate on readability returns average number of vowels in the words of the text
# 8. hardest_read() returns the filename of the text with the highest vowel score (use all the cpu cores on the computer
# for this work.

# https://www.geeksforgeeks.org/python-map-function/
# https://www.geeksforgeeks.org/python-dictionary/
# https://www.geeksforgeeks.org/zip-in-python/
# https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/

class NotFoundException(ValueError):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)


class URLDownloader:

    # 1.

    def __init__(self, url_list):
        self.url_list = url_list
        self.downloaded_files = []
        self.texts = []

    # 2.

    # Works

    def download(self, url, name=None):
        try:
            filename = os.path.basename(urlparse(url).path)

            if name:
                filename = name

            directory = 'Downloaded_Files'

            full_file_path = directory + '/' + filename

            file_exist = os.path.isfile(full_file_path)

            if file_exist:
                print(f'File: {filename} already exist in: {directory}, aborting download')
            else:
                return wget.download(url, out=full_file_path)
        except:
            raise NotFoundException('Error: File not found')

    # 3.

    # Works

    def multi_download(self):

        with ThreadPoolExecutor(os.cpu_count()) as pool:
            pool_of_urls = {pool.submit(self.download, url): url for url in self.url_list}
            for job in concurrent.futures.as_completed(pool_of_urls):
                url = pool_of_urls[job]
                try:
                    job.result()
                except Exception as e:
                    print(f'An error occurred: {url, e}')

    # 4.

    def __iter__(self):
        self.index = 0
        return self

    # 5.

    def __next__(self):
        self.index += 1
        if self.index < len(self.downloaded_files):
            return self.downloaded_files[self.index]
        else:
            raise StopIteration

    # 6.

    def url_list_generator(self):
        for url in self.downloaded_files:
            # https://www.geeksforgeeks.org/use-yield-keyword-instead-return-keyword-python/
            yield url

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
