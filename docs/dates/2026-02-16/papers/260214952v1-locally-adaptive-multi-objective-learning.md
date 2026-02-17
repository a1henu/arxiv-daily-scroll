---
layout: default
title: Locally Adaptive Multi-Objective Learning
---

# Locally Adaptive Multi-Objective Learning
**arXiv**：[2602.14952v1](https://arxiv.org/abs/2602.14952) · [PDF](https://arxiv.org/pdf/2602.14952.pdf)  
**作者**：Jivat Neet Kaur, Isaac Gibbs, Michael I. Jordan  

**一句话要点**：提出局部自适应多目标学习方法，以应对在线数据分布变化下的多目标学习问题

**关键词**：多目标学习, 在线学习, 分布偏移, 自适应算法, 算法公平, 能源预测

## 3 点简述
- 核心问题：在线学习中数据分布任意变化时，现有方法难以同时满足多个目标（如校准、遗憾、多准确性）并适应分布偏移
- 方法要点：通过将多目标学习中的部分替换为自适应在线算法，实现局部自适应，提升对分布变化的鲁棒性
- 实验或效果：在能源预测和算法公平数据集上评估，显示方法优于现有方法，实现子群无偏预测，并在分布偏移下保持稳健

## 摘要（原文）

> We consider the general problem of learning a predictor that satisfies multiple objectives of interest simultaneously, a broad framework that captures a range of specific learning goals including calibration, regret, and multiaccuracy. We work in an online setting where the data distribution can change arbitrarily over time. Existing approaches to this problem aim to minimize the set of objectives over the entire time horizon in a worst-case sense, and in practice they do not necessarily adapt to distribution shifts. Earlier work has aimed to alleviate this problem by incorporating additional objectives that target local guarantees over contiguous subintervals. Empirical evaluation of these proposals is, however, scarce. In this article, we consider an alternative procedure that achieves local adaptivity by replacing one part of the multi-objective learning method with an adaptive online algorithm. Empirical evaluations on datasets from energy forecasting and algorithmic fairness show that our proposed method improves upon existing approaches and achieves unbiased predictions over subgroups, while remaining robust under distribution shift.

