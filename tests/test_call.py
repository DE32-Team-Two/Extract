from extract.api.five_to_eight import ice_breaking, req, gen_url, get_key, list2df, save2df
import pandas as pd
import os


def test_save_df():
    df = req("20220501")

    assert isinstance(df, pd.DataFrame)


def test_exist_parquet():
    save2df("20220501")
    year,month,date="2022","05","01"
    parquet_path = '~/t2/test_parquet'
    up = os.path.expanduser(parquet_path)
    pf = os.path.join(up, f'year={year}', f'month={month}', f'date={date}')
    if os.path.exists(pf):
        assert True
    else:
        assert False

def test_ice_b():
    assert True

def test_list2df():
    pass
    #df = list2df()
    # assert isinstance(df, pd.DataFrame)
    # assert 'rnum' in df.columns
    # assert 'openDt' in df.columns
    # assert 'movieNm' in df.columns
    # assert 'audiAcc' in df.columns 
def test_req2list():
    pass
    #l = req2list()
    #assert len(l) > 0
    # v = l[0]
    # assert 'rnum' in v.keys()
    #assert v['rnum'] == '1'

def test_비밀키숨기기():
    key = get_key()
    assert key


def test_유알엘테스트():
    url = gen_url()
    assert "http" in url
    assert "kobis" in url
    
    #d = {"multiMovieYn": "N"}
    #url = gen_url(url_params = d)
    #print(url)
    #assert "multiMovieYn" in url
    

def test_req():
    pass
    #code, data = req()
    #assert code == 200

    #code, data = req('20230101')
    #print(data)
    #assert code == 200

