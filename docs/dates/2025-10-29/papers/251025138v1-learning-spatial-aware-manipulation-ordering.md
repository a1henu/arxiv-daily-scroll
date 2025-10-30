---
layout: default
title: Learning Spatial-Aware Manipulation Ordering
---

# Learning Spatial-Aware Manipulation Ordering
**arXiv**：[2510.25138v1](https://arxiv.org/abs/2510.25138) · [PDF](https://arxiv.org/pdf/2510.25138.pdf)  
**作者**：Yuxiang Yan, Zhiyuan Zhou, Xin Gao, Guanghao Li, Shenglin Li, Jiaqi Chen, Qunyan Pu, Jian Pu  

**一句话要点**：提出OrderMind框架以解决杂乱环境中物体操作顺序问题

**关键词**：操作顺序学习, 空间感知, 图神经网络, 蒸馏训练, 机器人操作

## 3 点简述
- 核心问题：杂乱环境中物体空间依赖导致操作顺序不当，引发碰撞或阻塞
- 方法要点：集成空间上下文编码器和时间优先级模块，学习基于空间上下文的操作优先级
- 实验或效果：在仿真和真实环境中显著优于现有方法，提升操作有效性和效率

## 摘要（原文）

> Manipulation in cluttered environments is challenging due to spatial
> dependencies among objects, where an improper manipulation order can cause
> collisions or blocked access. Existing approaches often overlook these spatial
> relationships, limiting their flexibility and scalability. To address these
> limitations, we propose OrderMind, a unified spatial-aware manipulation
> ordering framework that directly learns object manipulation priorities based on
> spatial context. Our architecture integrates a spatial context encoder with a
> temporal priority structuring module. We construct a spatial graph using
> k-Nearest Neighbors to aggregate geometric information from the local layout
> and encode both object-object and object-manipulator interactions to support
> accurate manipulation ordering in real-time. To generate physically and
> semantically plausible supervision signals, we introduce a spatial prior
> labeling method that guides a vision-language model to produce reasonable
> manipulation orders for distillation. We evaluate OrderMind on our Manipulation
> Ordering Benchmark, comprising 163,222 samples of varying difficulty. Extensive
> experiments in both simulation and real-world environments demonstrate that our
> method significantly outperforms prior approaches in effectiveness and
> efficiency, enabling robust manipulation in cluttered scenes.

