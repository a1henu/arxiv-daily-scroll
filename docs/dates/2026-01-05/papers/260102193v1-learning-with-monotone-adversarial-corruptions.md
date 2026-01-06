---
layout: default
title: Learning with Monotone Adversarial Corruptions
---

# Learning with Monotone Adversarial Corruptions
**arXiv**：[2601.02193v1](https://arxiv.org/abs/2601.02193) · [PDF](https://arxiv.org/pdf/2601.02193.pdf)  
**作者**：Kasper Green Larsen, Chirag Pabbaraju, Abhishek Shetty  

**一句话要点**：提出单调对抗性腐败模型以揭示最优学习算法对数据交换性的过度依赖

**关键词**：对抗性学习, 数据腐败, 二分类, 均匀收敛, 交换性

## 3 点简述
- 研究标准机器学习算法对数据交换性和独立性的依赖程度，引入单调对抗性腐败模型
- 展示在单调腐败下，已知最优二分类算法在新测试点上可能产生次优预期误差
- 基于均匀收敛的算法在保证上未退化，凸显最优算法的脆弱性

## 摘要（原文）

> We study the extent to which standard machine learning algorithms rely on exchangeability and independence of data by introducing a monotone adversarial corruption model. In this model, an adversary, upon looking at a "clean" i.i.d. dataset, inserts additional "corrupted" points of their choice into the dataset. These added points are constrained to be monotone corruptions, in that they get labeled according to the ground-truth target function. Perhaps surprisingly, we demonstrate that in this setting, all known optimal learning algorithms for binary classification can be made to achieve suboptimal expected error on a new independent test point drawn from the same distribution as the clean dataset. On the other hand, we show that uniform convergence-based algorithms do not degrade in their guarantees. Our results showcase how optimal learning algorithms break down in the face of seemingly helpful monotone corruptions, exposing their overreliance on exchangeability.

