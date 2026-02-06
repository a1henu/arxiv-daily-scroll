---
layout: default
title: Joint Embedding Variational Bayes
---

# Joint Embedding Variational Bayes
**arXiv**：[2602.05639v1](https://arxiv.org/abs/2602.05639) · [PDF](https://arxiv.org/pdf/2602.05639.pdf)  
**作者**：Amin Oji, Paul Fieguth  

**一句话要点**：提出变分联合嵌入框架，在非对比自监督学习中实现概率表示学习

**关键词**：变分推断, 自监督学习, 概率表示, 非对比学习, 异常检测

## 3 点简述
- 核心问题：传统基于能量的预测目标优化点间差异，缺乏概率建模能力，可能导致训练不稳定。
- 方法要点：通过变分推断最大化对称条件证据下界，使用学生t分布解耦方向和径向因子以防止范数诱导的不稳定性。
- 实验或效果：在ImageNet-1K等数据集上性能与标准非对比基线相当，并在异常检测中基于似然评分优于可比自监督方法。

## 摘要（原文）

> We introduce Variational Joint Embedding (VJE), a framework that synthesizes joint embedding and variational inference to enable self-supervised learning of probabilistic representations in a reconstruction-free, non-contrastive setting. Compared to energy-based predictive objectives that optimize pointwise discrepancies, VJE maximizes a symmetric conditional evidence lower bound (ELBO) for a latent-variable model defined directly on encoder embeddings. We instantiate the conditional likelihood with a heavy-tailed Student-$t$ model using a polar decomposition that explicitly decouples directional and radial factors to prevent norm-induced instabilities during training. VJE employs an amortized inference network to parameterize a diagonal Gaussian variational posterior whose feature-wise variances are shared with the likelihood scale to capture anisotropic uncertainty without auxiliary projection heads. Across ImageNet-1K, CIFAR-10/100, and STL-10, VJE achieves performance comparable to standard non-contrastive baselines under linear and k-NN evaluation. We further validate these probabilistic semantics through one-class CIFAR-10 anomaly detection, where likelihood-based scoring under the proposed model outperforms comparable self-supervised baselines.

