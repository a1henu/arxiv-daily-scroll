---
layout: default
title: Online Learning in MDPs with Partially Adversarial Transitions and Losses
---

# Online Learning in MDPs with Partially Adversarial Transitions and Losses
**arXiv**：[2602.09474v1](https://arxiv.org/abs/2602.09474) · [PDF](https://arxiv.org/pdf/2602.09474.pdf)  
**作者**：Ofir Schlisselberg, Tal Lancewicki, Yishay Mansour  

**一句话要点**：提出条件占用度量以处理MDP中部分对抗性转移和损失，实现在线学习算法。

**关键词**：强化学习, 对抗性MDP, 在线学习, 后悔界, 条件占用度量, 部分对抗性转移

## 3 点简述
- 研究MDP中转移函数在多数步骤随机、少数步骤对抗的强化学习问题。
- 引入条件占用度量保持稳定性，设计两种算法处理对抗步骤。
- 给出后悔界分析，包括完全对抗设置的上界和下界匹配结果。

## 摘要（原文）

> We study reinforcement learning in MDPs whose transition function is stochastic at most steps but may behave adversarially at a fixed subset of $Λ$ steps per episode. This model captures environments that are stable except at a few vulnerable points. We introduce \emph{conditioned occupancy measures}, which remain stable across episodes even with adversarial transitions, and use them to design two algorithms. The first handles arbitrary adversarial steps and achieves regret $\tilde{O}(H S^Λ\sqrt{K S A^{Λ+1}})$, where $K$ is the number of episodes, $S$ is the number of state, $A$ is the number of actions and $H$ is the episode's horizon. The second, assuming the adversarial steps are consecutive, improves the dependence on $S$ to $\tilde{O}(H\sqrt{K S^{3} A^{Λ+1}})$. We further give a $K^{2/3}$-regret reduction that removes the need to know which steps are the $Λ$ adversarial steps. We also characterize the regret of adversarial MDPs in the \emph{fully adversarial} setting ($Λ=H-1$) both for full-information and bandit feedback, and provide almost matching upper and lower bounds (slightly strengthen existing lower bounds, and clarify how different feedback structures affect the hardness of learning).

