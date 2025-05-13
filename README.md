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

****

# Game Theory and Prisoner's Dilemma Strategy Simulation
## Project Overview
This project combines linear algebra, game theory, and Python simulation to explore two core topics:

1. Nash Equilibrium Strategy Analysis

2. "Tit for Tat" Strategy Simulation in the Prisoner’s Dilemma

The inspiration comes from the double-ferry Prisoner’s Dilemma scene in The Dark Knight, expanded into a game-theoretic simulation study.

## Research Content
### Nash Equilibrium Strategy Analysis
We applied linear algebra techniques and matrix operations to analyze strategic interactions in the following games:

1. The classic Prisoner’s Dilemma

2. Competitive strategies between two companies

Python was used to compute the probability distributions of optimal strategies and their respective utility values.

## Experimental Results
### Prisoner’s Dilemma Simulation (Tit for Tat Strategy)
A 20-round interaction was simulated between two prisoners: one adopting the Tit for Tat strategy, the other acting randomly. The simulation is based on Douglas Hofstadter’s payoff matrix.

Douglas Hofstadter's payoff matrix used in the experiment
<img src="https://github.com/giraffeiscute/python-simulation-projects-game-theory-and-Prisoner-s-Dilemma/blob/main/result/%E5%9C%96%E7%89%872.png" alt="image" width="600">

Simulation output (C = Cooperate, D = Defect): <br/>
[(C, D), (D, D), (D, D), (D, D), (D, C), <br/>
 (C, C), (C, D), (D, D), (D, C), (C, C), <br/>
 (C, D), (D, D), (D, C), (C, C), (C, D), <br/>
 (D, D), (D, C), (C, C), (C, C), (C, C)]

## Experimental Conclusion
1. Stability and Recoverability of Tit for Tat
- Although there are early defections (e.g., repeated (D, D) rounds), as soon as the opponent returns to cooperation (e.g., round 5), the Tit for Tat strategy reciprocates, gradually rebuilding trust—evidenced by (C, C) outcomes in rounds 6, 10, 14, and 18–20.

2. Responsive Strategy Suppresses Endless Defection
- Player A never initiates defection and only retaliates once after being betrayed. This prevents an endless loop of mutual defection and encourages the opponent to return to cooperation.

3. Long-Term Cooperation Emerges
- In later rounds (18–20), stable mutual cooperation (C, C) is achieved, demonstrating the effectiveness of the Tit for Tat strategy in establishing long-term cooperation in the Prisoner’s Dilemma.

## Technologies & Tools
Python

NumPy / Matrix computation

Axelrod library for game theory simulations

## Conclusion
This project integrates concepts from linear algebra, economics, and programming to deepen our understanding of strategic modeling and quantitative analysis. It also highlights the limitations of such models when applied to complex human psychology.

## References
Mythili Krishnan (Dec 2020). Game Theory concepts with application in Python using Axelrod.
https://towardsdatascience.com/game-theory-concepts-with-application-in-python-using-axel-rod-part-2-8ae5e10e09a0

Wikipedia (Jan 2021). Prisoner's Dilemma.
https://zh.wikipedia.org/wiki/囚徒困境

## Author
Chih-Yuan Yang <br/>
National Tsing Hua University


