---
layout: default
title: Spectral Manifold Regularization for Stable and Modular Routing in Deep MoE Architectures
---

# Spectral Manifold Regularization for Stable and Modular Routing in Deep MoE Architectures
**arXiv**：[2601.03889v1](https://arxiv.org/abs/2601.03889) · [PDF](https://arxiv.org/pdf/2601.03889.pdf)  
**作者**：Ibrahim Delibasoglu  

**一句话要点**：提出谱正则化混合专家模型以解决专家崩溃和适应干扰问题

**关键词**：混合专家模型, 谱正则化, 路由稳定性, 模块化网络, 终身学习

## 3 点简述
- 核心问题：MoE架构中专家崩溃导致模型容量降低和适应时灾难性干扰
- 方法要点：通过谱范数约束和稳定秩惩罚施加几何约束，增强路由结构模块性
- 实验或效果：在模块化单次适应任务中，SR-MoE保持结构完整性，减少干扰

## 摘要（原文）

> Mixture of Experts (MoE) architectures enable efficient scaling of neural networks but suffer from expert collapse, where routing converges to a few dominant experts. This reduces model capacity and causes catastrophic interference during adaptation. We propose the Spectrally-Regularized Mixture of Experts (SR-MoE), which imposes geometric constraints on the routing manifold to enforce structural modularity. Our method uses dual regularization: spectral norm constraints bound routing function Lipschitz continuity, while stable rank penalties preserve high-dimensional feature diversity in expert selection. We evaluate SR-MoE across architectural scales and dataset complexities using modular one-shot adaptation tasks. Results show that traditional linear gating fails with increasing depth (accuracy drops up to 4.72% due to expert entanglement), while SR-MoE maintains structural integrity (mean interference -0.32%). Our spectral constraints facilitate positive knowledge transfer, enabling localized expert updates without global performance decay. SR-MoE provides a general solution for building high-capacity, modular networks capable of stable lifelong learning.

