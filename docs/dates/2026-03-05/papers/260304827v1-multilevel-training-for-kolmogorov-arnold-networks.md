---
layout: default
title: Multilevel Training for Kolmogorov Arnold Networks
---

# Multilevel Training for Kolmogorov Arnold Networks
**arXiv**：[2603.04827v1](https://arxiv.org/abs/2603.04827) · [PDF](https://arxiv.org/pdf/2603.04827.pdf)  
**作者**：Ben S. Southworth, Jonas A. Actor, Graham Harper, Eric C. Cyr  

**一句话要点**：提出多级训练方法以加速Kolmogorov-Arnold网络训练，提升物理信息神经网络性能

**关键词**：Kolmogorov-Arnold网络, 多级训练, 样条基函数, 物理信息神经网络, 梯度优化, 基变换

## 3 点简述
- 核心问题：传统神经网络训练因缺乏结构保证而难以加速，KANs提供更多结构但训练效率仍待提升
- 方法要点：通过基变换建立KANs与MLPs等价性，利用样条基函数结构设计多级训练算法，实现模型间几何插值
- 实验或效果：数值实验显示多级训练在精度上比传统方法提升多个数量级，尤其适用于物理信息神经网络

## 摘要（原文）

> Algorithmic speedup of training common neural architectures is made difficult by the lack of structure guaranteed by the function compositions inherent to such networks. In contrast to multilayer perceptrons (MLPs), Kolmogorov-Arnold networks (KANs) provide more structure by expanding learned activations in a specified basis. This paper exploits this structure to develop practical algorithms and theoretical insights, yielding training speedup via multilevel training for KANs. To do so, we first establish an equivalence between KANs with spline basis functions and multichannel MLPs with power ReLU activations through a linear change of basis. We then analyze how this change of basis affects the geometry of gradient-based optimization with respect to spline knots. The KANs change-of-basis motivates a multilevel training approach, where we train a sequence of KANs naturally defined through a uniform refinement of spline knots with analytic geometric interpolation operators between models. The interpolation scheme enables a ``properly nested hierarchy'' of architectures, ensuring that interpolation to a fine model preserves the progress made on coarse models, while the compact support of spline basis functions ensures complementary optimization on subsequent levels. Numerical experiments demonstrate that our multilevel training approach can achieve orders of magnitude improvement in accuracy over conventional methods to train comparable KANs or MLPs, particularly for physics informed neural networks. Finally, this work demonstrates how principled design of neural networks can lead to exploitable structure, and in this case, multilevel algorithms that can dramatically improve training performance.

