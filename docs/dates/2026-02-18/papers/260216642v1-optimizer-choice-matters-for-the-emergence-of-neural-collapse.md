---
layout: default
title: Optimizer choice matters for the emergence of Neural Collapse
---

# Optimizer choice matters for the emergence of Neural Collapse
**arXiv**：[2602.16642v1](https://arxiv.org/abs/2602.16642) · [PDF](https://arxiv.org/pdf/2602.16642.pdf)  
**作者**：Jim Zhao, Tin Sum Cheng, Wojciech Masarczyk, Aurelien Lucchi  

**一句话要点**：提出NC0指标以揭示优化器选择对神经崩溃现象的关键影响

**关键词**：神经崩溃, 优化器分析, 权重衰减耦合, 深度学习理论, 隐式偏差

## 3 点简述
- 核心问题：现有理论忽略优化器作用，假设神经崩溃普遍存在
- 方法要点：引入NC0诊断指标，理论证明自适应优化器中解耦权重衰减阻碍神经崩溃
- 实验或效果：3900次训练实验验证理论，首次解释优化器依赖的神经崩溃

## 摘要（原文）

> Neural Collapse (NC) refers to the emergence of highly symmetric geometric structures in the representations of deep neural networks during the terminal phase of training. Despite its prevalence, the theoretical understanding of NC remains limited. Existing analyses largely ignore the role of the optimizer, thereby suggesting that NC is universal across optimization methods. In this work, we challenge this assumption and demonstrate that the choice of optimizer plays a critical role in the emergence of NC. The phenomenon is typically quantified through NC metrics, which, however, are difficult to track and analyze theoretically. To overcome this limitation, we introduce a novel diagnostic metric, NC0, whose convergence to zero is a necessary condition for NC. Using NC0, we provide theoretical evidence that NC cannot emerge under decoupled weight decay in adaptive optimizers, as implemented in AdamW. Concretely, we prove that SGD, SignGD with coupled weight decay (a special case of Adam), and SignGD with decoupled weight decay (a special case of AdamW) exhibit qualitatively different NC0 dynamics. Also, we show the accelerating effect of momentum on NC (beyond convergence of train loss) when trained with SGD, being the first result concerning momentum in the context of NC. Finally, we conduct extensive empirical experiments consisting of 3,900 training runs across various datasets, architectures, optimizers, and hyperparameters, confirming our theoretical results. This work provides the first theoretical explanation for optimizer-dependent emergence of NC and highlights the overlooked role of weight-decay coupling in shaping the implicit biases of optimizers.

