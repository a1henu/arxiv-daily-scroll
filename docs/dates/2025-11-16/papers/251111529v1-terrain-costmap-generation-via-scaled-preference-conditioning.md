---
layout: default
title: Terrain Costmap Generation via Scaled Preference Conditioning
---

# Terrain Costmap Generation via Scaled Preference Conditioning
**arXiv**：[2511.11529v1](https://arxiv.org/abs/2511.11529) · [PDF](https://arxiv.org/pdf/2511.11529.pdf)  
**作者**：Luisa Mao, Garret Warnell, Peter Stone, Joydeep Biswas  

**一句话要点**：提出SPACER方法以解决越野机器人导航中地形成本图生成与快速适应问题

**关键词**：地形成本图生成, 缩放偏好条件, 机器人导航, 合成数据训练, 路径规划

## 3 点简述
- 核心问题：现有方法无法同时实现地形成本图的泛化与快速测试时成本调整
- 方法要点：利用合成数据训练，通过缩放偏好条件实现成本图快速适应
- 实验或效果：在多数环境中，SPACER在全局路径规划中表现出最低遗憾值

## 摘要（原文）

> Successful autonomous robot navigation in off-road domains requires the ability to generate high-quality terrain costmaps that are able to both generalize well over a wide variety of terrains and rapidly adapt relative costs at test time to meet mission-specific needs. Existing approaches for costmap generation allow for either rapid test-time adaptation of relative costs (e.g., semantic segmentation methods) or generalization to new terrain types (e.g., representation learning methods), but not both. In this work, we present scaled preference conditioned all-terrain costmap generation (SPACER), a novel approach for generating terrain costmaps that leverages synthetic data during training in order to generalize well to new terrains, and allows for rapid test-time adaptation of relative costs by conditioning on a user-specified scaled preference context. Using large-scale aerial maps, we provide empirical evidence that SPACER outperforms other approaches at generating costmaps for terrain navigation, with the lowest measured regret across varied preferences in five of seven environments for global path planning.

