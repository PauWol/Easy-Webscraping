from bs4 import BeautifulSoup
import requests , webbrowser ,os

class Website(object):
    def __init__(self,url):
        self.url = url
    
    def request(self):
        self.response = requests.get(self.url)
    
    def html_parser(self):
        soup = BeautifulSoup(self.response.content, "html.parser")
        self.photos = soup.find_all("img",src=True)
    
    def print_result(self):
        for o in self.photos:
            print(o)

class Html(object):
    def __init__(self,url):
        self.file_url = url
    
    def write_file(self,val):
        with open(self.file_url, "a") as f:
            f.write("\n".join([str(photo) for photo in val]))
            f.close()
    def open_file(self):
        if os.path.isfile(self.file_url):
            webbrowser.open_new_tab('file://' + os.path.realpath(self.file_url))

def main():
    url = input('Enter url of website:')
    website = Website(url)
    website.request()
    website.html_parser()
    html = Html('./index.html')
    html.write_file(website.photos)
    html.open_file()

if __name__ == '__main__':
    main()
    input('Type ENTER to exit')