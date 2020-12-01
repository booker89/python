import urllib.request as req
url="https://www.youtube.com/c/%E5%BD%AD%E5%BD%AD%E7%9A%84%E8%AA%B2%E7%A8%8B/playlists" 
request=req.Request(url,headers={
  "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36"
})
with req.urlopen(request) as response:
    data=response.read().decode("utf-8")


import bs4
root=bs4.BeautifulSoup(data,"html.parser")
# print(data)
# # print(root.title.string)
sub=root.find("a", class_="yt-simple-endpoint")
# print(root.find("div", {"class": "title"}))
print(sub)
# ---------------

