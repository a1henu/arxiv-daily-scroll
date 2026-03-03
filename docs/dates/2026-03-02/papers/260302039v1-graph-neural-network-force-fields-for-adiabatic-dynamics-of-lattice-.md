---
layout: default
title: Graph neural network force fields for adiabatic dynamics of lattice Hamiltonians
---

# Graph neural network force fields for adiabatic dynamics of lattice Hamiltonians
**arXiv**：[2603.02039v1](https://arxiv.org/abs/2603.02039) · [PDF](https://arxiv.org/pdf/2603.02039.pdf)  
**作者**：Yunhao Fan, Gia-Wei Chern  

**一句话要点**：提出图神经网络力场框架，用于晶格哈密顿量的绝热动力学模拟，实现对称性一致和大规模计算。

**关键词**：图神经网络力场, 晶格哈密顿量, 绝热动力学, 对称性强制执行, 大规模模拟, 电荷密度波

## 3 点简述
- 核心问题：晶格系统量子精确模拟需可扩展且对称性一致的力场模型，传统方法依赖复杂特征工程。
- 方法要点：利用图神经网络通过局部消息传递和权重共享直接强制执行离散平移和点群对称性，简化架构。
- 实验或效果：在半经典Holstein模型上训练，实现高精度力预测、线性系统规模扩展和大规模朗之万模拟，揭示电荷密度波有序的动力学标度行为。

## 摘要（原文）

> Scalable and symmetry-consistent force-field models are essential for extending quantum-accurate simulations to large spatiotemporal scales. While descriptor-based neural networks can incorporate lattice symmetries through carefully engineered features, we show that graph neural networks (GNNs) provide a conceptually simpler and more unified alternative in which discrete lattice translation and point-group symmetries are enforced directly through local message passing and weight sharing. We develop a GNN-based force-field framework for the adiabatic dynamics of lattice Hamiltonians and demonstrate it for the semiclassical Holstein model. Trained on exact-diagonalization data, the GNN achieves high force accuracy, strict linear scaling with system size, and direct transferability to large lattices. Enabled by this scalability, we perform large-scale Langevin simulations of charge-density-wave ordering following thermal quenches, revealing dynamical scaling and anomalously slow sub--Allen--Cahn coarsening. These results establish GNNs as an elegant and efficient architecture for symmetry-aware, large-scale dynamical simulations of correlated lattice systems.

