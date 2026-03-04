---
layout: default
title: Information Routing in Atomistic Foundation Models: How Equivariance Creates Linearly Disentangled Representations
---

# Information Routing in Atomistic Foundation Models: How Equivariance Creates Linearly Disentangled Representations
**arXiv**：[2603.03155v1](https://arxiv.org/abs/2603.03155) · [PDF](https://arxiv.org/pdf/2603.03155.pdf)  
**作者**：Joshua Steier  

**一句话要点**：提出成分投影分解方法，揭示原子基础模型中张量积等变架构如何线性解耦几何与成分信息。

**关键词**：原子基础模型, 表示解耦, 等变架构, 线性探针, 成分投影分解, 几何信息

## 3 点简述
- 核心问题：原子基础模型的中间表示如何组织和编码信息，特别是几何与成分的分离程度。
- 方法要点：使用QR投影线性移除成分信号，通过线性探针分析几何残差，评估表示的解耦性。
- 实验或效果：在QM9分子和Materials Project晶体上测试八种模型，发现张量积等变架构（如MACE）能线性解耦几何信息，而手工描述符（如ANI-2x）则非线性纠缠。

## 摘要（原文）

> What do atomistic foundation models encode in their intermediate representations, and how is that information organized? We introduce Composition Projection Decomposition (CPD), which uses QR projection to linearly remove composition signal from learned representations and probes the geometric residual. Across eight models from five architectural families on QM9 molecules and Materials Project crystals, we find a disentanglement gradient: tensor product equivariant architectures (MACE) produce representations where geometry is almost fully linearly accessible after composition removal ($R^2_{\text{geom}} = 0.782$ for HOMO-LUMO gap), while handcrafted descriptors (ANI-2x) entangle the same information nonlinearly ($R^2_{\text{geom}} = -0.792$ under Ridge; $R^2 = +0.784$ under MLP). MACE routes target-specific signal through irreducible representation channels -- dipole to $L = 1$, HOMO-LUMO gap to $L = 0$ -- a pattern not observed in ViSNet's vector-scalar architecture under the same probe. We show that gradient boosted tree probes on projected residuals are systematically inflated, recovering $R^2 = 0.68$--$0.95$ on a purely compositional target, and recommend linear probes as the primary metric. Linearly disentangled representations are more sample-efficient under linear probing, suggesting a practical advantage for equivariant architectures beyond raw prediction accuracy.

