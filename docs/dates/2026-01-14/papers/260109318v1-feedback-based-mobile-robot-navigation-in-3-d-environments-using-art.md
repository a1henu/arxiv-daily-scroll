---
layout: default
title: Feedback-Based Mobile Robot Navigation in 3-D Environments Using Artificial Potential Functions Technical Report
---

# Feedback-Based Mobile Robot Navigation in 3-D Environments Using Artificial Potential Functions Technical Report
**arXiv**：[2601.09318v1](https://arxiv.org/abs/2601.09318) · [PDF](https://arxiv.org/pdf/2601.09318.pdf)  
**作者**：Ro'i Lang, Elon Rimon  

**一句话要点**：提出基于多项式导航函数的反馈控制方法，用于三维环境中球形和圆柱形障碍物的移动机器人运动规划。

**关键词**：三维运动规划, 导航函数, 人工势场, 障碍物避免, 多项式隐函数, 反馈控制

## 3 点简述
- 核心问题：在三维工作空间中，存在球形和圆柱形障碍物时，如何设计导航函数以避免局部极小值并确保目标点唯一最小。
- 方法要点：使用平滑多项式隐函数编码障碍物，构建多项式导航函数，通过梯度和Hessian分析保证无局部极小值。
- 实验或效果：在障碍物丰富的三维环境中进行数值模拟，验证了理论结果的有效性和鲁棒性。

## 摘要（原文）

> This technical report presents the construction and analysis of polynomial navigation functions for motion planning in 3-D workspaces populated by spherical and cylindrical obstacles. The workspace is modeled as a bounded spherical region, and obstacles are encoded using smooth polynomial implicit functions. We establish conditions under which the proposed navigation functions admit a unique non-degenerate minimum at the target while avoiding local minima, including in the presence of pairwise intersecting obstacles. Gradient and Hessian analyses are provided, and the theoretical results are validated through numerical simulations in obstacle rich 3-D environments.

