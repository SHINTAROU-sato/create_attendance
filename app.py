import pandas as pd
import json
from pandas.io.json import json_normalize
import sys

args = sys.argv
print(args)
if args[1] == "pulala": # 第一引数にpulalaを設定した場合
    #変換したいJSONファイルを読み込む
    df = pd.read_json('sample.json')
    print(df)

    # read_jsonした結果だとネストしたjsonを展開できないのでnormalizeで展開させる
    df_json = json_normalize(df['data'])
    df_json.to_csv("out.csv", header=False, index=False, encoding='utf-8')

if args[1] == "goodworks": #第一引数にgoodworksを設定した場合
    #変換したいJSONファイルを読み込む
    df = pd.read_json('sample2.json')
    print(df)

    # read_jsonした結果だとネストしたjsonを展開できないのでnormalizeで展開させる
    df_json = json_normalize(df['data'])
    df_json.to_csv("out.csv", header=False, index=False, encoding='utf-8')