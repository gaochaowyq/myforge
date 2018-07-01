from Base.Model_Derivative import *
from Base.authenticate import *
from bubble import bubble
from Base.Data_Management import *
from urllib import parse
def run():
    filepath = r'C:\Users\2016028\Desktop\Tem\SongYang__All\SONGYANG_1_code_fin.rvt'
    filename = r'SONGYANG_1_code_fin.rvt'
    objectfrombucket=get_object_from_bucket('shixiang')
    print(objectfrombucket.GetContentAsJson())
    c=upload_file_to_bucket('shixiang',filepath,filename)
    print(c.GetContentObject().content)
    c=POST_job('shixiang',filename)

    print(c.GetContentObject().content)

if __name__ == '__main__':
    pass
