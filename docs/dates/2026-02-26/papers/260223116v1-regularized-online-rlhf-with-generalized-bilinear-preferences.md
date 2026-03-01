---
layout: default
title: Regularized Online RLHF with Generalized Bilinear Preferences
---

# Regularized Online RLHF with Generalized Bilinear Preferences
**arXiv**：[2602.23116v1](https://arxiv.org/abs/2602.23116) · [PDF](https://arxiv.org/pdf/2602.23116.pdf)  
**作者**：Junghyun Lee, Minju Hong, Kwang-Sung Jun, Chulhee Yun, Se-Young Yun  

**一句话要点**：提出正则化在线RLHF与广义双线性偏好模型，以解决上下文在线RLHF中识别纳什均衡的问题。

**关键词**：在线强化学习从人类反馈, 广义双线性偏好模型, 正则化优化, 遗憾分析, 纳什均衡, 高维统计

## 3 点简述
- 研究上下文在线RLHF，目标为识别纳什均衡，采用广义双线性偏好模型捕捉非传递偏好。
- 分析基于强凸正则化，证明贪婪策略对偶间隙受估计误差平方约束，推广了先前工作。
- 提出贪婪采样和探索-提交算法，分别实现无指数依赖的多对数遗憾和无多项式依赖的统计高效遗憾。

## 摘要（原文）

> We consider the problem of contextual online RLHF with general preferences, where the goal is to identify the Nash Equilibrium. We adopt the Generalized Bilinear Preference Model (GBPM) to capture potentially intransitive preferences via low-rank, skew-symmetric matrices. We investigate general preference learning with any strongly convex regularizer (where $η^{-1}$ is the regularization strength), generalizing beyond prior works limited to reverse KL-regularization. Central to our analysis is proving that the dual gap of the greedy policy is bounded by the square of the estimation error - a result derived solely from strong convexity and the skew-symmetricity of GBPM.Building on this insight and a feature diversity assumption, we establish two regret bounds via two simple algorithms: (1) Greedy Sampling achieves polylogarithmic, $e^{O(η)}$-free regret $\tilde{O}(ηd^4 (\log T)^2)$. (2) Explore-Then-Commit achieves $\mathrm{poly}(d)$-free regret $\tilde{O}(\sqrt{ηr T})$ by exploiting the low-rank structure; this is the first statistically efficient guarantee for online RLHF in high-dimensions.

