---
layout: default
title: Penalized Fair Regression for Multiple Groups in Chronic Kidney Disease
---

# Penalized Fair Regression for Multiple Groups in Chronic Kidney Disease
**arXiv**：[2512.17340v1](https://arxiv.org/abs/2512.17340) · [PDF](https://arxiv.org/pdf/2512.17340.pdf)  
**作者**：Carter H. Nakamoto, Lucia Lushi Chen, Agata Foryciarz, Sherri Rose  

**一句话要点**：提出惩罚公平回归框架，解决慢性肾病中多群体社会偏见问题。

**关键词**：公平回归, 多群体偏见, 惩罚方法, 慢性肾病, 成本敏感分类, 医疗公平

## 3 点简述
- 核心问题：现有公平回归方法较少处理多群体偏见，尤其在医疗领域。
- 方法要点：引入多群体不公平惩罚，通过成本敏感分类高效实现，并自动选择惩罚权重。
- 实验或效果：模拟和真实数据中，在保持整体拟合的同时显著提升多群体公平性。

## 摘要（原文）

> Fair regression methods have the potential to mitigate societal bias concerns in health care, but there has been little work on penalized fair regression when multiple groups experience such bias. We propose a general regression framework that addresses this gap with unfairness penalties for multiple groups. Our approach is demonstrated for binary outcomes with true positive rate disparity penalties. It can be efficiently implemented through reduction to a cost-sensitive classification problem. We additionally introduce novel score functions for automatically selecting penalty weights. Our penalized fair regression methods are empirically studied in simulations, where they achieve a fairness-accuracy frontier beyond that of existing comparison methods. Finally, we apply these methods to a national multi-site primary care study of chronic kidney disease to develop a fair classifier for end-stage renal disease. There we find substantial improvements in fairness for multiple race and ethnicity groups who experience societal bias in the health care system without any appreciable loss in overall fit.

