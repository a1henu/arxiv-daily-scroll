---
layout: default
title: Inverting Self-Organizing Maps: A Unified Activation-Based Framework
---

# Inverting Self-Organizing Maps: A Unified Activation-Based Framework
**arXiv**：[2601.13851v1](https://arxiv.org/abs/2601.13851) · [PDF](https://arxiv.org/pdf/2601.13851.pdf)  
**作者**：Alessandro Londei, Matteo Benati, Denise Lanzieri, Vittorio Loreto  

**一句话要点**：提出基于自组织映射激活模式的反演框架，实现精确输入恢复与可控语义轨迹生成

**关键词**：自组织映射反演, 激活模式分析, 可控语义轨迹, 数据流形探索, 欧氏距离几何, 确定性更新规则

## 3 点简述
- 核心问题：自组织映射的激活模式（到原型的平方距离）能否反演以恢复输入，并用于可控数据探索
- 方法要点：利用欧氏距离几何理论，推导线性系统，引入MUSIC更新规则，通过修改平方距离实现确定性几何流
- 实验或效果：在合成高斯混合、MNIST和Faces in the Wild数据集上验证，生成平滑、可解释的轨迹，揭示学习流形几何

## 摘要（原文）

> Self-Organizing Maps provide topology-preserving projections of high-dimensional data and have been widely used for visualization, clustering, and vector quantization. In this work, we show that the activation pattern of a SOM - the squared distances to its prototypes - can be inverted to recover the exact input under mild geometric conditions. This follows from a classical fact in Euclidean distance geometry: a point in $D$ dimensions is uniquely determined by its distances to $D{+}1$ affinely independent references. We derive the corresponding linear system and characterize the conditions under which the inversion is well-posed. Building upon this mechanism, we introduce the Manifold-Aware Unified SOM Inversion and Control (MUSIC) update rule, which enables controlled, semantically meaningful trajectories in latent space. MUSIC modifies squared distances to selected prototypes while preserving others, resulting in a deterministic geometric flow aligned with the SOM's piecewise-linear structure. Tikhonov regularization stabilizes the update rule and ensures smooth motion on high-dimensional datasets. Unlike variational or probabilistic generative models, MUSIC does not rely on sampling, latent priors, or encoder-decoder architectures. If no perturbation is applied, inversion recovers the exact input; when a target cluster or prototype is specified, MUSIC produces coherent semantic variations while remaining on the data manifold. This leads to a new perspective on data augmentation and controllable latent exploration based solely on prototype geometry. We validate the approach using synthetic Gaussian mixtures, the MNIST and the Faces in the Wild dataset. Across all settings, MUSIC produces smooth, interpretable trajectories that reveal the underlying geometry of the learned manifold, illustrating the advantages of SOM-based inversion over unsupervised clustering.

