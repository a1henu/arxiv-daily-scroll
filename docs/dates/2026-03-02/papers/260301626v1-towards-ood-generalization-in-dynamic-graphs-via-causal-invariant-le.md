---
layout: default
title: Towards OOD Generalization in Dynamic Graphs via Causal Invariant Learning
---

# Towards OOD Generalization in Dynamic Graphs via Causal Invariant Learning
**arXiv**：[2603.01626v1](https://arxiv.org/abs/2603.01626) · [PDF](https://arxiv.org/pdf/2603.01626.pdf)  
**作者**：Xinxun Zhang, Pengfei Jiao, Mengzhou Gao, Tianpeng Li, Xuan Guo  

**一句话要点**：提出DyCIL模型，通过因果不变学习解决动态图OOD泛化问题

**关键词**：动态图神经网络, OOD泛化, 因果不变学习, 时空模式, 分布外场景, 图演化

## 3 点简述
- 核心问题：动态图神经网络在分布外（OOD）场景下泛化能力不足，面临复杂图演化和有限数据观测的挑战。
- 方法要点：基于因果视角，设计动态因果子图生成器、因果感知时空注意力模块和自适应环境生成器，提取不变时空模式。
- 实验或效果：在真实和合成动态图数据集上验证，模型在OOD泛化方面优于现有基线方法。

## 摘要（原文）

> Although dynamic graph neural networks (DyGNNs) have demonstrated promising capabilities, most existing methods ignore out-of-distribution (OOD) shifts that commonly exist in dynamic graphs. Dynamic graph OOD generalization is non-trivial due to the following challenges: 1) Identifying invariant and variant patterns amid complex graph evolution, 2) Capturing the intrinsic evolution rationale from these patterns, and 3) Ensuring model generalization across diverse OOD shifts despite limited data distribution observations. Although several attempts have been made to tackle these challenges, none has successfully addressed all three simultaneously, and they face various limitations in complex OOD scenarios. To solve these issues, we propose a Dynamic graph Causal Invariant Learning (DyCIL) model for OOD generalization via exploiting invariant spatio-temporal patterns from a causal view. Specifically, we first develop a dynamic causal subgraph generator to identify causal dynamic subgraphs explicitly. Next, we design a causal-aware spatio-temporal attention module to extract the intrinsic evolution rationale behind invariant patterns. Finally, we further introduce an adaptive environment generator to capture the underlying dynamics of distributional shifts. Extensive experiments on both real-world and synthetic dynamic graph datasets demonstrate the superiority of our model over state-of-the-art baselines in handling OOD shifts.

