---
layout: default
title: From Core to Detail: Unsupervised Disentanglement with Entropy-Ordered Flows
---

# From Core to Detail: Unsupervised Disentanglement with Entropy-Ordered Flows
**arXiv**：[2602.06940v1](https://arxiv.org/abs/2602.06940) · [PDF](https://arxiv.org/pdf/2602.06940.pdf)  
**作者**：Daniel Galperin, Ullrich Köthe  

**一句话要点**：提出熵序流以解决无监督表示学习中语义稳定性和细节分离的挑战

**关键词**：无监督表示学习, 熵序流, 归一化流, 语义可解释性, 自适应压缩, 去噪

## 3 点简述
- 核心问题：无监督表示学习需实现语义稳定且可解释的表示，避免运行间波动
- 方法要点：基于熵排序的归一化流框架，通过熵排序实现自适应注入流，支持推理时灵活选择核心维度
- 实验或效果：在CelebA数据集上验证，能发现语义可解释特征，支持高压缩和强去噪

## 摘要（原文）

> Learning unsupervised representations that are both semantically meaningful and stable across runs remains a central challenge in modern representation learning. We introduce entropy-ordered flows (EOFlows), a normalizing-flow framework that orders latent dimensions by their explained entropy, analogously to PCA's explained variance. This ordering enables adaptive injective flows: after training, one may retain only the top C latent variables to form a compact core representation while the remaining variables capture fine-grained detail and noise, with C chosen flexibly at inference time rather than fixed during training. EOFlows build on insights from Independent Mechanism Analysis, Principal Component Flows and Manifold Entropic Metrics. We combine likelihood-based training with local Jacobian regularization and noise augmentation into a method that scales well to high-dimensional data such as images. Experiments on the CelebA dataset show that our method uncovers a rich set of semantically interpretable features, allowing for high compression and strong denoising.

