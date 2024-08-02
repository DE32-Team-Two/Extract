import requests
import os
import pandas as pd


def ice_b():
    return "ice breaking"


def save2df(load_dt='20120101', url_params={}, df=None):
    # 외부에서 입력 받는 DF가 없다면 날짜와 URL Param으로 데이터를 추출
    if df is None:
        df = list2df(load_dt, url_params)

    df['load_dt'] = load_dt

    partitions = [
        'load_dt'
    ]

    for k, v in url_params.items():
        df[k] = v
        partitions.append(k)

    print(f"partitioning List : {partitions}")

    df.to_parquet('~/tmp/test_parquet', partition_cols=partitions)

    return df

def list2df(load_dt='20120101', url_params={}):
    l = req2list(load_dt, url_params)
    df = pd.DataFrame(l)
    return df


def req2list(load_dt='20120101', url_params={}) -> list:
    _, data = req(load_dt, url_params)
    l = data['boxOfficeResult']['dailyBoxOfficeList']
    return l


def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(load_dt="20120101", url_params={}):
    url = gen_url(load_dt, url_params)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    print(data)
    return code, data

def gen_url(dt="20120101", url_params={}):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"
    for k, v in url_params.items():
        url = url + f"&{k}={v}"
    return url
