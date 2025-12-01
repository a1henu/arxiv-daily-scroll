---
layout: default
title: Time Extrapolation with Graph Convolutional Autoencoder and Tensor Train Decomposition
---

# Time Extrapolation with Graph Convolutional Autoencoder and Tensor Train Decomposition
**arXiv**：[2511.23037v1](https://arxiv.org/abs/2511.23037) · [PDF](https://arxiv.org/pdf/2511.23037.pdf)  
**作者**：Yuanhong Chen, Federico Pichi, Zhen Gao, Gianluigi Rozza  

**一句话要点**：提出结合图卷积自编码器与张量列车分解的模型，以解决参数化偏微分方程在复杂几何上的时间外推问题。

**关键词**：图卷积自编码器, 张量列车分解, 时间外推, 参数化偏微分方程, 深度算子网络, 算子推断

## 3 点简述
- 核心问题：图自编码器在参数化动态系统的时间外推中，需同时处理时间因果性和参数空间泛化性，面临挑战。
- 方法要点：通过张量列车分解将高保真快照分解为参数、空间和时间核心，结合算子推断学习时间演化，并利用深度算子网络增强泛化。
- 实验或效果：在热传导、对流扩散和涡旋脱落等数值实验中，相比MeshGraphNets等先进方法，展现出优异的外推性能。

## 摘要（原文）

> Graph autoencoders have gained attention in nonlinear reduced-order modeling of parameterized partial differential equations defined on unstructured grids. Despite they provide a geometrically consistent way of treating complex domains, applying such architectures to parameterized dynamical systems for temporal prediction beyond the training data, i.e. the extrapolation regime, is still a challenging task due to the simultaneous need of temporal causality and generalizability in the parametric space. In this work, we explore the integration of graph convolutional autoencoders (GCAs) with tensor train (TT) decomposition and Operator Inference (OpInf) to develop a time-consistent reduced-order model. In particular, high-fidelity snapshots are represented as a combination of parametric, spatial, and temporal cores via TT decomposition, while OpInf is used to learn the evolution of the latter. Moreover, we enhance the generalization performance by developing a multi-fidelity two-stages approach in the framework of Deep Operator Networks (DeepONet), treating the spatial and temporal cores as the trunk networks, and the parametric core as the branch network. Numerical results, including heat-conduction, advection-diffusion and vortex-shedding phenomena, demonstrate great performance in effectively learning the dynamic in the extrapolation regime for complex geometries, also in comparison with state-of-the-art approaches e.g. MeshGraphNets.

