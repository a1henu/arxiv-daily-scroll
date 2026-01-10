---
layout: default
title: Optimal Lower Bounds for Online Multicalibration
---

# Optimal Lower Bounds for Online Multicalibration
**arXiv**：[2601.05245v1](https://arxiv.org/abs/2601.05245) · [PDF](https://arxiv.org/pdf/2601.05245.pdf)  
**作者**：Natalie Collina, Jiuyao Lu, Georgy Noarov, Aaron Roth  

**一句话要点**：证明在线多校准的紧下界，建立与边际校准的信息论分离。

**关键词**：在线学习, 多校准, 下界证明, 信息论, 组函数, 边际校准

## 3 点简述
- 核心问题：在线多校准的下界分析，对比边际校准的复杂度差异。
- 方法要点：使用信息论技术，基于组函数依赖关系构造下界证明。
- 实验或效果：在一般和受限组函数设置下，分别匹配已知上界至对数因子。

## 摘要（原文）

> We prove tight lower bounds for online multicalibration, establishing an information-theoretic separation from marginal calibration.
>   In the general setting where group functions can depend on both context and the learner's predictions, we prove an $Ω(T^{2/3})$ lower bound on expected multicalibration error using just three disjoint binary groups. This matches the upper bounds of Noarov et al. (2025) up to logarithmic factors and exceeds the $O(T^{2/3-\varepsilon})$ upper bound for marginal calibration (Dagan et al., 2025), thereby separating the two problems.
>   We then turn to lower bounds for the more difficult case of group functions that may depend on context but not on the learner's predictions. In this case, we establish an $\widetildeΩ(T^{2/3})$ lower bound for online multicalibration via a $Θ(T)$-sized group family constructed using orthogonal function systems, again matching upper bounds up to logarithmic factors.

