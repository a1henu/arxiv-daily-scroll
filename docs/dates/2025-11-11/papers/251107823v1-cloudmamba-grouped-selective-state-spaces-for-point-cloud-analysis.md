---
layout: default
title: CloudMamba: Grouped Selective State Spaces for Point Cloud Analysis
---

# CloudMamba: Grouped Selective State Spaces for Point Cloud Analysis
**arXiv**：[2511.07823v1](https://arxiv.org/abs/2511.07823) · [PDF](https://arxiv.org/pdf/2511.07823.pdf)  
**作者**：Kanglin Qu, Pan Gao, Qun Dai, Zhanzhi Ye, Rui Ye, Yuanhao Sun  

**一句话要点**：提出CloudMamba以解决点云分析中的序列化、几何感知和过拟合问题

**关键词**：点云分析, 选择性状态空间模型, 序列化方法, 几何感知, 过拟合缓解, 线性复杂度

## 3 点简述
- 核心问题：点云序列化不完善、高层几何感知不足、S6模型过拟合
- 方法要点：序列扩展与合并、链式Mamba、分组选择性状态空间模型
- 实验或效果：在多个任务中实现SOTA结果，复杂度显著降低

## 摘要（原文）

> Due to the long-range modeling ability and linear complexity property, Mamba has attracted considerable attention in point cloud analysis. Despite some interesting progress, related work still suffers from imperfect point cloud serialization, insufficient high-level geometric perception, and overfitting of the selective state space model (S6) at the core of Mamba. To this end, we resort to an SSM-based point cloud network termed CloudMamba to address the above challenges. Specifically, we propose sequence expanding and sequence merging, where the former serializes points along each axis separately and the latter serves to fuse the corresponding higher-order features causally inferred from different sequences, enabling unordered point sets to adapt more stably to the causal nature of Mamba without parameters. Meanwhile, we design chainedMamba that chains the forward and backward processes in the parallel bidirectional Mamba, capturing high-level geometric information during scanning. In addition, we propose a grouped selective state space model (GS6) via parameter sharing on S6, alleviating the overfitting problem caused by the computational mode in S6. Experiments on various point cloud tasks validate CloudMamba's ability to achieve state-of-the-art results with significantly less complexity.

