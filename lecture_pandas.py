#pandasをインポート
import pandas as pd

#5行2列のデータフレームを作成してdfに代入。列名は出身地と性別。
df=pd.DataFrame({"出身地":["大分市","別府市","中津市","佐伯市","大分市"],"性別":["男性","女性","女性","男性","女性"]})

#printにて出力
print(df)

#先頭2行を出力
df.head(2)


#出身地が大分市のみを抽出してdf_placeに代入。
df_place=df[df["出身地"]=="大分市"]

#性別が女性を抽出してdf_fに代入。
df_f=df[df["性別"]=="女性"]

#dfに年齢という新しい列を追加。
df["年齢"]=[10,20,30,40,50]

#年齢が30才以上を抽出してdf_over30に代入。
df_over30=df[df["年齢"]>=30]

#新しいデータフレームを作成してdf2に代入。
df2=pd.DataFrame({"出身地":["竹田市","国東市"],"性別":["男性","女性"],"年齢":[15,25]})

#dfとdf2を結合してdf_concatに代入。
df_concat=pd.concat([df,df2])

#新しいデータフレームを作成してdf3に代入。
df3=pd.DataFrame({"出身地":["中津市","竹田市"],"血液型":["A","O"]})

#df_concatとdf3で出身地が同じものを結合しdf_mergeに代入する。
df_merge=pd.merge(df_concat,df3,on="出身地")
