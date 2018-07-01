import requests
import json
class Base(object):
    def __init__(self):
        self.header=""
        self.data=""
        self.method=''
        self.url=""
    def GetContentObject(self):
        s = requests.session()
        s.keep_alive = False
        if self.method=='get':
            with s.get(self.url, headers=self.header,data=self.data,timeout=300) as f:
                r =f
        elif self.method=='post':
            with s.post(self.url, headers=self.header,data=self.data,timeout=300) as f :
                r =f
        elif self.method == 'put':
            with s.put(self.url, headers=self.header, data=self.data,timeout=300) as f:
                r = f
        elif self.method == 'delete':
            with s.delete(self.url, headers=self.header, data=self.data,timeout=300) as f:
                r = f
        else:
            r='bad run'
        return  r
    def GetContent(self):
        return  self.GetContentObject().text
    def GetContentAsJson(self):
        return  json.loads(self.GetContent())
    #从返回的Json中读取需要的内容
    def GetItem(self,name):
        content=json.loads(self.GetContent())
        return content[name]