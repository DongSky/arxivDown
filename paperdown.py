import urllib
import urllib.parse
import urllib.request
def paperDown(arxiv_id):
    download_link="https://arxiv.org/pdf/"+str(arxiv_id)+".pdf"
    request=urllib.request.Request(download_link)
    request.add_header("User-Agent","Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36")
    get=urllib.request.urlopen(request).read()
    print(len(get))
    with open(str(arxiv_id)+".pdf","wb") as f:
        f.write(get)
        f.close()
if __name__=="__main__":
    paperDown("1704.00028")
