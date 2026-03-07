---
layout: default
title: Integrated cooperative localization of heterogeneous measurement swarm: A unified data-driven method
---

# Integrated cooperative localization of heterogeneous measurement swarm: A unified data-driven method
**arXiv**：[2603.04932v1](https://arxiv.org/abs/2603.04932) · [PDF](https://arxiv.org/pdf/2603.04932.pdf)  
**作者**：Kunrui Ze, Wei Wang, Guibin Sun, Jiaqi Yan, Kexin Liu, Jinhu Lü  

**一句话要点**：提出统一数据驱动方法，解决异构机器人系统在稀疏有向测量拓扑下的协同定位问题。

**关键词**：协同定位, 异构机器人系统, 数据驱动方法, 相对定位估计, 分布式控制, 测量拓扑

## 3 点简述
- 研究异构机器人协同定位问题，现有方法依赖多邻居几何约束，难以处理有向稀疏测量拓扑。
- 开发统一数据驱动的自适应相对定位估计器，基于互测和里程计信息，支持异构和单向测量。
- 设计分布式姿态耦合协同定位策略，在弱连通有向拓扑下保证定位，并通过编队控制和真实实验验证。

## 摘要（原文）

> The cooperative localization (CL) problem in heterogeneous robotic systems with different measurement capabilities is investigated in this work. In practice, heterogeneous sensors lead to directed and sparse measurement topologies, whereas most existing CL approaches rely on multilateral localization with restrictive multi-neighbor geometric requirements. To overcome this limitation, we enable pairwise relative localization (RL) between neighboring robots using only mutual measurement and odometry information. A unified data-driven adaptive RL estimator is first developed to handle heterogeneous and unidirectional measurements. Based on the convergent RL estimates, a distributed pose-coupling CL strategy is then designed, which guarantees CL under a weakly connected directed measurement topology, representing the least restrictive condition among existing results. The proposed method is independent of specific control tasks and is validated through a formation control application and real-world experiments.

