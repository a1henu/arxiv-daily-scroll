---
layout: default
title: A Geometry-Adaptive Deep Variational Framework for Phase Discovery in the Landau-Brazovskii Model
---

# A Geometry-Adaptive Deep Variational Framework for Phase Discovery in the Landau-Brazovskii Model
**arXiv**：[2603.05161v1](https://arxiv.org/abs/2603.05161) · [PDF](https://arxiv.org/pdf/2603.05161.pdf)  
**作者**：Yuchen Xie, Jianyuan Yin, Lei Zhang  

**一句话要点**：提出几何自适应深度变分框架以解决Landau-Brazovskii模型中相发现的计算域敏感性问题

**关键词**：Landau-Brazovskii模型, 几何自适应变分框架, 深度神经网络, 相发现, 计算域优化, 亚稳态识别

## 3 点简述
- 核心问题：数值求解器对计算域尺寸敏感，导致人工应力并陷入高能亚稳态
- 方法要点：联合优化神经网络参数化的序参数和计算域的几何参数，消除人工应力
- 实验或效果：通过预热惩罚和引导初始化，从随机初始化自发成核复杂三维有序相

## 摘要（原文）

> The discovery of ordered structures in pattern-forming systems, such as the Landau-Brazovskii (LB) model, is often limited by the sensitivity of numerical solvers to the prescribed computational domain size. Incompatible domains induce artificial stress, frequently trapping the system in high-energy metastable configurations. To resolve this issue, we propose a Geometry-Adaptive Deep Variational Framework (GeoDVF) that jointly optimizes the infinite-dimensional order parameter, which is parameterized by a neural network, and the finite-dimensional geometric parameters of the computational domain. By explicitly treating the domain size as trainable variables within the variational formulation, GeoDVF naturally eliminates artificial stress during training. To escape the attraction basin of the disordered phase under small initializations, we introduce a warmup penalty mechanism, which effectively destabilizes the disordered phase, enabling the spontaneous nucleation of complex three-dimensional ordered phases from random initializations. Furthermore, we design a guided initialization protocol to resolve topologically intricate phases associated with narrow basins of attraction. Extensive numerical experiments show that GeoDVF provides a robust and geometry-consistent variational solver capable of identifying both stable and metastable states without prior knowledge.

