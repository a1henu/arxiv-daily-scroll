---
layout: default
title: DynaMoE: Dynamic Token-Level Expert Activation with Layer-Wise Adaptive Capacity for Mixture-of-Experts Neural Networks
---

# DynaMoE: Dynamic Token-Level Expert Activation with Layer-Wise Adaptive Capacity for Mixture-of-Experts Neural Networks
**arXiv**：[2603.01697v1](https://arxiv.org/abs/2603.01697) · [PDF](https://arxiv.org/pdf/2603.01697.pdf)  
**作者**：Gökdeniz Gülmez  

**一句话要点**：提出DynaMoE框架，通过动态路由和层间自适应容量分配提升混合专家网络的效率与性能。

**关键词**：混合专家网络, 动态路由, 自适应容量分配, 参数效率, 梯度方差优化, 神经网络架构设计

## 3 点简述
- 核心问题：标准MoE架构依赖固定Top-K路由和均匀层间专家分配，限制了灵活性与效率。
- 方法要点：引入动态令牌级专家激活，基于输入复杂度调整激活专家数；实施六种层间容量调度策略，如降序、升序和金字塔模式。
- 实验或效果：在图像分类和语言建模任务上，DynaMoE优于静态基线，参数效率更高，且最优调度策略依赖任务和模型规模。

## 摘要（原文）

> Mixture-of-Experts (MoE) architectures have emerged as a powerful paradigm for scaling neural networks while maintaining computational efficiency. However, standard MoE implementations rely on two rigid design assumptions: (1) fixed Top-K routing where exactly K experts are activated per token, and (2) uniform expert allocation across all layers. This paper introduces DynaMoE, a novel MoE framework that relaxes both constraints through dynamic token-level expert activation and layer-wise adaptive capacity allocation. DynaMoE introduces a principled routing mechanism where the number of active experts per token varies based on input complexity. Concurrently, the framework implements six distinct scheduling strategies for distributing expert capacity across network depth, including descending, ascending, pyramid, and wave patterns. We theoretically analyze the expressivity gains of dynamic routing and derive bounds on computational efficiency. Through extensive experiments on MNIST, Fashion-MNIST, CIFAR-10 (image classification), and Recycling-the-Web (language modeling) across multiple model scales, we demonstrate that DynaMoE achieves superior parameter efficiency compared to static baselines. Our key finding is that optimal expert schedules are task- and scale-dependent: descending schedules (concentrating capacity in early layers) outperform uniform baselines on image classification. For language modeling, optimal schedules vary by model size, descending for Tiny, ascending for Small, and uniform for Medium. Furthermore, dynamic routing reduces gradient variance during training, leading to improved convergence stability. DynaMoE establishes a new framework for adaptive computation in neural networks, providing principled guidance for MoE architecture design.

