---
layout: default
title: Linear Convergence in Games with Delayed Feedback via Extra Prediction
---

# Linear Convergence in Games with Delayed Feedback via Extra Prediction
**arXiv**：[2602.17486v1](https://arxiv.org/abs/2602.17486) · [PDF](https://arxiv.org/pdf/2602.17486.pdf)  
**作者**：Yuma Fujimoto, Kenshi Abe, Kaito Ariu  

**一句话要点**：提出加权乐观梯度下降-上升算法，通过额外预测加速延迟反馈下双线性博弈的线性收敛。

**关键词**：延迟反馈, 双线性博弈, 乐观梯度下降-上升, 线性收敛, 额外预测, 多智能体学习

## 3 点简述
- 研究延迟反馈在多智能体学习中的性能退化问题，聚焦双线性博弈的收敛率未知。
- 将加权乐观梯度下降-上升算法解释为额外近端点近似，分析其线性收敛率，并证明额外预测可容忍更大步长。
- 实验验证额外预测驱动加速收敛，与理论结果定性一致，表明其为应对延迟的有效对策。

## 摘要（原文）

> Feedback delays are inevitable in real-world multi-agent learning. They are known to severely degrade performance, and the convergence rate under delayed feedback is still unclear, even for bilinear games. This paper derives the rate of linear convergence of Weighted Optimistic Gradient Descent-Ascent (WOGDA), which predicts future rewards with extra optimism, in unconstrained bilinear games. To analyze the algorithm, we interpret it as an approximation of the Extra Proximal Point (EPP), which is updated based on farther future rewards than the classical Proximal Point (PP). Our theorems show that standard optimism (predicting the next-step reward) achieves linear convergence to the equilibrium at a rate $\exp(-Θ(t/m^{5}))$ after $t$ iterations for delay $m$. Moreover, employing extra optimism (predicting farther future reward) tolerates a larger step size and significantly accelerates the rate to $\exp(-Θ(t/(m^{2}\log m)))$. Our experiments also show accelerated convergence driven by the extra optimism and are qualitatively consistent with our theorems. In summary, this paper validates that extra optimism is a promising countermeasure against performance degradation caused by feedback delays.

