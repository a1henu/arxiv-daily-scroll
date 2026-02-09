---
layout: default
title: Degradation of Feature Space in Continual Learning
---

# Degradation of Feature Space in Continual Learning
**arXiv**：[2602.06586v1](https://arxiv.org/abs/2602.06586) · [PDF](https://arxiv.org/pdf/2602.06586.pdf)  
**作者**：Chiara Lanza, Roberto Pereira, Marco Miozzo, Eduard Angelats, Paolo Dini  

**一句话要点**：探究特征空间各向同性在持续学习中的影响，发现其可能降低模型精度

**关键词**：持续学习, 特征空间各向异性, 对比学习, 正则化, 灾难性遗忘

## 3 点简述
- 核心问题：持续学习中特征空间趋向各向异性，是否应强制各向同性以平衡稳定性和可塑性？
- 方法要点：使用对比持续学习技术，在CIFAR-10和CIFAR-100上实验各向同性正则化效果。
- 实验或效果：各向同性正则化未能提升模型精度，反而可能降低，表明其不适合非平稳学习场景。

## 摘要（原文）

> Centralized training is the standard paradigm in deep learning, enabling models to learn from a unified dataset in a single location. In such setup, isotropic feature distributions naturally arise as a mean to support well-structured and generalizable representations. In contrast, continual learning operates on streaming and non-stationary data, and trains models incrementally, inherently facing the well-known plasticity-stability dilemma. In such settings, learning dynamics tends to yield increasingly anisotropic feature space. This arises a fundamental question: should isotropy be enforced to achieve a better balance between stability and plasticity, and thereby mitigate catastrophic forgetting? In this paper, we investigate whether promoting feature-space isotropy can enhance representation quality in continual learning. Through experiments using contrastive continual learning techniques on CIFAR-10 and CIFAR-100 data, we find that isotropic regularization fails to improve, and can in fact degrade, model accuracy in continual settings. Our results highlight essential differences in feature geometry between centralized and continual learning, suggesting that isotropy, while beneficial in centralized setups, may not constitute an appropriate inductive bias for non-stationary learning scenarios.

