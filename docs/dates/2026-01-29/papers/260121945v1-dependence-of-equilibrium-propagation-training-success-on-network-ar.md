---
layout: default
title: Dependence of Equilibrium Propagation Training Success on Network Architecture
---

# Dependence of Equilibrium Propagation Training Success on Network Architecture
**arXiv**：[2601.21945v1](https://arxiv.org/abs/2601.21945) · [PDF](https://arxiv.org/pdf/2601.21945.pdf)  
**作者**：Qingshan Wang, Clara C. Wanjura, Florian Marquardt  

**一句话要点**：研究平衡传播训练在局部连接网络中的性能，为现实架构提供指导

**关键词**：平衡传播训练, 局部连接网络, 神经形态计算, XY模型, 架构优化

## 3 点简述
- 核心问题：AI能耗增长推动神经形态计算，但现有研究多基于密集网络，难以实验实现。
- 方法要点：使用平衡传播训练XY模型，探索局部连接晶格架构对训练性能的影响。
- 实验或效果：稀疏局部连接网络性能可比密集网络，为现实设置中的架构扩展提供依据。

## 摘要（原文）

> The rapid rise of artificial intelligence has led to an unsustainable growth in energy consumption. This has motivated progress in neuromorphic computing and physics-based training of learning machines as alternatives to digital neural networks. Many theoretical studies focus on simple architectures like all-to-all or densely connected layered networks. However, these may be challenging to realize experimentally, e.g. due to connectivity constraints. In this work, we investigate the performance of the widespread physics-based training method of equilibrium propagation for more realistic architectural choices, specifically, locally connected lattices. We train an XY model and explore the influence of architecture on various benchmark tasks, tracking the evolution of spatially distributed responses and couplings during training. Our results show that sparse networks with only local connections can achieve performance comparable to dense networks. Our findings provide guidelines for further scaling up architectures based on equilibrium propagation in realistic settings.

