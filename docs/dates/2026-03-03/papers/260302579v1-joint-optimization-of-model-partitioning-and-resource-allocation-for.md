---
layout: default
title: Joint Optimization of Model Partitioning and Resource Allocation for Anti-Jamming Collaborative Inference Systems
---

# Joint Optimization of Model Partitioning and Resource Allocation for Anti-Jamming Collaborative Inference Systems
**arXiv**：[2603.02579v1](https://arxiv.org/abs/2603.02579) · [PDF](https://arxiv.org/pdf/2603.02579.pdf)  
**作者**：Mengru Wu, Jiawei Li, Jiaqi Wei, Bin Lyu, Kai-Kit Wong, Hyundong Shin  

**一句话要点**：提出联合优化模型分割与资源分配方案以增强抗干扰协作推理系统性能

**关键词**：协作推理, 抗干扰, 模型分割, 资源分配, 交替优化, 量子遗传算法

## 3 点简述
- 核心问题：DNN协作推理中传输易受恶意干扰，影响推理准确性与延迟
- 方法要点：通过数据回归分析干扰与分割影响，联合优化资源分配、功率和分割策略
- 实验或效果：仿真显示方案在延迟-准确性收益上优于基线方法

## 摘要（原文）

> With the increasing computational demands of deep neural network (DNN) inference on resource-constrained devices, DNN partitioning-based device-edge collaborative inference has emerged as a promising paradigm. However, the transmission of intermediate feature data is vulnerable to malicious jamming, which significantly degrades the overall inference performance. To counter this threat, this letter focuses on an anti-jamming collaborative inference system in the presence of a malicious jammer. In this system, a DNN model is partitioned into two distinct segments, which are executed by wireless devices and edge servers, respectively. We first analyze the effects of jamming and DNN partitioning on inference accuracy via data regression. Based on this, our objective is to maximize the system's revenue of delay and accuracy (RDA) under inference accuracy and computing resource constraints by jointly optimizing computation resource allocation, devices' transmit power, and DNN partitioning. To address the mixed-integer nonlinear programming problem, we propose an efficient alternating optimization-based algorithm, which decomposes the problem into three subproblems that are solved via Karush-Kuhn-Tucker conditions, convex optimization methods, and a quantum genetic algorithm, respectively. Extensive simulations demonstrate that our proposed scheme outperforms baselines in terms of RDA.

