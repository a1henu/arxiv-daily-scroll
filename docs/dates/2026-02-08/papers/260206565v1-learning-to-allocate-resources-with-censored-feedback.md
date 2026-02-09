---
layout: default
title: Learning to Allocate Resources with Censored Feedback
---

# Learning to Allocate Resources with Censored Feedback
**arXiv**：[2602.06565v1](https://arxiv.org/abs/2602.06565) · [PDF](https://arxiv.org/pdf/2602.06565.pdf)  
**作者**：Giovanni Montanari, Côme Fiegel, Corentin Pla, Aadirupa Saha, Vianney Perchet  

**一句话要点**：提出RA-UCB和MG-UCB算法，解决在线资源分配中的审查反馈问题。

**关键词**：在线资源分配, 审查反馈, 遗憾分析, 参数估计, 乐观算法

## 3 点简述
- 研究在线资源分配问题，需在审查反馈下估计未知参数并分配预算。
- 提出乐观算法RA-UCB和MG-UCB，实现亚线性或对数级遗憾上界。
- 在真实数据集上验证理论结果，展示算法有效性。

## 摘要（原文）

> We study the online resource allocation problem in which at each round, a budget $B$ must be allocated across $K$ arms under censored feedback. An arm yields a reward if and only if two conditions are satisfied: (i) the arm is activated according to an arm-specific Bernoulli random variable with unknown parameter, and (ii) the allocated budget exceeds a random threshold drawn from a parametric distribution with unknown parameter. Over $T$ rounds, the learner must jointly estimate the unknown parameters and allocate the budget so as to maximize cumulative reward facing the exploration--exploitation trade-off. We prove an information-theoretic regret lower bound $Ω(T^{1/3})$, demonstrating the intrinsic difficulty of the problem. We then propose RA-UCB, an optimistic algorithm that leverages non-trivial parameter estimation and confidence bounds. When the budget $B$ is known at the beginning of each round, RA-UCB achieves a regret of order $\widetilde{\mathcal{O}}(\sqrt{T})$, and even $\mathcal{O}(\mathrm{poly}\text{-}\log T)$ under stronger assumptions. As for unknown, round dependent budget, we introduce MG-UCB, which allows within-round switching and infinitesimal allocations, and matches the regret guarantees of RA-UCB. We then validate our theoretical results through experiments on real-world datasets.

