---
layout: default
title: Frequency-Separable Hamiltonian Neural Network for Multi-Timescale Dynamics
---

# Frequency-Separable Hamiltonian Neural Network for Multi-Timescale Dynamics
**arXiv**：[2603.06354v1](https://arxiv.org/abs/2603.06354) · [PDF](https://arxiv.org/pdf/2603.06354.pdf)  
**作者**：Yaojun Li, Yulong Yang, Christine Allen-Blanchette  

**一句话要点**：提出频率可分离哈密顿神经网络以解决多时间尺度动力学建模问题

**关键词**：哈密顿神经网络, 多时间尺度动力学, 频谱偏差, 偏微分方程建模, 长期外推, 泛化性能

## 3 点简述
- 哈密顿神经网络难以捕捉多时间尺度复杂动态，常受限于频谱偏差
- FS-HNN通过多网络参数化哈密顿函数，分别学习快慢模式，并扩展至偏微分方程
- 实验表明FS-HNN在挑战性动力系统中提升长期外推性能，泛化于ODE和PDE问题

## 摘要（原文）

> While Hamiltonian mechanics provides a powerful inductive bias for neural networks modeling dynamical systems, Hamiltonian Neural Networks and their variants often fail to capture complex temporal dynamics spanning multiple timescales. This limitation is commonly linked to the spectral bias of deep neural networks, which favors learning low-frequency, slow-varying dynamics. Prior approaches have sought to address this issue through symplectic integration schemes that enforce energy conservation or by incorporating geometric constraints to impose structure on the configuration-space. However, such methods either remain limited in their ability to fully capture multiscale dynamics or require substantial domain specific assumptions. In this work, we exploit the observation that Hamiltonian functions admit decompositions into explicit fast and slow modes and can be reconstructed from these components. We introduce the Frequency-Separable Hamiltonian Neural Network (FS-HNN), which parameterizes the system Hamiltonian using multiple networks, each governed by Hamiltonian dynamics and trained on data sampled at distinct timescales. We further extend this framework to partial differential equations by learning a state- and boundary-conditioned symplectic operators. Empirically, we show that FS-HNN improves long-horizon extrapolation performance on challenging dynamical systems and generalizes across a broad range of ODE and PDE problems.

