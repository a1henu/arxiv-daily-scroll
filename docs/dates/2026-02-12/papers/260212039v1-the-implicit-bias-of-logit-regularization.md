---
layout: default
title: The Implicit Bias of Logit Regularization
---

# The Implicit Bias of Logit Regularization
**arXiv**：[2602.12039v1](https://arxiv.org/abs/2602.12039) · [PDF](https://arxiv.org/pdf/2602.12039.pdf)  
**作者**：Alon Beck, Yohai Bar Sinai, Noam Levi  

**一句话要点**：分析Logit正则化在线性分类中的隐式偏差，揭示其驱动权重对齐Fisher线性判别式

**关键词**：Logit正则化, 隐式偏差, 线性分类, Fisher线性判别式, 泛化鲁棒性, 标签平滑

## 3 点简述
- 研究Logit正则化（如标签平滑）在分类中的机制，聚焦其隐式偏差
- 证明在高斯数据或Logit聚类条件下，正则化使权重向量精确对齐Fisher线性判别式
- 在信号加噪声模型中，正则化降低临界样本复杂度，增强泛化鲁棒性

## 摘要（原文）

> Logit regularization, the addition a convex penalty directly in logit space, is widely used in modern classifiers, with label smoothing as a prominent example. While such methods often improve calibration and generalization, their mechanism remains under-explored. In this work, we analyze a general class of such logit regularizers in the context of linear classification, and demonstrate that they induce an implicit bias of logit clustering around finite per-sample targets. For Gaussian data, or whenever logits are sufficiently clustered, we prove that logit clustering drives the weight vector to align exactly with Fisher's Linear Discriminant. To demonstrate the consequences, we study a simple signal-plus-noise model in which this transition has dramatic effects: Logit regularization halves the critical sample complexity and induces grokking in the small-noise limit, while making generalization robust to noise. Our results extend the theoretical understanding of label smoothing and highlight the efficacy of a broader class of logit-regularization methods.

