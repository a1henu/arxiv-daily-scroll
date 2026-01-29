---
layout: default
title: On the Computational Complexity of Performative Prediction
---

# On the Computational Complexity of Performative Prediction
**arXiv**：[2601.20180v1](https://arxiv.org/abs/2601.20180) · [PDF](https://arxiv.org/pdf/2601.20180.pdf)  
**作者**：Ioannis Anagnostides, Rohan Chauhan, Ioannis Panageas, Tuomas Sandholm, Jingming Yan  

**一句话要点**：揭示执行预测在强效应下的计算复杂性为PPAD完全，并扩展至战略分类的PLS困难性

**关键词**：执行预测, 计算复杂性, PPAD完全, 战略分类, 变分不等式, 分布偏移

## 3 点简述
- 核心问题：执行预测中强效应（ρ>1）下计算稳定点的复杂性未知
- 方法要点：证明计算ε-执行稳定点是PPAD完全的，即使ρ接近1，并扩展至凸域
- 实验或效果：在二次损失和线性分布偏移的简单设置中，复杂性依然存在

## 摘要（原文）

> Performative prediction captures the phenomenon where deploying a predictive model shifts the underlying data distribution. While simple retraining dynamics are known to converge linearly when the performative effects are weak ($ρ< 1$), the complexity in the regime $ρ> 1$ was hitherto open. In this paper, we establish a sharp phase transition: computing an $ε$-performatively stable point is PPAD-complete -- and thus polynomial-time equivalent to Nash equilibria in general-sum games -- even when $ρ= 1 + O(ε)$. This intractability persists even in the ostensibly simple setting with a quadratic loss function and linear distribution shifts. One of our key technical contributions is to extend this PPAD-hardness result to general convex domains, which is of broader interest in the complexity of variational inequalities. Finally, we address the special case of strategic classification, showing that computing a strategic local optimum is PLS-hard.

