---
layout: default
title: Optimizing Energy and Data Collection in UAV-aided IoT Networks using Attention-based Multi-Objective Reinforcement Learning
---

# Optimizing Energy and Data Collection in UAV-aided IoT Networks using Attention-based Multi-Objective Reinforcement Learning
**arXiv**：[2601.14092v1](https://arxiv.org/abs/2601.14092) · [PDF](https://arxiv.org/pdf/2601.14092.pdf)  
**作者**：Babacar Toure, Dimitrios Tsilimantos, Omid Esrafilian, Marios Kountouris  

**一句话要点**：提出基于注意力的多目标强化学习架构，优化无人机辅助物联网网络中的能量与数据收集权衡。

**关键词**：无人机路径规划, 多目标强化学习, 注意力机制, 物联网数据收集, 能量优化, 泛化能力

## 3 点简述
- 核心问题：现有算法在动态环境中数据有限，且忽视多目标权衡，如数据收集与能耗。
- 方法要点：使用注意力机制的多目标强化学习，无需无线信道先验知识，适应不同偏好和动态参数。
- 实验或效果：仿真显示在性能、模型紧凑性、样本效率和泛化能力上优于现有强化学习方案。

## 摘要（原文）

> Due to their adaptability and mobility, Unmanned Aerial Vehicles (UAVs) are becoming increasingly essential for wireless network services, particularly for data harvesting tasks. In this context, Artificial Intelligence (AI)-based approaches have gained significant attention for addressing UAV path planning tasks in large and complex environments, bridging the gap with real-world deployments. However, many existing algorithms suffer from limited training data, which hampers their performance in highly dynamic environments. Moreover, they often overlook the inherently multi-objective nature of the task, treating it in an overly simplistic manner. To address these limitations, we propose an attention-based Multi-Objective Reinforcement Learning (MORL) architecture that explicitly handles the trade-off between data collection and energy consumption in urban environments, even without prior knowledge of wireless channel conditions. Our method develops a single model capable of adapting to varying trade-off preferences and dynamic scenario parameters without the need for fine-tuning or retraining. Extensive simulations show that our approach achieves substantial improvements in performance, model compactness, sample efficiency, and most importantly, generalization to previously unseen scenarios, outperforming existing RL solutions.

