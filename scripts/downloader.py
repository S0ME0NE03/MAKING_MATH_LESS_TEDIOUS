import urllib.request
def download(url, filename):
  urllib.request.urlretrieve("url","filename")
if ___name___ == ___main___:
  url = input("Input a url:\n")
  filename = input("What should the file be named?\n")
  download(url, filename)
