---
layout: default
title: InfoNCE Induces Gaussian Distribution
---

# InfoNCE Induces Gaussian Distribution
**arXiv**：[2602.24012v1](https://arxiv.org/abs/2602.24012) · [PDF](https://arxiv.org/pdf/2602.24012.pdf)  
**作者**：Roy Betser, Eyal Gofer, Meir Yossef Levi, Guy Gilboa  

**一句话要点**：揭示InfoNCE损失在对比学习中诱导表示呈高斯分布

**关键词**：对比学习, InfoNCE损失, 高斯分布, 表示学习, 理论分析

## 3 点简述
- 核心问题：对比学习表示常呈高斯分布，但缺乏理论解释
- 方法要点：在特定假设下，证明InfoNCE损失诱导表示渐近趋近高斯分布
- 实验或效果：在合成和CIFAR-10数据集上验证高斯行为，支持理论分析

## 摘要（原文）

> Contrastive learning has become a cornerstone of modern representation learning, allowing training with massive unlabeled data for both task-specific and general (foundation) models. A prototypical loss in contrastive training is InfoNCE and its variants. In this work, we show that the InfoNCE objective induces Gaussian structure in representations that emerge from contrastive training. We establish this result in two complementary regimes. First, we show that under certain alignment and concentration assumptions, projections of the high-dimensional representation asymptotically approach a multivariate Gaussian distribution. Next, under less strict assumptions, we show that adding a small asymptotically vanishing regularization term that promotes low feature norm and high feature entropy leads to similar asymptotic results. We support our analysis with experiments on synthetic and CIFAR-10 datasets across multiple encoder architectures and sizes, demonstrating consistent Gaussian behavior. This perspective provides a principled explanation for commonly observed Gaussianity in contrastive representations. The resulting Gaussian model enables principled analytical treatment of learned representations and is expected to support a wide range of applications in contrastive learning.

