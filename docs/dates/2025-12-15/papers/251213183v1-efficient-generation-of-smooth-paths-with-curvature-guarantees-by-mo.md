---
layout: default
title: Efficient Generation of Smooth Paths with Curvature Guarantees by Mollification
---

# Efficient Generation of Smooth Paths with Curvature Guarantees by Mollification
**arXiv**：[2512.13183v1](https://arxiv.org/abs/2512.13183) · [PDF](https://arxiv.org/pdf/2512.13183.pdf)  
**作者**：Alfredo González-Calvin, Juan F. Jiménez, Héctor García de Marina  

**一句话要点**：提出基于磨光法的平滑路径生成方法，以解决非完整机器人路径跟踪中非可微路径的可行性问题。

**关键词**：路径平滑, 磨光法, 曲率约束, 非完整机器人, 实时路径生成, 轨迹跟踪

## 3 点简述
- 核心问题：非可微路径（如分段函数）在机器人路径跟踪中因缺乏二阶可微性而被排除，但作为高层输入方便。
- 方法要点：通过磨光法正则化非可微函数，生成可微路径并保证曲率有界，计算高效。
- 实验或效果：应用于连接航点的路径，实现实时微控制器兼容，支持标准跟踪算法。

## 摘要（原文）

> Most path following and trajectory tracking algorithms in mobile robotics require the desired path or trajectory to be defined by at least twice continuously differentiable functions to guarantee key properties such as global convergence, especially for nonholonomic robots like unicycles with speed constraints. Consequently, these algorithms typically exclude continuous but non-differentiable paths, such as piecewise functions. Despite this exclusion, such paths provide convenient high-level inputs for describing robot missions or behavior. While techniques such as spline interpolation or optimization-based methods are commonly used to smooth non-differentiable paths or create feasible ones from sequences of waypoints, they either can produce unnecessarily complex trajectories or are computationally expensive. In this work, we present a method to regularize non-differentiable functions and generate feasible paths through mollification. Specifically, we approximate an arbitrary path with a differentiable function that can converge to it with arbitrary precision. Additionally, we provide a systematic method for bounding the curvature of generated paths, which we demonstrate by applying it to paths resulting from linking a sequence of waypoints with segments. The proposed approach is computationally efficient, enabling real-time implementation on microcontrollers and compatibility with standard trajectory tracking and path following algorithms.

