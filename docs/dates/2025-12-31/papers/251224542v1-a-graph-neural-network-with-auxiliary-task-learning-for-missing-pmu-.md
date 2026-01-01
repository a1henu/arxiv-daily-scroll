---
layout: default
title: A Graph Neural Network with Auxiliary Task Learning for Missing PMU Data Reconstruction
---

# A Graph Neural Network with Auxiliary Task Learning for Missing PMU Data Reconstruction
**arXiv**：[2512.24542v1](https://arxiv.org/abs/2512.24542) · [PDF](https://arxiv.org/pdf/2512.24542.pdf)  
**作者**：Bo Li, Zijun Chen, Haiwang Zhong, Di Cao, Guangchun Ruan  

**一句话要点**：提出辅助任务学习图神经网络以重构广域测量系统中缺失的PMU数据

**关键词**：图神经网络, PMU数据重构, 辅助任务学习, 时空依赖, 低秩特性, 不完全可观测性

## 3 点简述
- 核心问题：PMU数据因硬件故障、通信延迟和网络攻击易缺失，现有方法对概念漂移适应差、高缺失率下鲁棒性弱且依赖全系统可观测性假设。
- 方法要点：设计K跳图神经网络直接学习PMU节点子图，结合时空GNN和辅助GNN的辅助学习框架，利用数据低秩特性实现无监督在线学习。
- 实验或效果：数值结果显示方法在高缺失率和不完全可观测性下具有优越的离线和在线性能。

## 摘要（原文）

> In wide-area measurement systems (WAMS), phasor measurement unit (PMU) measurement is prone to data missingness due to hardware failures, communication delays, and cyber-attacks. Existing data-driven methods are limited by inadaptability to concept drift in power systems, poor robustness under high missing rates, and reliance on the unrealistic assumption of full system observability. Thus, this paper proposes an auxiliary task learning (ATL) method for reconstructing missing PMU data. First, a K-hop graph neural network (GNN) is proposed to enable direct learning on the subgraph consisting of PMU nodes, overcoming the limitation of the incompletely observable system. Then, an auxiliary learning framework consisting of two complementary graph networks is designed for accurate reconstruction: a spatial-temporal GNN extracts spatial-temporal dependencies from PMU data to reconstruct missing values, and another auxiliary GNN utilizes the low-rank property of PMU data to achieve unsupervised online learning. In this way, the low-rank properties of the PMU data are dynamically leveraged across the architecture to ensure robustness and self-adaptation. Numerical results demonstrate the superior offline and online performance of the proposed method under high missing rates and incomplete observability.

