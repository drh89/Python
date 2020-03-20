# Exercise 06

# Create a module containing a class with the following methods:
# import webget
import pandas as pd
from requests import get  # to make GET request
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
import multiprocessing
import requests


class NotFoundException(ValueError):
    """Raised when the url returns value 404"""

    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)


class Exercise6_1:
    """download books"""
    # 1. init(self, url_list)
    def __init__(self, url_list):
        self.url_list = url_list
        self.filenames = []
        self.index = 0

    # 4. iter() returns an iterator
    def __iter__(self):
        return self

    # 5. next() returns each of the downloaded files
    def __next__(self):
        if self.index >= len(self.filenames):
            raise StopIteration

        with open(self.filenames[self.index], "r", encoding="utf8", errors='ignore') as file:
            self.index += 1
            str = ""
            return str.join(file.readlines())

    # 2. download(url, filename)

    def download(self, url, filename):
        """download books and raises NotFoundException when url returns 404"""
        print("url", url)
        print("filename", filename)
        # open in binary mode
        with open(filename, "wb") as file:
            # get request
            try:
                r = requests.get(url)
                if r.status_code == 404:
                    raise NotFoundException(
                        "URL: ", url, " is not working. Status code 404")
                # write to file
                file.write(r.content)
                print("file downloaded")
            except ConnectionError as ex:
                print(ex)
            except NotFoundException as ex:
                print(ex)
            except Exception as ex:
                print(ex)

    # 3. multi_download(url_list)
    def multi_download(self, url_list):
        """uses threads to download multiple urls as text and stores filenames as a property"""
        workers = 4
        with ThreadPoolExecutor(workers) as ex:
            urls = [url_list[x] for x in range(len(url_list))]
            self.filenames = [str(y)+".txt" for y in range(len(url_list))]
            ex.map(self.download, urls, self.filenames)
        return self.filenames

    # 6. filelist_generator(url_list)
    def filelist_generator(self):
        """returns a generator to loop through the filenames"""
        for filename in self.filenames:
            yield filename

    # 7. avg_vowels(text)
    def avg_vowels(self, text):
        """a rough estimate on readability returns average number of vowels in the words of the text"""
        val = 0
        if text:
            text = text.replace("\n", "")
            text = text.replace(",", "")
            text = text.replace("'", "")
            it = (map(text.lower().count, "aeiouyæøå"))
            word_count = len(text.split(" "))
            it_sum = 0
            for x in it:
                it_sum += +x
            if word_count == 0:
                return 0
            val = round(it_sum/word_count, 2)
        print("avg vowels returned", val)
        return val

    # 8. hardest_read()
    def hardest_read(self, it):
        """ returns the filename of the text with the highest vowel score(use all the cpu cores on the computer for this work."""
        workers = multiprocessing.cpu_count()
        # highest_avg=0
        texts = []
        while True:
            try:
                texts.append(it.__next__())
            except StopIteration:
                break

        with ProcessPoolExecutor(workers) as ex:
            res = ex.map(self.avg_vowels, texts)
        result = dict(zip([filename for filename in self.filenames], [avg for avg in list(res)]))
        maxi = max(result, key=result.get) # finding key with max value
        return maxi


if __name__ == '__main__':

    # iterable = Exercise6_1(["url1", "Url2"])

    # my_iterator = iter(iterable)
    # while True:
    #     try:
    #         # get the next item
    #         element = next(my_iterator)
    #         print(element)
    #         # do something with element
    #     except StopIteration:
    #         # if StopIteration is raised, break from loop
    #         break

    filing = Exercise6_1([])

    url = "https://www.gutenberg.org/files/1342/1342-0.txt"
    url2 = "https://www.gutenberg.org/files/1343/1343-0.txt"
    url3 = "https://www.gutenberg.org/files/1344/1344-0.txt"

    # url_list = [url]
    url_list = [url, url2, url3]
    reslist = filing.multi_download(url_list)
    # print("list of filenames: ", reslist)
    # texts = [x for x in next(iter(filing))]
    # print(texts)
    try:
        print("Highest average is in ", filing.hardest_read(iter(filing)))
    except OSError as ex:
        print(ex)
    # print(f)
