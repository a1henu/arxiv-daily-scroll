---
layout: default
title: Multi-Domain Enhanced Map-Free Trajectory Prediction with Selective Attention
---

# Multi-Domain Enhanced Map-Free Trajectory Prediction with Selective Attention
**arXiv**：[2512.02368v1](https://arxiv.org/abs/2512.02368) · [PDF](https://arxiv.org/pdf/2512.02368.pdf)  
**作者**：Wenyi Xiong, Jian Chen  

**一句话要点**：提出多域增强的无地图轨迹预测算法，通过选择性注意力处理复杂交互场景。

**关键词**：轨迹预测, 无地图预测, 选择性注意力, 专家混合机制, 多域增强, 自动驾驶

## 3 点简述
- 核心问题：现有方法在复杂交互场景中难以高效提取冗余数据中的有价值信息，影响计算效率和预测准确性。
- 方法要点：采用专家混合机制自适应选择关键频率成分，结合选择性注意力模块过滤时空冗余信息，并设计多模态解码器。
- 实验或效果：在Nuscences数据集上验证了算法的优越性，有效处理复杂交互场景。

## 摘要（原文）

> Trajectory prediction is crucial for the reliability and safety of autonomous driving systems, yet it remains a challenging task in complex interactive scenarios. Existing methods often struggle to efficiently extract valuable scene information from redundant data, thereby reducing computational efficiency and prediction accuracy, especially when dealing with intricate agent interactions. To address these challenges, we propose a novel map-free trajectory prediction algorithm that achieves trajectory prediction across the temporal, spatial, and frequency domains. Specifically, in temporal information processing, We utilize a Mixture of Experts (MoE) mechanism to adaptively select critical frequency components. Concurrently, we extract these components and integrate multi-scale temporal features. Subsequently, a selective attention module is proposed to filter out redundant information in both temporal sequences and spatial interactions. Finally, we design a multimodal decoder. Under the supervision of patch-level and point-level losses, we obtain reasonable trajectory results. Experiments on Nuscences datasets demonstrate the superiority of our algorithm, validating its effectiveness in handling complex interactive scenarios.

