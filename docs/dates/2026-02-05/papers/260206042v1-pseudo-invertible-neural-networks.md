---
layout: default
title: Pseudo-Invertible Neural Networks
---

# Pseudo-Invertible Neural Networks
**arXiv**：[2602.06042v1](https://arxiv.org/abs/2602.06042) · [PDF](https://arxiv.org/pdf/2602.06042.pdf)  
**作者**：Yamit Ehrlich, Nimrod Berman, Assaf Shocher  

**一句话要点**：提出伪可逆神经网络以扩展零样本逆问题至非线性退化场景

**关键词**：伪可逆神经网络, 非线性伪逆, 零样本逆问题, 扩散模型, 非线性退化, 语义控制

## 3 点简述
- 核心问题：将线性伪逆推广至非线性映射，解决非线性信息损失下的逆问题
- 方法要点：设计具有可处理非线性伪逆的满射伪可逆神经网络架构
- 实验或效果：应用于零样本逆问题，支持复杂退化如光学畸变和语义抽象的控制

## 摘要（原文）

> The Moore-Penrose Pseudo-inverse (PInv) serves as the fundamental solution for linear systems. In this paper, we propose a natural generalization of PInv to the nonlinear regime in general and to neural networks in particular. We introduce Surjective Pseudo-invertible Neural Networks (SPNN), a class of architectures explicitly designed to admit a tractable non-linear PInv. The proposed non-linear PInv and its implementation in SPNN satisfy fundamental geometric properties. One such property is null-space projection or "Back-Projection", $x' = x + A^\dagger(y-Ax)$, which moves a sample $x$ to its closest consistent state $x'$ satisfying $Ax=y$. We formalize Non-Linear Back-Projection (NLBP), a method that guarantees the same consistency constraint for non-linear mappings $f(x)=y$ via our defined PInv. We leverage SPNNs to expand the scope of zero-shot inverse problems. Diffusion-based null-space projection has revolutionized zero-shot solving for linear inverse problems by exploiting closed-form back-projection. We extend this method to non-linear degradations. Here, "degradation" is broadly generalized to include any non-linear loss of information, spanning from optical distortions to semantic abstractions like classification. This approach enables zero-shot inversion of complex degradations and allows precise semantic control over generative outputs without retraining the diffusion prior.

