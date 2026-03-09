---
layout: default
title: Weak-SIGReg: Covariance Regularization for Stable Deep Learning
---

# Weak-SIGReg: Covariance Regularization for Stable Deep Learning
**arXiv**：[2603.05924v1](https://arxiv.org/abs/2603.05924) · [PDF](https://arxiv.org/pdf/2603.05924.pdf)  
**作者**：Habibullah Akbar  

**一句话要点**：提出Weak-SIGReg正则化方法，通过协方差约束稳定深度学习优化，解决低数据或低偏置架构的训练崩溃问题。

**关键词**：优化正则化, 协方差约束, 训练稳定性, Vision Transformers, 深度学习优化

## 3 点简述
- 核心问题：低偏置架构如Vision Transformers在无架构先验或低数据增强下易发生优化崩溃。
- 方法要点：基于SIGReg，推导Weak-SIGReg，通过随机草图技术正则化协方差矩阵，约束表示密度向各向同性高斯分布。
- 实验或效果：在CIFAR-100上，将ViT准确率从20.73%提升至72.02%，并改善深度MLP的SGD收敛。

## 摘要（原文）

> Modern neural network optimization relies heavily on architectural priorssuch as Batch Normalization and Residual connectionsto stabilize training dynamics. Without these, or in low-data regimes with aggressive augmentation, low-bias architectures like Vision Transformers (ViTs) often suffer from optimization collapse. This work adopts Sketched Isotropic Gaussian Regularization (SIGReg), recently introduced in the LeJEPA self-supervised framework, and repurposes it as a general optimization stabilizer for supervised learning. While the original formulation targets the full characteristic function, a computationally efficient variant is derived, Weak-SIGReg, which targets the covariance matrix via random sketching. Inspired by interacting particle systems, representation collapse is viewed as stochastic drift; SIGReg constrains the representation density towards an isotropic Gaussian, mitigating this drift. Empirically, SIGReg recovers the training of a ViT on CIFAR-100 from a collapsed 20.73\% to 72.02\% accuracy without architectural hacks and significantly improves the convergence of deep vanilla MLPs trained with pure SGD. Code is available at \href{https://github.com/kreasof-ai/sigreg}{github.com/kreasof-ai/sigreg}.

