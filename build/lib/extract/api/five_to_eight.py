import os
import requests
import pandas as pd

def ice_breaking():
    img = """
    ice!!!!!!
    """
    return img

def get_key():
    key = os.getenv('MOVIE_API_KEY')
    return key

def gen_url(load_dt='20220501', url_param = {}):
    key = get_key()
    base_url = "http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key="
    url = base_url + f"{key}&targetDt={load_dt}"
    for k, v in url_param.items():
        url += f"&{k}={v}"

    return url

def req(load_dt='20220501', url_params={}):
    url = gen_url(load_dt)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    df = pd.DataFrame(data['boxOfficeResult']['dailyBoxOfficeList'])

    return df

def list2df(load_dt='20220501', url_param = {}):
    l = req2list(load_dt, url_param)
    df = pd.DataFrame(l)
    return df

def save2df(load_dt='20220501'):

    PARQUET_PATH='~/t2/test_parquet'

    df = req(load_dt)

    df['year'] = str(load_dt[0:4])
    df['month'] = str(load_dt[4:6])
    df['date'] = str(load_dt[6:9])

    partitions = [
    'year', 'month', 'date'
            ]

    exist_parquet(PARQUET_PATH, str(load_dt[0:4]), str(load_dt[4:6]), str(load_dt[7:9]))

    df.to_parquet(PARQUET_PATH, partition_cols=partitions)

    return df

def exist_parquet(parquet_path, year, month, date):
    import os
    up = os.path.expanduser(parquet_path)
    pf = os.path.join(up, f'year={year}', f'month={month}', f'date={date}')
    if os.path.exists(pf):
        import shutil
        shutil.rmtree(pf)
