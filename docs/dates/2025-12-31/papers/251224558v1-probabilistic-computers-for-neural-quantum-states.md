---
layout: default
title: Probabilistic Computers for Neural Quantum States
---

# Probabilistic Computers for Neural Quantum States
**arXiv**：[2512.24558v1](https://arxiv.org/abs/2512.24558) · [PDF](https://arxiv.org/pdf/2512.24558.pdf)  
**作者**：Shuvro Chowdhury, Jasper Pieterse, Navid Anjum Aadit, Johan H. Mentink, Kerem Y. Camsari  

**一句话要点**：提出结合概率计算硬件与稀疏玻尔兹曼机，以解决神经量子态中蒙特卡洛采样瓶颈问题。

**关键词**：神经量子态, 概率计算硬件, 玻尔兹曼机, 蒙特卡洛采样, 量子多体系统, FPGA加速

## 3 点简述
- 核心问题：神经量子态在大规模系统中蒙特卡洛采样成本高，限制可扩展性。
- 方法要点：利用FPGA实现概率计算机作为快速采样器，并引入双采样算法训练深度玻尔兹曼机。
- 实验或效果：在二维横向场伊辛模型中，实现高达6400自旋的精确基态能量计算。

## 摘要（原文）

> Neural quantum states efficiently represent many-body wavefunctions with neural networks, but the cost of Monte Carlo sampling limits their scaling to large system sizes. Here we address this challenge by combining sparse Boltzmann machine architectures with probabilistic computing hardware. We implement a probabilistic computer on field programmable gate arrays (FPGAs) and use it as a fast sampler for energy-based neural quantum states. For the two-dimensional transverse-field Ising model at criticality, we obtain accurate ground-state energies for lattices up to 80 $\times$ 80 (6400 spins) using a custom multi-FPGA cluster. Furthermore, we introduce a dual-sampling algorithm to train deep Boltzmann machines, replacing intractable marginalization with conditional sampling over auxiliary layers. This enables the training of sparse deep models and improves parameter efficiency relative to shallow networks. Using this algorithm, we train deep Boltzmann machines for a system with 35 $\times$ 35 (1225 spins). Together, these results demonstrate that probabilistic hardware can overcome the sampling bottleneck in variational simulation of quantum many-body systems, opening a path to larger system sizes and deeper variational architectures.

