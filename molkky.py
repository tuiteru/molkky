######################################################
# Hayashi版 Molkky点数プログラム
# 2023-06-11 Version 1.0 by Hiro Hayashi
######################################################

import sys
import datetime

"""""""""""""""""""""""""""""
日付の出力をクラス化
print("")
print("今日は" + str(datetime.date.today()) + "です。")
print("")
"""""""""""""""""""""""""""""

class Datestamp:
    #初期値
    def __init__(self):
        #なんの処理もしない
        pass
    #日付の機能
    def printdatetime(self):
        print("")
        print("今日は" + str(datetime.date.today()) + "です。")
        print("")

#インスタンスの作成
date_stamp = Datestamp()

#ここで日付の出力
date_stamp.printdatetime()


teams = []
scores = {}
fouls = {}

def createTeam(team_name):
    if team_name == "":
        return False
    else:
        teams.append(team_name)
        scores[team_name] = 0
        fouls[team_name] = 0
        return True

# チーム作成
while createTeam(input("チーム " + str(len(teams) + 1)+ " のチーム名 (何も入力せずEnterでチーム登録終了): ")):
    for i in range(len(teams)):
        print("■ チーム " + str(i + 1) + " : " + str(teams[i]))

teams_number = len(teams)

if teams_number < 1:
    print("登録チームの数がゼロなので終了します。")
    sys.exit()

# ゲーム開始
print("----------------------")
print("  ゲ  ー  ム  開  始  ")
print("----------------------")

# イニング数のカウンタを初期化
inning = 0
gameplay = True

while gameplay:
    inning += 1
    print("")
    print("◆◆◆ " + str(inning) + "回戦 ◆◆◆")
    print("")
    for team in teams:
        print("■ " + str(team) + ":")
        print("   現在のスコア: " + str(scores[team]) + " 点    連続ファール: " + str(fouls[team]) + " 回")
    print("")
    for team in teams:
        # スコア入力
        while True:
            score = input(team + ": 倒した本数または点数を入力: ")
            # 入力値が0から12の整数であるかチェック
            if score.isdigit() and 0 <= int(score) <= 12:
                break
            else:
                print("倒した本数または点数は 0 から 12 の範囲で入力してください。")
        # 倒した本数が0の場合はファールに1点加算
        if score == "0":
            fouls[team] += 1
            print(team + ": 連続ファール: " + str(fouls[team]) + " 回目")
        else:
            scores[team] += int(score)
            fouls[team] = 0
        # スコアが50点を超えた場合は25点に戻す
        if scores[team] > 50:
            scores[team] = 25
            print("")
            print(team + "のスコアが50点を超えたので25点に戻ります。")
            print("")
        # 3回連続ファールの場合はゲームセット
        if fouls[team] == 3:
            print("")
            print(team + " のファールが3回になったのでゲームセットです。")
            print("")
            print("チーム " + team + " の負け！")
            print("")
            gameplay = False
            break
        # スコアが50点ぴったりの場合はゲームセット
        if scores[team] == 50:
            print("")
            print(team + " のスコアが50点になったのでゲームセットです。")
            print("")
            # 勝者チームを表示
            print("チーム " + team + " の勝ち！")
            print("")
            gameplay = False
            break

print("----------------------")
print("  ゲ  ー  ム  終  了  ")
print("----------------------")
print("")
