import sys
import pandas as pd
import random as rd
import string
import datetime as dt

if __name__ == "__main__":
    ipf = str(input("入力ファイルのPATHを入力してください。\n>>"))
    #ipf = "./sample-input.csv"

    num = int(input("あたりの個数を入力してください。\n>>"))
    #num = 5

    dup = bool(input("重複当選の有無を入力してください。(True/False)\n>>"))
    #dup = False

    with open("./choice.log", mode="a", encoding="utf-8_sig") as log:
        now = dt.datetime.now()
        log.write("-----" + str(now) + "の実行ログ-----\n")
        ipf = pd.read_csv(ipf, encoding="cp932")
        print(ipf)

        dice = list(range(0, len(ipf)))
        weight = list(ipf["weight"])

        ipf["result"] = ""
        if dup:
            for chance in range(num):
                choice = rd.choices(dice, weights=weight)[000]
                ipf.loc[choice,
                        "result"] += list(string.ascii_lowercase)[chance]
                print(">>", ipf.loc[choice, "choice"], "さんが当選しました。")
                log.write(">>" + ipf.loc[choice, "choice"] + "さんが当選しました。\n")
        else:
            if not((len(ipf) - num) > -1):
                print("候補数が少ない、あるいは当選数が多すぎます。再設定してください。")
                log.write("候補数が少ない、あるいは当選数が多すぎます。再設定してください。\n")
                sys.exit()
            for chance in range(num):
                while True:
                    choice = rd.choices(dice, weights=weight)[0]
                    if ipf.loc[choice, "result"] == "":
                        ipf.loc[choice, "result"] = list(
                            string.ascii_lowercase)[chance]
                        print(">>", ipf.loc[choice, "choice"], "さんが当選しました。")
                        log.write(
                            ">>" + ipf.loc[choice, "choice"] + "さんが当選しました。\n")
                        break
                    else:
                        print(">>", ipf.loc[choice, "choice"],
                              "さんが当選しましたが、重複したため再抽選します。")
                        log.write(
                            ">>" + ipf.loc[choice, "choice"] + "さんが当選しましたが、重複したため再抽選します。\n")
                        continue

        print(ipf)
        ipf.to_csv("result.csv", encoding="utf-8_sig")
