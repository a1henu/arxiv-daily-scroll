---
layout: default
title: Displacement-Resistant Extensions of DPO with Nonconvex $f$-Divergences
---

# Displacement-Resistant Extensions of DPO with Nonconvex $f$-Divergences
**arXiv**：[2602.06788v1](https://arxiv.org/abs/2602.06788) · [PDF](https://arxiv.org/pdf/2602.06788.pdf)  
**作者**：Idan Pipano, Shoham Sabach, Kavosh Asadi, Mohammad Ghavamzadeh  

**一句话要点**：提出SquaredPO损失以解决DPO中的概率位移问题，基于非凸f-散度扩展理论框架。

**关键词**：语言模型对齐, f-散度, 概率位移, 强化学习从人类反馈, 非凸优化, SquaredPO损失

## 3 点简述
- 核心问题：DPO算法在RLHF中可能引发概率位移，导致胜败响应概率趋近零。
- 方法要点：识别DPO诱导和位移抵抗条件，扩展f-散度到非凸函数，确保问题可解。
- 实验或效果：SquaredPO损失在理论上更强，实践中性能与DPO竞争。

## 摘要（原文）

> DPO and related algorithms align language models by directly optimizing the RLHF objective: find a policy that maximizes the Bradley-Terry reward while staying close to a reference policy through a KL divergence penalty. Previous work showed that this approach could be further generalized: the original problem remains tractable even if the KL divergence is replaced by a family of $f$-divergence with a convex generating function $f$. Our first contribution is to show that convexity of $f$ is not essential. Instead, we identify a more general condition, referred to as DPO-inducing, that precisely characterizes when the RLHF problem remains tractable. Our next contribution is to establish a second condition on $f$ that is necessary to prevent probability displacement, a known empirical phenomenon in which the probabilities of the winner and the loser responses approach zero. We refer to any $f$ that satisfies this condition as displacement-resistant. We finally focus on a specific DPO-inducing and displacement-resistant $f$, leading to our novel SquaredPO loss. Compared to DPO, this new loss offers stronger theoretical guarantees while performing competitively in practice.

