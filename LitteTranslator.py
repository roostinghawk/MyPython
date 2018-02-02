from urllib.request import *
from urllib.parse import *
import requests

from tkinter import *


class LittleTranslator:
    def __init__(self, root):
        root.geometry('600x400')
        root.title("小小翻译助手")

        t1 = Text(root, width = 50, height = 10)
        t1.grid(row=0,column=0, padx=(20,10), pady=(10,10))
        lb1 = Label(root, text="", width=50, height=10, anchor="w")
        lb1.grid(row=2,column=0, padx=(20,10),pady=(10,10))

        # translator = self.translate(t1, )
        btn = Button(root, text="翻译", fg="blue", command=lambda : self.translate(t1, lb1), width=10, height=1)
        btn.grid(row=1, column = 0, padx=(20,10),pady=(10,10))

    def translate(self, t1,lb1):
        fromText = t1.get("1.0",END).strip('\n')
        body = {}
        body["from"] = "en"
        body["to"] = "zh"
        body["type"] = "AUTO"
        body["doctype"] = "json"
        body["query"] = fromText
        body["transtype"] = "translang"
        body["simple_means_flag"] = "3"
        body["sign"] = "431039.159886"
        body["token"] = "9632ba802c570dc94aa3ea50c5ca84b9"
        data = urlencode(body).encode("utf-8")

        # req = Request("http://fanyi.baidu.com/v2transapi", method = "POST", data = data)
        # req.add_header("Host", "fanyi.baidu.com")
        # req.add_header("Origin", "http://fanyi.baidu.com")
        # req.add_header("Pragma", "no-cache")
        # req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36")
        # req.add_header("X-Requested-With", "XMLHttpRequest")
        # req.add_header("Content-Type", "application/x-www-form-urlencoded; charset=UTF-8")
        headers = {}
        headers["Host"] = "fanyi.baidu.com"
        headers["Origin"] = "http://fanyi.baidu.com"
        headers["Referer"] = "http://fanyi.baidu.com/"
        headers["Pragma"] = "no-cache"
        headers["Accept-Language"] = "en-US,en;q=0.9"
        headers["Accept-Encoding"] = "gzip, deflate"
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
        headers["X-Requested-With"] = "XMLHttpRequest"
        headers["Content-Type"] = "application/x-www-form-urlencoded; charset=UTF-8"

        response = requests.post("http://fanyi.baidu.com/v2transapi", data=data, headers=headers)


        # response = urlopen(req)
        # html = response.read().decode("utf-8")
        html = response.text
        result = html
        lb1.config(text=result)
