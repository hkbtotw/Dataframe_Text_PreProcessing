from typing import no_type_check_decorator
import pandas as pd
from datetime import datetime, date,  timedelta
from dateutil.relativedelta import relativedelta
import math
import numpy as np

start_datetime = datetime.now()
print (start_datetime,'execute')
todayStr=date.today().strftime('%Y-%m-%d')
nowStr=datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print("TodayStr's date:", todayStr,' -- ',type(todayStr))
print("nowStr's date:", nowStr,' -- ',type(nowStr))


def Clean_Prefix(x):
    try:
        words = ["นาย","นางสาว","น.","นส.","น.ส."]
        themessage = str(x)    
        for word in words:
            themessage =  themessage.replace(word, "").strip()  
    except:
        themessage=x
    return themessage

def RemoveWhiteSpace_ALL(x):
    return x.strip().replace(' ','')

def ModifyPhoneNumber(x):
    dummy=x.strip().replace(' ','')
    dummy=dummy.replace('-','')
    print(x, ' ---  ',dummy)
    if(len(dummy)<=10):
        sum=10-len(dummy)
        print(len(dummy),' : ',sum)
        for n in range(sum):
            dummy='0'+dummy
        print(' result : ',dummy)
    return dummy

def Clean_TextGender(x):
    try:
        word_list = ['f.', 'f','หญิง','ญ.','ญ','female']  
        # initializing replace word 
        repl_wrd = 'female'  
        # Replace multiple words with K
        # Using join() + split() + list comprehension
        res = ' '.join([repl_wrd if idx in word_list else idx for idx in x.lower().split()])

        word_list = ['m.', 'm','ชาย','ช.','ช','male']  
        # initializing replace word 
        repl_wrd = 'male'  
        # Replace multiple words with K
        # Using join() + split() + list comprehension
        res = ' '.join([repl_wrd if idx in word_list else idx for idx in res.lower().split()])
    except:
        res=''
    return res

def Clean_FirstName(first_name_col, dfIn):  
    dfIn[first_name_col]=dfIn.apply(lambda x:Clean_Prefix(x[first_name_col]),axis=1)
    return dfIn
def Clean_IdCard(idcard_col, dfIn):
    dfIn[idcard_col]=dfIn.apply(lambda x:RemoveWhiteSpace_ALL(x[idcard_col]),axis=1)
    return dfIn
def Clean_MobileNumber(mobile_col, dfIn):
    dfIn[mobile_col]=dfIn.apply(lambda x:ModifyPhoneNumber(x[mobile_col]),axis=1)    
    return dfIn
def Clean_Gender(gender_col, dfIn):
    dfIn[gender_col]=dfIn.apply(lambda x:Clean_TextGender(x[gender_col]),axis=1)    
    return dfIn


# file_path='C:\\Users\\70018928\\Documents\\Project2021\\Ad-Hoc\\CleanText\\'

# file_name_1='DataVaccineSV_20210427_0830_.xlsx'
# file_name_2='DataVaccineSV_20210427_1500.xlsx'
# file_name_3='TemplateVaccineSV_20210426_1930.xlsx'

# cvt={'contact_emdid':str, 'contact_mobile':str}
# dfIn=pd.read_excel(file_path+file_name_1,sheet_name='ข้อมูลพนักงาน', converters=cvt )

# print(dfIn.head(10))
# dfDummy=dfIn.head(10).copy()

# first_name_col='Gender'
# #dfDummy=Clean_FirstName(first_name_col,dfDummy)
# #dfDummy=Clean_IdCard(first_name_col,dfDummy)
# dfDummy=Clean_Gender(first_name_col,dfDummy)
# dfDummy.to_csv(file_path+'check_prefix.csv')
# print(' ===> ',dfDummy)

###****************************************************************
end_datetime = datetime.now()
print ('---Start---',start_datetime)
print('---complete---',end_datetime)
DIFFTIME = end_datetime - start_datetime 
DIFFTIMEMIN = DIFFTIME.total_seconds()
print('Time_use : ',round(DIFFTIMEMIN,2), ' Seconds')
