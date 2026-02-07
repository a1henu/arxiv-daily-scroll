---
layout: default
title: Private Prediction via Shrinkage
---

# Private Prediction via Shrinkage
**arXiv**：[2602.05219v1](https://arxiv.org/abs/2602.05219) · [PDF](https://arxiv.org/pdf/2602.05219.pdf)  
**作者**：Chao Yan  

**一句话要点**：提出私有预测方法，在流式查询中降低样本复杂度至对数依赖

**关键词**：差分隐私预测, 流式查询, 样本复杂度, 概念类, 半空间, 在线对手

## 3 点简述
- 研究差分隐私预测问题，关注流式查询下的样本复杂度
- 针对不同对手模型，提出方法将查询数T的依赖从平方根降至多对数
- 理论分析显示，对概念类和半空间，所需标记样本数大幅减少

## 摘要（原文）

> We study differentially private prediction introduced by Dwork and Feldman (COLT 2018): an algorithm receives one labeled sample set $S$ and then answers a stream of unlabeled queries while the output transcript remains $(\varepsilon,δ)$-differentially private with respect to $S$. Standard composition yields a $\sqrt{T}$ dependence for $T$ queries.
>   We show that this dependence can be reduced to polylogarithmic in $T$ in streaming settings. For an oblivious online adversary and any concept class $\mathcal{C}$, we give a private predictor that answers $T$ queries with $\|S\|= \tilde{O}(VC(\mathcal{C})^{3.5}\log^{3.5}T)$ labeled examples. For an adaptive online adversary and halfspaces over $\mathbb{R}^d$, we obtain $\|S\|=\tilde{O}\left(d^{5.5}\log T\right)$.

