---
layout: default
title: New Spiking Architecture for Multi-Modal Decision-Making in Autonomous Vehicles
---

# New Spiking Architecture for Multi-Modal Decision-Making in Autonomous Vehicles
**arXiv**：[2512.01882v1](https://arxiv.org/abs/2512.01882) · [PDF](https://arxiv.org/pdf/2512.01882.pdf)  
**作者**：Aref Ghoreishee, Abhishek Mishra, Lifeng Zhou, John Walsh, Nagarajan Kandasamy  

**一句话要点**：提出基于脉冲神经元的时空感知类Transformer架构，用于自动驾驶多模态决策，以降低计算成本。

**关键词**：自动驾驶决策, 多模态融合, 脉冲神经网络, Transformer架构, 计算效率

## 3 点简述
- 核心问题：Transformer在多模态融合中计算成本高，难以部署于资源受限的边缘环境。
- 方法要点：采用三元脉冲神经元构建脉冲时空感知类Transformer，实现高效多模态融合。
- 实验或效果：在高速公路环境中多任务评估，验证了实时决策的有效性和效率。

## 摘要（原文）

> This work proposes an end-to-end multi-modal reinforcement learning framework for high-level decision-making in autonomous vehicles. The framework integrates heterogeneous sensory input, including camera images, LiDAR point clouds, and vehicle heading information, through a cross-attention transformer-based perception module. Although transformers have become the backbone of modern multi-modal architectures, their high computational cost limits their deployment in resource-constrained edge environments. To overcome this challenge, we propose a spiking temporal-aware transformer-like architecture that uses ternary spiking neurons for computationally efficient multi-modal fusion. Comprehensive evaluations across multiple tasks in the Highway Environment demonstrate the effectiveness and efficiency of the proposed approach for real-time autonomous decision-making.

