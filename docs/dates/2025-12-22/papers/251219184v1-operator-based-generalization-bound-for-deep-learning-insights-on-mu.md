---
layout: default
title: Operator-Based Generalization Bound for Deep Learning: Insights on Multi-Task Learning
---

# Operator-Based Generalization Bound for Deep Learning: Insights on Multi-Task Learning
**arXiv**：[2512.19184v1](https://arxiv.org/abs/2512.19184) · [PDF](https://arxiv.org/pdf/2512.19184.pdf)  
**作者**：Mahdi Mohammadigohari, Giuseppe Di Fatta, Giuseppe Nicosia, Panos M. Pardalos  

**一句话要点**：提出基于算子的泛化界以增强多任务深度学习性能

**关键词**：多任务学习, 泛化界, 向量值神经网络, Koopman算子, 深度核方法, 草图技术

## 3 点简述
- 核心问题：多任务学习中向量值神经网络的泛化性能分析不足
- 方法要点：结合Koopman算子与草图技术，推导更紧的泛化界
- 实验或效果：应用于鲁棒和多重分位数回归，提供性能保证

## 摘要（原文）

> This paper presents novel generalization bounds for vector-valued neural networks and deep kernel methods, focusing on multi-task learning through an operator-theoretic framework. Our key development lies in strategically combining a Koopman based approach with existing techniques, achieving tighter generalization guarantees compared to traditional norm-based bounds. To mitigate computational challenges associated with Koopman-based methods, we introduce sketching techniques applicable to vector valued neural networks. These techniques yield excess risk bounds under generic Lipschitz losses, providing performance guarantees for applications including robust and multiple quantile regression. Furthermore, we propose a novel deep learning framework, deep vector-valued reproducing kernel Hilbert spaces (vvRKHS), leveraging Perron Frobenius (PF) operators to enhance deep kernel methods. We derive a new Rademacher generalization bound for this framework, explicitly addressing underfitting and overfitting through kernel refinement strategies. This work offers novel insights into the generalization properties of multitask learning with deep learning architectures, an area that has been relatively unexplored until recent developments.

