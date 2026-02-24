---
layout: default
title: Bellman Value Decomposition for Task Logic in Safe Optimal Control
---

# Bellman Value Decomposition for Task Logic in Safe Optimal Control
**arXiv**：[2602.19532v1](https://arxiv.org/abs/2602.19532) · [PDF](https://arxiv.org/pdf/2602.19532.pdf)  
**作者**：William Sharpless, Oswin So, Dylan Hirsch, Sylvia Herbert, Chuchu Fan  

**一句话要点**：提出Bellman值分解方法以解决高维任务中安全与目标逻辑的自动优化问题

**关键词**：Bellman值分解, 时序逻辑任务, 安全最优控制, 高维优化, 神经网络策略

## 3 点简述
- 核心问题：高维任务中，形式化自动机复杂且稀疏奖励需手动调参，难以平衡安全与活性。
- 方法要点：证明时序逻辑任务的Bellman值可分解为图结构，通过Reach-Avoid等方程连接，并嵌入神经网络求解。
- 实验或效果：在模拟和硬件实验中，相比基线方法显著提升性能，自动平衡安全与活性。

## 摘要（原文）

> Real-world tasks involve nuanced combinations of goal and safety specifications. In high dimensions, the challenge is exacerbated: formal automata become cumbersome, and the combination of sparse rewards tends to require laborious tuning. In this work, we consider the innate structure of the Bellman Value as a means to naturally organize the problem for improved automatic performance. Namely, we prove the Bellman Value for a complex task defined in temporal logic can be decomposed into a graph of Bellman Values, connected by a set of well-known Bellman equations (BEs): the Reach-Avoid BE, the Avoid BE, and a novel type, the Reach-Avoid-Loop BE. To solve the Value and optimal policy, we propose VDPPO, which embeds the decomposed Value graph into a two-layer neural net, bootstrapping the implicit dependencies. We conduct a variety of simulated and hardware experiments to test our method on complex, high-dimensional tasks involving heterogeneous teams and nonlinear dynamics. Ultimately, we find this approach greatly improves performance over existing baselines, balancing safety and liveness automatically.

