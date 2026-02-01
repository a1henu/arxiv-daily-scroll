---
layout: default
title: Sim-MSTNet: sim2real based Multi-task SpatioTemporal Network Traffic Forecasting
---

# Sim-MSTNet: sim2real based Multi-task SpatioTemporal Network Traffic Forecasting
**arXiv**：[2601.21384v1](https://arxiv.org/abs/2601.21384) · [PDF](https://arxiv.org/pdf/2601.21384.pdf)  
**作者**：Hui Ma, Qingzhong Li, Jin Wang, Jie Wu, Shaoyu Dou, Li Feng, Xinjun Pei  

**一句话要点**：提出Sim-MSTNet，基于sim2real方法解决网络流量预测中的数据稀缺和多任务学习问题。

**关键词**：网络流量预测, 多任务学习, sim2real, 时空网络, 注意力机制, 动态损失加权

## 3 点简述
- 核心问题：网络流量预测中数据稀缺导致泛化差，多任务学习存在任务不平衡和负迁移。
- 方法要点：利用模拟器生成合成数据，通过双层优化减少分布差距，结合注意力机制和动态损失加权。
- 实验或效果：在两个开源数据集上优于现有基线，提升准确性和泛化能力。

## 摘要（原文）

> Network traffic forecasting plays a crucial role in intelligent network operations, but existing techniques often perform poorly when faced with limited data. Additionally, multi-task learning methods struggle with task imbalance and negative transfer, especially when modeling various service types. To overcome these challenges, we propose Sim-MSTNet, a multi-task spatiotemporal network traffic forecasting model based on the sim2real approach. Our method leverages a simulator to generate synthetic data, effectively addressing the issue of poor generalization caused by data scarcity. By employing a domain randomization technique, we reduce the distributional gap between synthetic and real data through bi-level optimization of both sample weighting and model training. Moreover, Sim-MSTNet incorporates attention-based mechanisms to selectively share knowledge between tasks and applies dynamic loss weighting to balance task objectives. Extensive experiments on two open-source datasets show that Sim-MSTNet consistently outperforms state-of-the-art baselines, achieving enhanced accuracy and generalization.

