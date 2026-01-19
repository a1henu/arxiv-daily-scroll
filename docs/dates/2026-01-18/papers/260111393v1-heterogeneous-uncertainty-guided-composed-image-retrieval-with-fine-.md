---
layout: default
title: Heterogeneous Uncertainty-Guided Composed Image Retrieval with Fine-Grained Probabilistic Learning
---

# Heterogeneous Uncertainty-Guided Composed Image Retrieval with Fine-Grained Probabilistic Learning
**arXiv**：[2601.11393v1](https://arxiv.org/abs/2601.11393) · [PDF](https://arxiv.org/pdf/2601.11393.pdf)  
**作者**：Haomiao Tang, Jinpeng Wang, Minyi Zhao, Guanghao Meng, Ruisheng Luo, Long Chen, Shu-Tao Xia  

**一句话要点**：提出异构不确定性引导的细粒度概率学习框架，以解决组合图像检索中的噪声和鲁棒性问题。

**关键词**：组合图像检索, 概率学习, 不确定性估计, 多模态协调, 细粒度学习, 负采样策略

## 3 点简述
- 核心问题：组合图像检索中三元组噪声导致内在不确定性，现有概率方法因实例级整体建模和同质处理查询与目标而不足。
- 方法要点：采用细粒度概率学习，为查询和目标定制异构不确定性估计，包括多模态协调和动态加权机制。
- 实验或效果：在基准测试中超越现有方法，通过不确定性引导目标和负采样策略增强判别性学习。

## 摘要（原文）

> Composed Image Retrieval (CIR) enables image search by combining a reference image with modification text. Intrinsic noise in CIR triplets incurs intrinsic uncertainty and threatens the model's robustness. Probabilistic learning approaches have shown promise in addressing such issues; however, they fall short for CIR due to their instance-level holistic modeling and homogeneous treatment of queries and targets. This paper introduces a Heterogeneous Uncertainty-Guided (HUG) paradigm to overcome these limitations. HUG utilizes a fine-grained probabilistic learning framework, where queries and targets are represented by Gaussian embeddings that capture detailed concepts and uncertainties. We customize heterogeneous uncertainty estimations for multi-modal queries and uni-modal targets. Given a query, we capture uncertainties not only regarding uni-modal content quality but also multi-modal coordination, followed by a provable dynamic weighting mechanism to derive comprehensive query uncertainty. We further design uncertainty-guided objectives, including query-target holistic contrast and fine-grained contrasts with comprehensive negative sampling strategies, which effectively enhance discriminative learning. Experiments on benchmarks demonstrate HUG's effectiveness beyond state-of-the-art baselines, with faithful analysis justifying the technical contributions.

