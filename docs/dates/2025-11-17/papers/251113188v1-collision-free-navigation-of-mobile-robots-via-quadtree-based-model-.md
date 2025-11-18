---
layout: default
title: Collision-Free Navigation of Mobile Robots via Quadtree-Based Model Predictive Control
---

# Collision-Free Navigation of Mobile Robots via Quadtree-Based Model Predictive Control
**arXiv**：[2511.13188v1](https://arxiv.org/abs/2511.13188) · [PDF](https://arxiv.org/pdf/2511.13188.pdf)  
**作者**：Osama Al Sheikh Ali, Sotiris Koutsoftas, Ze Zhang, Knut Akesson, Emmanuel Dean  

**一句话要点**：提出基于四叉树模型预测控制的集成导航框架，实现自主移动机器人无碰撞导航。

**关键词**：自主移动机器人, 模型预测控制, 四叉树, 无碰撞导航, 轨迹生成

## 3 点简述
- 核心问题：自主移动机器人在复杂环境中需高效生成无碰撞轨迹。
- 方法要点：使用四叉树从占据地图提取安全区域，并作为MPC线性约束。
- 实验效果：在复杂环境中表现优于基线方法，实现可靠导航。

## 摘要（原文）

> This paper presents an integrated navigation framework for Autonomous Mobile Robots (AMRs) that unifies environment representation, trajectory generation, and Model Predictive Control (MPC). The proposed approach incorporates a quadtree-based method to generate structured, axis-aligned collision-free regions from occupancy maps. These regions serve as both a basis for developing safe corridors and as linear constraints within the MPC formulation, enabling efficient and reliable navigation without requiring direct obstacle encoding. The complete pipeline combines safe-area extraction, connectivity graph construction, trajectory generation, and B-spline smoothing into one coherent system. Experimental results demonstrate consistent success and superior performance compared to baseline approaches across complex environments.

