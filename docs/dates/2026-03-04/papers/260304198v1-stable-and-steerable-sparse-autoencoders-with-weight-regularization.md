---
layout: default
title: Stable and Steerable Sparse Autoencoders with Weight Regularization
---

# Stable and Steerable Sparse Autoencoders with Weight Regularization
**arXiv**：[2603.04198v1](https://arxiv.org/abs/2603.04198) · [PDF](https://arxiv.org/pdf/2603.04198.pdf)  
**作者**：Piotr Jedryszek, Oliver M. Crook  

**一句话要点**：提出权重正则化方法以提升稀疏自编码器的稳定性和可操控性

**关键词**：稀疏自编码器, 权重正则化, 特征稳定性, 可操控性, 语言模型

## 3 点简述
- 稀疏自编码器特征学习不稳定，受随机种子和训练选择影响大
- 研究L1和L2权重正则化，结合绑定初始化和单位范数解码器约束
- 在MNIST和语言模型上，L2正则化提高特征一致性和操控成功率

## 摘要（原文）

> Sparse autoencoders (SAEs) are widely used to extract human-interpretable features from neural network activations, but their learned features can vary substantially across random seeds and training choices. To improve stability, we studied weight regularization by adding L1 or L2 penalties on encoder and decoder weights, and evaluate how regularization interacts with common SAE training defaults. On MNIST, we observe that L2 weight regularization produces a core of highly aligned features and, when combined with tied initialization and unit-norm decoder constraints, it dramatically increases cross-seed feature consistency. For TopK SAEs trained on language model activations (Pythia-70M-deduped), adding a small L2 weight penalty increased the fraction of features shared across three random seeds and roughly doubles steering success rates, while leaving the mean of automated interpretability scores essentially unchanged. Finally, in the regularized setting, activation steering success becomes better predicted by auto-interpretability scores, suggesting that regularization can align text-based feature explanations with functional controllability.

