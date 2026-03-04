---
layout: default
title: Joint Training Across Multiple Activation Sparsity Regimes
---

# Joint Training Across Multiple Activation Sparsity Regimes
**arXiv**：[2603.03131v1](https://arxiv.org/abs/2603.03131) · [PDF](https://arxiv.org/pdf/2603.03131.pdf)  
**作者**：Haotian Wang  

**一句话要点**：提出联合训练多激活稀疏度策略以提升深度神经网络泛化能力

**关键词**：激活稀疏化, 泛化能力, 联合训练, top-k约束, 渐进压缩

## 3 点简述
- 核心问题：深度神经网络泛化机制尚不完全明确，生物系统在稀疏激活下表现更强泛化性
- 方法要点：通过全局top-k约束隐藏激活，循环训练模型于不同稀疏度，结合渐进压缩和周期性重置
- 实验或效果：在CIFAR-10无数据增强和WRN-28-4骨干上，自适应保持率策略优于密集基线训练

## 摘要（原文）

> Generalization in deep neural networks remains only partially understood. Inspired by the stronger generalization tendency of biological systems, we explore the hypothesis that robust internal representations should remain effective across both dense and sparse activation regimes. To test this idea, we introduce a simple training strategy that applies global top-k constraints to hidden activations and repeatedly cycles a single model through multiple activation budgets via progressive compression and periodic reset. Using CIFAR-10 without data augmentation and a WRN-28-4 backbone, we find in single-run experiments that two adaptive keep-ratio control strategies both outperform dense baseline training. These preliminary results suggest that joint training across multiple activation sparsity regimes may provide a simple and effective route to improved generalization.

