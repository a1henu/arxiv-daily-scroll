---
layout: default
title: Can You Hear Me Now? A Benchmark for Long-Range Graph Propagation
---

# Can You Hear Me Now? A Benchmark for Long-Range Graph Propagation
**arXiv**：[2512.17762v1](https://arxiv.org/abs/2512.17762) · [PDF](https://arxiv.org/pdf/2512.17762.pdf)  
**作者**：Luca Miglior, Matteo Tolloso, Alessio Gravina, Davide Bacciu  

**一句话要点**：提出ECHO基准以评估图神经网络在长距离图传播中的能力

**关键词**：图神经网络, 长距离传播, 基准评估, 化学预测, 信息瓶颈, AI for science

## 3 点简述
- 核心问题：图神经网络在捕获长距离交互方面存在未解决的挑战，影响科学应用。
- 方法要点：设计ECHO基准，包括合成图任务和真实化学数据集，以系统评估长距离传播。
- 实验或效果：基准测试揭示流行GNN架构的性能差距，强调长距离传播的困难及改进设计选择。

## 摘要（原文）

> Effectively capturing long-range interactions remains a fundamental yet unresolved challenge in graph neural network (GNN) research, critical for applications across diverse fields of science. To systematically address this, we introduce ECHO (Evaluating Communication over long HOps), a novel benchmark specifically designed to rigorously assess the capabilities of GNNs in handling very long-range graph propagation. ECHO includes three synthetic graph tasks, namely single-source shortest paths, node eccentricity, and graph diameter, each constructed over diverse and structurally challenging topologies intentionally designed to introduce significant information bottlenecks. ECHO also includes two real-world datasets, ECHO-Charge and ECHO-Energy, which define chemically grounded benchmarks for predicting atomic partial charges and molecular total energies, respectively, with reference computations obtained at the density functional theory (DFT) level. Both tasks inherently depend on capturing complex long-range molecular interactions. Our extensive benchmarking of popular GNN architectures reveals clear performance gaps, emphasizing the difficulty of true long-range propagation and highlighting design choices capable of overcoming inherent limitations. ECHO thereby sets a new standard for evaluating long-range information propagation, also providing a compelling example for its need in AI for science.

