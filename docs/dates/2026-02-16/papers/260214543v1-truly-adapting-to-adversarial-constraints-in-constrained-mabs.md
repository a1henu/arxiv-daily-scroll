---
layout: default
title: Truly Adapting to Adversarial Constraints in Constrained MABs
---

# Truly Adapting to Adversarial Constraints in Constrained MABs
**arXiv**：[2602.14543v1](https://arxiv.org/abs/2602.14543) · [PDF](https://arxiv.org/pdf/2602.14543.pdf)  
**作者**：Francesco Emanuele Stradi, Kalana Kalupahana, Matteo Castiglioni, Alberto Marchesi, Nicola Gatti  

**一句话要点**：提出算法以在约束多臂老虎机中适应对抗性约束，实现最优后悔与正违反率。

**关键词**：约束多臂老虎机, 对抗性学习, 非平稳环境, 强盗反馈, 后悔最小化, 约束违反控制

## 3 点简述
- 研究约束多臂老虎机问题，在损失和约束均非平稳环境下平衡后悔与约束违反。
- 提出算法在完全反馈下实现O(√T+C)后悔和正违反，并扩展至强盗反馈场景。
- 算法在约束随机、损失对抗时达到最优性能，并平滑适应约束对抗性程度。

## 摘要（原文）

> We study the constrained variant of the \emph{multi-armed bandit} (MAB) problem, in which the learner aims not only at minimizing the total loss incurred during the learning dynamic, but also at controlling the violation of multiple \emph{unknown} constraints, under both \emph{full} and \emph{bandit feedback}. We consider a non-stationary environment that subsumes both stochastic and adversarial models and where, at each round, both losses and constraints are drawn from distributions that may change arbitrarily over time. In such a setting, it is provably not possible to guarantee both sublinear regret and sublinear violation. Accordingly, prior work has mainly focused either on settings with stochastic constraints or on relaxing the benchmark with fully adversarial constraints (\emph{e.g.}, via competitive ratios with respect to the optimum). We provide the first algorithms that achieve optimal rates of regret and \emph{positive} constraint violation when the constraints are stochastic while the losses may vary arbitrarily, and that simultaneously yield guarantees that degrade smoothly with the degree of adversariality of the constraints. Specifically, under \emph{full feedback} we propose an algorithm attaining $\widetilde{\mathcal{O}}(\sqrt{T}+C)$ regret and $\widetilde{\mathcal{O}}(\sqrt{T}+C)$ {positive} violation, where $C$ quantifies the amount of non-stationarity in the constraints. We then show how to extend these guarantees when only bandit feedback is available for the losses. Finally, when \emph{bandit feedback} is available for the constraints, we design an algorithm achieving $\widetilde{\mathcal{O}}(\sqrt{T}+C)$ {positive} violation and $\widetilde{\mathcal{O}}(\sqrt{T}+C\sqrt{T})$ regret.

