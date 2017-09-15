import os
import urllib
import urllib.parse
import urllib.request
import paperdown
import requests

def paperSearch(keywords):
    search_query=" ".join(keywords)
    params={
        "query":search_query,
        "searchtype":"all"
    }
    headers={
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
        "Referer":"https://arxiv.org/"
    }
    request_url="https://arxiv.org/search"
    response=requests.post(request_url,headers=headers,data=params)
    f=open("test.html","wb")
    f.write(response.content)
    f.close()
    pass
if __name__=="__main__":
    paperSearch(["reinforcement","learning"])
