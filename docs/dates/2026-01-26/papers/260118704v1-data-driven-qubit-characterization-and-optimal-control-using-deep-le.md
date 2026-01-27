---
layout: default
title: Data-Driven Qubit Characterization and Optimal Control using Deep Learning
---

# Data-Driven Qubit Characterization and Optimal Control using Deep Learning
**arXiv**：[2601.18704v1](https://arxiv.org/abs/2601.18704) · [PDF](https://arxiv.org/pdf/2601.18704.pdf)  
**作者**：Paul Surrey, Julian D. Teske, Tobias Hangleiter, Hendrik Bluhm, Pascal Cerfontaine  

**一句话要点**：提出基于深度学习的量子比特表征与最优控制协议，以解决高保真量子门优化中的梯度计算和系统建模挑战。

**关键词**：量子计算, 最优控制, 深度学习, 循环神经网络, 量子比特表征

## 3 点简述
- 核心问题：量子计算中高保真量子门优化需高效梯度计算和复杂系统动力学建模。
- 方法要点：使用循环神经网络预测量子比特行为，实现无需详细系统模型的梯度优化。
- 实验或效果：在单ST_0量子比特模拟中验证了方法的有效性。

## 摘要（原文）

> Quantum computing requires the optimization of control pulses to achieve high-fidelity quantum gates. We propose a machine learning-based protocol to address the challenges of evaluating gradients and modeling complex system dynamics. By training a recurrent neural network (RNN) to predict qubit behavior, our approach enables efficient gradient-based pulse optimization without the need for a detailed system model. First, we sample qubit dynamics using random control pulses with weak prior assumptions. We then train the RNN on the system's observed responses, and use the trained model to optimize high-fidelity control pulses. We demonstrate the effectiveness of this approach through simulations on a single $ST_0$ qubit.

