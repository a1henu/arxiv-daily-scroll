---
layout: default
title: Accelerated Predictive Coding Networks via Direct Kolen-Pollack Feedback Alignment
---

# Accelerated Predictive Coding Networks via Direct Kolen-Pollack Feedback Alignment
**arXiv**：[2602.15571v1](https://arxiv.org/abs/2602.15571) · [PDF](https://arxiv.org/pdf/2602.15571.pdf)  
**作者**：Davide Casnici, Martin Lefebvre, Justin Dauwels, Charlotte Frenkel  

**一句话要点**：提出直接Kolen-Pollack预测编码以解决反馈延迟和指数衰减问题，提升预测编码效率。

**关键词**：预测编码, 反馈对齐, 深度学习优化, 局部更新, 硬件效率

## 3 点简述
- 预测编码面临误差信号传播延迟和指数衰减，导致早期层更新消失。
- 引入可学习反馈连接，从输出层直接传输误差到所有隐藏层，降低时间复杂度至O(1)。
- 实验显示性能至少可比标准预测编码，并改善延迟和计算性能，支持硬件高效实现。

## 摘要（原文）

> Predictive coding (PC) is a biologically inspired algorithm for training neural networks that relies only on local updates, allowing parallel learning across layers. However, practical implementations face two key limitations: error signals must still propagate from the output to early layers through multiple inference-phase steps, and feedback decays exponentially during this process, leading to vanishing updates in early layers. We propose direct Kolen-Pollack predictive coding (DKP-PC), which simultaneously addresses both feedback delay and exponential decay, yielding a more efficient and scalable variant of PC while preserving update locality. Leveraging direct feedback alignment and direct Kolen-Pollack algorithms, DKP-PC introduces learnable feedback connections from the output layer to all hidden layers, establishing a direct pathway for error transmission. This yields an algorithm that reduces the theoretical error propagation time complexity from O(L), with L being the network depth, to O(1), removing depth-dependent delay in error signals. Moreover, empirical results demonstrate that DKP-PC achieves performance at least comparable to, and often exceeding, that of standard PC, while offering improved latency and computational performance, supporting its potential for custom hardware-efficient implementations.

