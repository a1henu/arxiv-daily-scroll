---
layout: default
title: Optimizer-Induced Low-Dimensional Drift and Transverse Dynamics in Transformer Training
---

# Optimizer-Induced Low-Dimensional Drift and Transverse Dynamics in Transformer Training
**arXiv**：[2602.23696v1](https://arxiv.org/abs/2602.23696) · [PDF](https://arxiv.org/pdf/2602.23696.pdf)  
**作者**：Yongzhong Xu  

**一句话要点**：揭示优化器在Transformer训练中诱导低维漂移与横向动态的几何特性

**关键词**：Transformer训练, 优化器几何, 低维漂移, 轨迹PCA, AdamW对比SGD, 横向动态

## 3 点简述
- 研究小Transformer训练轨迹的几何结构，发现参数更新形成主导漂移方向与横向残差动态
- 使用非中心化行归一化轨迹PCA，显示早期训练中单一方向捕获大部分累积参数移动，其余分量编码辅助探针性能的振荡行为
- 比较AdamW与SGD变体，揭示优化器选择显著影响轨迹几何维度和结构，超越损失值表现

## 摘要（原文）

> We study the geometry of training trajectories in small transformer models and find that parameter updates organize into a dominant drift direction with transverse residual dynamics. Using uncentered, row-normalized trajectory PCA, we show that a single direction captures a large fraction of cumulative parameter movement early in training, while remaining components encode oscillatory behavior in auxiliary probe performance. Instantaneous gradients exhibit little alignment with this dominant direction, indicating that it arises from accumulated optimizer updates rather than per-batch gradient structure. Comparing AdamW with SGD variants at matched loss levels reveals substantial differences in trajectory geometry: AdamW develops multi-dimensional drift structure, whereas SGD-family optimizers produce nearly colinear parameter evolution and weaker probe dynamics. Reheating selectively perturbs transverse components with minimal effect on the dominant drift coordinate. These findings suggest that optimizer choice shapes the effective dimensionality and structure of learning trajectories beyond what is apparent from loss values alone.

