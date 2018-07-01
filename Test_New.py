from Base.Model_Derivative import *
from Base.authenticate import *
from bubble import bubble
from Base.Data_Management import *
from urllib import parse
#c=create_bucket("shixiang")
#print(c.GetContentObject().content)
#GetBucketList
#bucklist=get_bucket_list()
#print(bucklist.GetContentObject().content)

filepath=r'E:\01_TenElephant_Project\2018_Project\20880414 SongYang_Project\02 BIM_单体\#1\20180419 中心文件\SONGYANG_1_code_fin.rvt'
filename=r'SONGYANG_1_fin.rvt'


#c=upload_file_to_bucket('shixiang',filepath,filename)

#print(c.GetContentObject().content)
#c=POST_job('shixiang',filename)

#print(c.GetContentObject().content)

#c=Get_urn_manifest("shixiang",filename)
#print(c.GetContentObject().content)

#c=DELETE_urn_manifest("shixiang",filename)
#print(c.GetContentObject().content)

#objectfrombucket=get_object_from_bucket('shixiang')
#print(objectfrombucket.GetContentAsJson())


#deleteobject=delete_object_from_bucket('shixiang',filename)
#print(deleteobject.GetContentObject().content)


b=bubble('shixiang',filename)
ll=b.Download(r'C:\Users\2016028\Desktop\Tem\SongYang__All\Tem1')

#c=authenticate.authenticate()

#print(c.get_access_token)

