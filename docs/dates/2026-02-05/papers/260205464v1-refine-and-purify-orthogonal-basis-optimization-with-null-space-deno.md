---
layout: default
title: Refine and Purify: Orthogonal Basis Optimization with Null-Space Denoising for Conditional Representation Learning
---

# Refine and Purify: Orthogonal Basis Optimization with Null-Space Denoising for Conditional Representation Learning
**arXiv**：[2602.05464v1](https://arxiv.org/abs/2602.05464) · [PDF](https://arxiv.org/pdf/2602.05464.pdf)  
**作者**：Jiaquan Wang, Yan Lyu, Chen Li, Yuheng Jia  

**一句话要点**：提出OD-CRL框架，通过正交基优化与零空间去噪解决条件表示学习中的子空间敏感性和干扰问题。

**关键词**：条件表示学习, 正交基优化, 零空间去噪, 子空间干扰抑制, 定制化任务

## 3 点简述
- 核心问题：现有方法对子空间基敏感且易受子空间间干扰影响。
- 方法要点：集成自适应正交基优化和零空间去噪投影，提升特征提取精度。
- 实验或效果：在定制化任务中实现最先进性能，具有优越泛化能力。

## 摘要（原文）

> Conditional representation learning aims to extract criterion-specific features for customized tasks. Recent studies project universal features onto the conditional feature subspace spanned by an LLM-generated text basis to obtain conditional representations. However, such methods face two key limitations: sensitivity to subspace basis and vulnerability to inter-subspace interference. To address these challenges, we propose OD-CRL, a novel framework integrating Adaptive Orthogonal Basis Optimization (AOBO) and Null-Space Denoising Projection (NSDP). Specifically, AOBO constructs orthogonal semantic bases via singular value decomposition with a curvature-based truncation. NSDP suppresses non-target semantic interference by projecting embeddings onto the null space of irrelevant subspaces. Extensive experiments conducted across customized clustering, customized classification, and customized retrieval tasks demonstrate that OD-CRL achieves a new state-of-the-art performance with superior generalization.

