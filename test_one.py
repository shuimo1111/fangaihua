# Author: fangmiao

# CreatTime: 2021/3/11

# FileName: test_one

# Description: A very interesting piece of code
import pandas as pd

df ={'姓名':[' 黄同学','黄至尊','黄老邪 ','陈大美','孙尚香'],
     '英文名':['Huang tong_xue','huang zhi_zun','Huang Lao_xie','Chen Da_mei','sun shang_xiang'],
     '性别':['男','women','men','女','男'],
     '身份证':['463895200003128433','429475199912122345','420934199110102311','431085200005230122','420953199509082345'],
     '身高':['mid:175_good','low:165_bad','low:159_bad','high:180_verygood','low:172_bad'],
     '家庭住址':['湖北广水','河南信阳','广西桂林','湖北孝感','广东广州'],
     '电话号码':['13434813546','19748672895','16728613064','14561586431','19384683910'],
     '收入':['1.1万','8.5千','0.9万','6.5千','2.0万']}
df = pd.DataFrame(df)
print(df)
