---
layout: default
title: Rethinking Transferable Adversarial Attacks on Point Clouds from a Compact Subspace Perspective
---

# Rethinking Transferable Adversarial Attacks on Point Clouds from a Compact Subspace Perspective
**arXiv**：[2601.23102v1](https://arxiv.org/abs/2601.23102) · [PDF](https://arxiv.org/pdf/2601.23102.pdf)  
**作者**：Keke Tang, Xianheng Liu, Weilong Peng, Xiaofei Wang, Daizong Liu, Peican Zhu, Can Lu, Zhihong Tian  

**一句话要点**：提出CoSA框架，从紧凑子空间视角提升点云对抗攻击的跨模型可迁移性。

**关键词**：点云对抗攻击, 可迁移性, 紧凑子空间, 低维语义表示, 跨模型泛化

## 3 点简述
- 核心问题：点云对抗攻击可迁移性差，现有方法依赖模型特定梯度或启发式，泛化受限。
- 方法要点：在共享低维语义空间中，用类特定原型表示点云，在低秩子空间优化扰动以抑制模型依赖噪声。
- 实验或效果：在多个数据集和网络架构上，CoSA优于先进方法，保持不可感知性和防御鲁棒性。

## 摘要（原文）

> Transferable adversarial attacks on point clouds remain challenging, as existing methods often rely on model-specific gradients or heuristics that limit generalization to unseen architectures. In this paper, we rethink adversarial transferability from a compact subspace perspective and propose CoSA, a transferable attack framework that operates within a shared low-dimensional semantic space. Specifically, each point cloud is represented as a compact combination of class-specific prototypes that capture shared semantic structure, while adversarial perturbations are optimized within a low-rank subspace to induce coherent and architecture-agnostic variations. This design suppresses model-dependent noise and constrains perturbations to semantically meaningful directions, thereby improving cross-model transferability without relying on surrogate-specific artifacts. Extensive experiments on multiple datasets and network architectures demonstrate that CoSA consistently outperforms state-of-the-art transferable attacks, while maintaining competitive imperceptibility and robustness under common defense strategies. Codes will be made public upon paper acceptance.

