---
layout: default
title: Distribution-informed Online Conformal Prediction
---

# Distribution-informed Online Conformal Prediction
**arXiv**：[2512.07770v1](https://arxiv.org/abs/2512.07770) · [PDF](https://arxiv.org/pdf/2512.07770.pdf)  
**作者**：Dongjian Hu, Junxi Wu, Shu-Tao Xia, Changliang Zou  

**一句话要点**：提出COP算法以解决在线共形预测中数据分布偏移导致的预测集保守问题

**关键词**：在线共形预测, 不确定性量化, 数据分布偏移, 预测集优化, 覆盖率保证

## 3 点简述
- 核心问题：在线共形预测在对抗性环境中因数据分布偏移产生保守预测集，影响效率
- 方法要点：COP通过非一致性分数的累积分布函数估计，将数据模式融入更新规则，生成更紧预测集
- 实验或效果：COP在保持有效覆盖率的同时，比基线方法构建更短的预测区间，验证了其有效性

## 摘要（原文）

> Conformal prediction provides a pivotal and flexible technique for uncertainty quantification by constructing prediction sets with a predefined coverage rate. Many online conformal prediction methods have been developed to address data distribution shifts in fully adversarial environments, resulting in overly conservative prediction sets. We propose Conformal Optimistic Prediction (COP), an online conformal prediction algorithm incorporating underlying data pattern into the update rule. Through estimated cumulative distribution function of non-conformity scores, COP produces tighter prediction sets when predictable pattern exists, while retaining valid coverage guarantees even when estimates are inaccurate. We establish a joint bound on coverage and regret, which further confirms the validity of our approach. We also prove that COP achieves distribution-free, finite-sample coverage under arbitrary learning rates and can converge when scores are $i.i.d.$. The experimental results also show that COP can achieve valid coverage and construct shorter prediction intervals than other baselines.

