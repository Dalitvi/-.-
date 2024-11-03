class Downloader:
    def download(self, url):
        raise NotImplementedError("Subclasses must implement this method")

class SimpleDownloader(Downloader):
    def download(self, url):
        print(f"Downloading -> {url}")
        return f"Downloaded content from -> {url}"

class CachedDownloader(Downloader):
    def __init__(self, simple_downloader):
        self._simple_downloader = simple_downloader
        self._cache = {}

    def download(self, url):
        if url in self._cache:
            print(f"Fetching from cache -> {url}")
            return self._cache[url]
        else:
            data = self._simple_downloader.download(url)
            self._cache[url] = data
            return data

def main():
    downloader = CachedDownloader(SimpleDownloader())

    data1 = downloader.download("https://Test.com/File1")
    print(data1 + "\n")

    data2 = downloader.download("https://Test.com/File2")
    print(data2 + "\n")

    data3 = downloader.download("https://Test.com/File1")
    print(data3 + "\n")

    data4 = downloader.download("https://Test.com/File2")
    print(data4 + "\n")

    data5 = downloader.download("https://Test.com/File3")
    print(data5 + "\n")

if __name__ == "__main__":
    main()
