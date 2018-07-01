from Base.Base import Base
from Base import authenticate
import base64
import  json

class get_bucket_list(Base):
    def __init__(self):
        super(get_bucket_list,self).__init__()
        self.auth = authenticate.authenticate().get_access_token
        self.header = {'Authorization': self.auth,'Content-Type': 'application/json'}
        self.method = 'get'
        self.url = 'https://developer.api.autodesk.com/oss/v2/buckets'
    def result(self):
        return self.GetContent()



class upload_file_to_bucket(Base):
    def __init__(self,bucketname,filepath,filename):
        super(upload_file_to_bucket,self).__init__()
        self.bucketname=bucketname
        self.filename=filename
        with open(filepath, 'rb') as f:
            self.data = f.read()
        print(self.data.__len__())
        self.url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s' % (self.bucketname, self.filename)
        self.auth = authenticate.authenticate().get_access_token
        self.header = {
            'Authorization': self.auth,
            'Content-Type': 'application/octet-stream',
        }
        self.method = 'put'

    def result(self):
        return self.GetContent()

class create_bucket(Base):
    def __init__(self,bucketname,policyKey='transient'):
        super(create_bucket,self).__init__()
        _data = {'bucketKey': bucketname, 'policyKey':policyKey}
        self.data=json.dumps(_data)
        self.auth = authenticate.authenticate().get_access_token
        self.header ={'Authorization': self.auth,'Content-Type': 'application/json'}
        self.method = 'post'
        self.url = 'https://developer.api.autodesk.com/oss/v2/buckets'

    def result(self):
        return self.GetContent()

class get_object_from_bucket(Base):
    def __init__(self,bucketname,auth):
        super(get_object_from_bucket,self).__init__()
        self.url='https://developer.api.autodesk.com/oss/v2/buckets/%s/objects' % (bucketname)
        self.auth =auth
        self.header= {
            'Authorization': self.auth,
            'Content-Type': 'application/json'
        }
        self.method = 'get'
    def result(self):
        return self.GetContent()

    def list_all_urn(self):
        c = self.GetItem('items')
        all=[]
        for i in c:
            objectId=i['objectId'].encode(encoding="utf-8")
            urn = base64.b64encode(objectId).decode('utf-8').strip("=").encode('utf-8')
            all.append(urn)
        return all

    def get_urn(self,objectKey):
        c = self.GetItem('items')
        b='No This ObjectKey'
        for i in c:
            if i['objectKey']==objectKey:
                objectId = i['objectId'].encode(encoding="utf-8")
                urn = base64.b64encode(objectId).decode('utf-8').strip("=").encode('utf-8')
                b=urn
        return b


class delete_object_from_bucket(Base):
    def __init__(self,bucketname,filename):
        super(delete_object_from_bucket,self).__init__()
        self.bucketname=bucketname
        self.filename=filename
        self.url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s' % (self.bucketname, self.filename)
        self.auth = authenticate.authenticate().get_access_token
        self.header = {
            'Authorization': self.auth,
            'Content-Type': 'application/octet-stream',
        }
        self.method = 'delete'

    def result(self):
        return self.GetContent()

class download_file_from_bucket(Base):
    def __init__(self,bucketname,filename):
        super(download_file_from_bucket,self).__init__()
        self.bucketname=bucketname
        self.filename=filename
        self.url = 'https://developer.api.autodesk.com/oss/v2/buckets/%s/objects/%s' % (self.bucketname, self.filename)
        self.auth = authenticate.authenticate().get_access_token
        self.header = {
            'Authorization': self.auth,
            'Content-Type': 'application/octet-stream',
        }
        self.method = 'put'

    def result(self):
        return self.GetContent()