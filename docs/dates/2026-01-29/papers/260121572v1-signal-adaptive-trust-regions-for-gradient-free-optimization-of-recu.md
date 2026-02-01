---
layout: default
title: Signal-Adaptive Trust Regions for Gradient-Free Optimization of Recurrent Spiking Neural Networks
---

# Signal-Adaptive Trust Regions for Gradient-Free Optimization of Recurrent Spiking Neural Networks
**arXiv**：[2601.21572v1](https://arxiv.org/abs/2601.21572) · [PDF](https://arxiv.org/pdf/2601.21572.pdf)  
**作者**：Jinhao Li, Yuhao Sun, Zhiyuan Ma, Hao He, Xinche Zhang, Xing Chen, Jin Li, Sen Song  

**一句话要点**：提出信号自适应信任区域以优化循环脉冲神经网络，提升强化学习稳定性与效率。

**关键词**：循环脉冲神经网络, 强化学习, 梯度自由优化, 信任区域方法, 二进制权重, 连续控制

## 3 点简述
- 循环脉冲神经网络训练面临高维长时程强化学习挑战，梯度估计方差大导致更新不稳定。
- 方法引入信号自适应信任区域，基于KL散度归一化约束分布更新，自动调整信任区域大小。
- 实验在连续控制基准上验证了稳定性提升和竞争性性能，并实现二进制优化加速训练。

## 摘要（原文）

> Recurrent spiking neural networks (RSNNs) are a promising substrate for energy-efficient control policies, but training them for high-dimensional, long-horizon reinforcement learning remains challenging. Population-based, gradient-free optimization circumvents backpropagation through non-differentiable spike dynamics by estimating gradients. However, with finite populations, high variance of these estimates can induce harmful and overly aggressive update steps. Inspired by trust-region methods in reinforcement learning that constrain policy updates in distribution space, we propose \textbf{Signal-Adaptive Trust Regions (SATR)}, a distributional update rule that constrains relative change by bounding KL divergence normalized by an estimated signal energy. SATR automatically expands the trust region under strong signals and contracts it when updates are noise-dominated. We instantiate SATR for Bernoulli connectivity distributions, which have shown strong empirical performance for RSNN optimization. Across a suite of high-dimensional continuous-control benchmarks, SATR improves stability under limited populations and reaches competitive returns against strong baselines including PPO-LSTM. In addition, to make SATR practical at scale, we introduce a bitset implementation for binary spiking and binary weights, substantially reducing wall-clock training time and enabling fast RSNN policy search.

