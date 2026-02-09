---
layout: default
title: Robustness Beyond Known Groups with Low-rank Adaptation
---

# Robustness Beyond Known Groups with Low-rank Adaptation
**arXiv**：[2602.06924v1](https://arxiv.org/abs/2602.06924) · [PDF](https://arxiv.org/pdf/2602.06924.pdf)  
**作者**：Abinitha Gourabathina, Hyewon Jeong, Teya Bergamaschi, Marzyeh Ghassemi, Collin Stultz  

**一句话要点**：提出LEIA方法以提升深度学习模型在未知敏感子群体上的鲁棒性

**关键词**：群体鲁棒性, 低秩适配, 未知子群体, 模型错误分析, 表示空间

## 3 点简述
- 核心问题：模型在未知子群体上存在系统性失败，现有方法需先验知识
- 方法要点：通过低秩调整分类器logits，在表示空间错误集中子空间进行适配
- 实验或效果：在五种真实数据集上，LEIA一致提升最差群体性能，参数高效且超参数鲁棒

## 摘要（原文）

> Deep learning models trained to optimize average accuracy often exhibit systematic failures on particular subpopulations. In real world settings, the subpopulations most affected by such disparities are frequently unlabeled or unknown, thereby motivating the development of methods that are performant on sensitive subgroups without being pre-specified. However, existing group-robust methods typically assume prior knowledge of relevant subgroups, using group annotations for training or model selection. We propose Low-rank Error Informed Adaptation (LEIA), a simple two-stage method that improves group robustness by identifying a low-dimensional subspace in the representation space where model errors concentrate. LEIA restricts adaptation to this error-informed subspace via a low-rank adjustment to the classifier logits, directly targeting latent failure modes without modifying the backbone or requiring group labels. Using five real-world datasets, we analyze group robustness under three settings: (1) truly no knowledge of subgroup relevance, (2) partial knowledge of subgroup relevance, and (3) full knowledge of subgroup relevance. Across all settings, LEIA consistently improves worst-group performance while remaining fast, parameter-efficient, and robust to hyperparameter choice.

