---
layout: default
title: Adaptive Trajectory Refinement for Optimization-based Local Planning in Narrow Passages
---

# Adaptive Trajectory Refinement for Optimization-based Local Planning in Narrow Passages
**arXiv**：[2510.26142v1](https://arxiv.org/abs/2510.26142) · [PDF](https://arxiv.org/pdf/2510.26142.pdf)  
**作者**：Hahjin Lee, Young J. Kim  

**一句话要点**：提出自适应轨迹细化算法以解决移动机器人在狭窄通道中的轨迹规划问题

**关键词**：轨迹规划, 移动机器人, 狭窄通道, 碰撞检测, 姿态校正, 优化算法

## 3 点简述
- 核心问题：移动机器人在杂乱环境中的狭窄通道轨迹规划困难，传统方法易失败或生成次优路径。
- 方法要点：采用分段保守碰撞测试和基于穿透方向的姿态校正，确保轨迹段和姿态级安全。
- 实验或效果：仿真和真实实验显示，成功率和规划速度分别提升至1.69倍和3.79倍。

## 摘要（原文）

> Trajectory planning for mobile robots in cluttered environments remains a
> major challenge due to narrow passages, where conventional methods often fail
> or generate suboptimal paths. To address this issue, we propose the adaptive
> trajectory refinement algorithm, which consists of two main stages. First, to
> ensure safety at the path-segment level, a segment-wise conservative collision
> test is applied, where risk-prone trajectory path segments are recursively
> subdivided until collision risks are eliminated. Second, to guarantee
> pose-level safety, pose correction based on penetration direction and line
> search is applied, ensuring that each pose in the trajectory is collision-free
> and maximally clear from obstacles. Simulation results demonstrate that the
> proposed method achieves up to 1.69x higher success rates and up to 3.79x
> faster planning times than state-of-the-art approaches. Furthermore, real-world
> experiments confirm that the robot can safely pass through narrow passages
> while maintaining rapid planning performance.

