---
layout: default
title: The Stability of Online Algorithms in Performative Prediction
---

# The Stability of Online Algorithms in Performative Prediction
**arXiv**：[2602.24207v1](https://arxiv.org/abs/2602.24207) · [PDF](https://arxiv.org/pdf/2602.24207.pdf)  
**作者**：Gabriele Farina, Juan Carlos Perdomo  

**一句话要点**：提出无条件归约证明在线算法在表演性预测中收敛至稳定均衡

**关键词**：表演性预测, 在线算法, 稳定均衡, 反馈循环, 鞅论, 随机化

## 3 点简述
- 核心问题：算法预测在决策中引发反馈循环，影响数据分布和模型重训练
- 方法要点：使用鞅论和随机化，避免对分布影响的强假设，证明无遗憾算法收敛
- 实验或效果：连接在线优化与表演性，解释梯度下降等算法自然稳定化机制

## 摘要（原文）

> The use of algorithmic predictions in decision-making leads to a feedback loop where the models we deploy actively influence the data distributions we see, and later use to retrain on. This dynamic was formalized by Perdomo et al. 2020 in their work on performative prediction. Our main result is an unconditional reduction showing that any no-regret algorithm deployed in performative settings converges to a (mixed) performatively stable equilibrium: a solution in which models actively shape data distributions in ways that their own predictions look optimal in hindsight. Prior to our work, all positive results in this area made strong restrictions on how models influenced distributions. By using a martingale argument and allowing randomization, we avoid any such assumption and sidestep recent hardness results for finding stable models. Lastly, on a more conceptual note, our connection sheds light on why common algorithms, like gradient descent, are naturally stabilizing and prevent runaway feedback loops. We hope our work enables future technical transfer of ideas between online optimization and performativity.

