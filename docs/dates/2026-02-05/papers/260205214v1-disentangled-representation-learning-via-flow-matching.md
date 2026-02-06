---
layout: default
title: Disentangled Representation Learning via Flow Matching
---

# Disentangled Representation Learning via Flow Matching
**arXiv**：[2602.05214v1](https://arxiv.org/abs/2602.05214) · [PDF](https://arxiv.org/pdf/2602.05214.pdf)  
**作者**：Jinjin Chi, Taoping Liu, Mengtao Yin, Ximing Li, Yongcheng Jing, Dacheng Tao  

**一句话要点**：提出基于流匹配的框架以解决解耦表示学习中语义对齐不足的问题

**关键词**：解耦表示学习, 流匹配, 语义对齐, 因子条件流, 非重叠正则化

## 3 点简述
- 核心问题：现有扩散方法在解耦表示学习中常缺乏强语义对齐，导致因子间干扰和信息泄露
- 方法要点：通过因子条件流在紧凑潜在空间中学习解耦表示，并引入非重叠正则化器抑制跨因子干扰
- 实验或效果：在多个数据集上实验显示，相比基线方法，本框架在解耦分数、可控性和样本保真度方面均有提升

## 摘要（原文）

> Disentangled representation learning aims to capture the underlying explanatory factors of observed data, enabling a principled understanding of the data-generating process. Recent advances in generative modeling have introduced new paradigms for learning such representations. However, existing diffusion-based methods encourage factor independence via inductive biases, yet frequently lack strong semantic alignment. In this work, we propose a flow matching-based framework for disentangled representation learning, which casts disentanglement as learning factor-conditioned flows in a compact latent space. To enforce explicit semantic alignment, we introduce a non-overlap (orthogonality) regularizer that suppresses cross-factor interference and reduces information leakage between factors. Extensive experiments across multiple datasets demonstrate consistent improvements over representative baselines, yielding higher disentanglement scores as well as improved controllability and sample fidelity.

