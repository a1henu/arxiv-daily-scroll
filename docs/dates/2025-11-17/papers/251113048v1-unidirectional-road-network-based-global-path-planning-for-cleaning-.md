---
layout: default
title: Unidirectional-Road-Network-Based Global Path Planning for Cleaning Robots in Semi-Structured Environments
---

# Unidirectional-Road-Network-Based Global Path Planning for Cleaning Robots in Semi-Structured Environments
**arXiv**：[2511.13048v1](https://arxiv.org/abs/2511.13048) · [PDF](https://arxiv.org/pdf/2511.13048.pdf)  
**作者**：Yong Li, Hui Cheng  

**一句话要点**：提出基于单向路网的全局路径规划方法，以优化清洁机器人在半结构化环境中的导航效率。

**关键词**：全局路径规划, 清洁机器人, 半结构化环境, 单向路网, 路径优化

## 3 点简述
- 核心问题：现有方法在路径长度与交通规则约束间失衡，导致重规划频繁或路径过长。
- 方法要点：构建单向路网表示交通约束，允许起点和终点跨越道路以缩短路径。
- 实验或效果：实验验证方法在路径长度与路网一致性间取得更好平衡，优于现有技术。

## 摘要（原文）

> Practical global path planning is critical for commercializing cleaning robots working in semi-structured environments. In the literature, global path planning methods for free space usually focus on path length and neglect the traffic rule constraints of the environments, which leads to high-frequency re-planning and increases collision risks. In contrast, those for structured environments are developed mainly by strictly complying with the road network representing the traffic rule constraints, which may result in an overlong path that hinders the overall navigation efficiency. This article proposes a general and systematic approach to improve global path planning performance in semi-structured environments. A unidirectional road network is built to represent the traffic constraints in semi-structured environments and a hybrid strategy is proposed to achieve a guaranteed planning result.Cutting across the road at the starting and the goal points are allowed to achieve a shorter path. Especially, a two-layer potential map is proposed to achieve a guaranteed performance when the starting and the goal points are in complex intersections. Comparative experiments are carried out to validate the effectiveness of the proposed method. Quantitative experimental results show that, compared with the state-of-art, the proposed method guarantees a much better balance between path length and the consistency with the road network.

