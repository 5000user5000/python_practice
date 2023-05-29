import pandas as pd
from unittest.mock import Mock #unittest的套件

def id2group():
    pass

#偶數的分一組，奇數一組
def mock_id2group(id_list):
    group =[]
    for id in id_list:
        group.append(id%2)
    return group

def mock_connect():
    pass

#id2g = id2group()
id2g = Mock() #模擬真的func
id2g.connect = mock_connect #不是寫 mock_connect() ，而是直接給函式名
id2g.connect("postgresql://192.168.110.100:5432/groupdb")
#id2g.connect.return_value  = "postgresql://192.168.110.100:5432/groupdb"
id2g.mapping = mock_id2group

def group_mean_std(input_fn):
    df1 = pd.read_csv(input_fn)
    id_list = df1.iloc[:,0].values
    df1['group'] = id2g.mapping(id_list)
    tmpsum = (df1[['Score', 'group']].groupby("group").agg(['mean', 'std', 'count']))    
    return tmpsum.to_dict()

ans = group_mean_std("./data1.csv")
#確認結果，還有 pair dict 是這樣去呼叫的，和陣列小小不同，且不能用ans[0]
assert ans['Score','mean'] == {0: 62.46031746031746, 1: 68.1875},"it should be {0: 62.46031746031746, 1: 68.1875}"
assert ans['Score','std'] == {0: 22.072333724067917, 1: 19.97289830411868},"it should be {0: 22.072333724067917, 1: 19.97289830411868}"
assert  ans['Score','count']==  {0: 63, 1: 64},"it should be {0: 63, 1: 64}"
#print(ans['Score','count']) 
#print(ans)
