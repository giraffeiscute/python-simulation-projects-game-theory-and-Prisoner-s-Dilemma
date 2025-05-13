English version underneaath
# 賽局理論與囚徒困境策略模擬分析

## 專案簡介
本專案結合線性代數、賽局理論與 Python 程式模擬，探討兩大主題：

1. 奈許均衡策略分析

2. 囚徒困境中「以牙還牙（Tit for Tat）」策略模擬

靈感來自電影《蝙蝠俠》中雙船囚徒困境的橋段，進一步延伸為賽局理論模擬研究。

## 研究內容
### 奈許均衡策略分析
透過線性代數方法與矩陣運算，分析以下賽局：
- 囚徒困境模擬

- 雙公司策略分配賽局

利用 Python 程式輸出最佳策略的機率分配與對應的效益值（Utility）。

## 實驗結果
### 囚徒困境模擬（Tit for Tat 策略）
模擬兩位囚犯互動20次，其中一方使用「以牙還牙」策略，另一方隨機行動。根據 Douglas Hofstadter 所提出的支付矩陣進行模擬分析。

此為本實驗之Douglas Hofstadter 支付矩陣設定

<img src="https://github.com/giraffeiscute/python-simulation-projects-game-theory-and-Prisoner-s-Dilemma/blob/main/result/%E5%9C%96%E7%89%872.png" alt="image" width="600">

模擬結果: (C為合作D為背叛) <br/>
[(C, D), (D, D), (D, D), (D, D), (D, C), <br/>
 (C, C), (C, D), (D, D), (D, C), (C, C), <br/>
 (C, D), (D, D), (D, C), (C, C), (C, D), <br/>
 (D, D), (D, C), (C, C), (C, C), (C, C)]

## 實驗結論
1. 以牙還牙具備穩定性與回復性
- 雖然初期出現背叛 (如前幾輪出現連續 (D, D))，但只要對方不再持續背叛（如第 5 回合玩家 B 選擇 C），「以牙還牙」策略便會選擇合作，並逐漸重建互信。這可從第 6、10、14、18~20 回合出現 (C, C) 看出。

2. 策略回應模式可抑制背叛連鎖
- 玩家 A 不會主動背叛，僅在對方背叛時回應一次背叛，這樣的策略可避免無止盡的 (D, D) 惡性循環，鼓勵對方回歸合作。

3. 長期合作可逐漸形成
- 模擬結果在後期（第 18～20 回合）呈現穩定的雙方合作 (C, C)，證實了「以牙還牙」策略在囚徒困境中的有效性，有助於建立長期穩定的合作關係。


## 技術與工具
Python

Numpy / Matrix 運算

Axelrod 賽局模擬套件

## 總結
本專案綜合運用了線性代數、經濟學與程式設計等領域知識，深化了對策略行為建模與量化分析的理解，也反思了模型在人類心理層面的侷限。

## 參考資料
Mythili Krishnan (Dec 2020). Game Theory concepts with application in Python using Axelrod.
https://towardsdatascience.com/game-theory-concepts-with-application-in-python-using-axel-rod-part-2-8ae5e10e09a0

Wikipedia (Jan 2021). 囚徒困境
https://zh.wikipedia.org/wiki/囚徒困境

作者
楊致遠<br\>
國立清華大學
