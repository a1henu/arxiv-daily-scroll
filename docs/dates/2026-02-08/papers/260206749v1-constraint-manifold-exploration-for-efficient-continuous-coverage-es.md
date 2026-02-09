---
layout: default
title: Constraint Manifold Exploration for Efficient Continuous Coverage Estimation
---

# Constraint Manifold Exploration for Efficient Continuous Coverage Estimation
**arXiv**：[2602.06749v1](https://arxiv.org/abs/2602.06749) · [PDF](https://arxiv.org/pdf/2602.06749.pdf)  
**作者**：Robert Wilbrandt, Rüdiger Dillmann  

**一句话要点**：提出基于约束流形探索的连续覆盖估计方法，以解决工业机器人表面覆盖可行性分析问题。

**关键词**：工业机器人, 表面覆盖估计, 约束流形探索, 配置空间采样, 连续覆盖分析

## 3 点简述
- 核心问题：工业机器人应用中缺乏有效方法分析复杂表面完全覆盖的可行性。
- 方法要点：在扩展配置空间中，采用基于延续的采样策略探索可达表面区域。
- 实验或效果：通过不同运动学和环境的评估，验证了方法在复杂场景中的准确性和效率。

## 摘要（原文）

> Many automated manufacturing processes rely on industrial robot arms to move process-specific tools along workpiece surfaces. In applications like grinding, sanding, spray painting, or inspection, they need to cover a workpiece fully while keeping their tools perpendicular to its surface. While there are approaches to generate trajectories for these applications, there are no sufficient methods for analyzing the feasibility of full surface coverage. This work proposes a sampling-based approach for continuous coverage estimation that explores reachable surface regions in the configuration space. We define an extended ambient configuration space that allows for the representation of tool position and orientation constraints. A continuation-based approach is used to explore it using two different sampling strategies. A thorough evaluation across different kinematics and environments analyzes their runtime and efficiency. This validates our ability to accurately and efficiently calculate surface coverage for complex surfaces in complicated environments.

