---
layout: default
title: Two-dimensional RMSD projections for reaction path visualization and validation
---

# Two-dimensional RMSD projections for reaction path visualization and validation
**arXiv**：[2512.07329v1](https://arxiv.org/abs/2512.07329) · [PDF](https://arxiv.org/pdf/2512.07329.pdf)  
**作者**：Rohit Goswami  

**一句话要点**：提出二维RMSD投影方法以可视化与验证反应路径优化轨迹

**关键词**：反应路径可视化, 过渡态搜索, RMSD投影, 能量等高线, 计算化学分析

## 3 点简述
- 核心问题：传统一维能量-位移图掩盖高维结构重排，难以比较不同优化方法轨迹
- 方法要点：将轨迹映射到基于反应物和产物构型的二维RMSD表面，用径向基函数插值能量颜色映射
- 实验或效果：在环加成反应中验证，显示机器学习势能鞍点与密度泛函理论参考位于可比能量等高线

## 摘要（原文）

> Transition state or minimum energy path finding methods constitute a routine component of the computational chemistry toolkit. Standard analysis involves trajectories conventionally plotted in terms of the relative energy to the initial state against a cumulative displacement variable, or the image number. These dimensional reductions obscure structural rearrangements in high dimensions and may often be trajectory dependent. This precludes the ability to compare optimization trajectories of different methods beyond the number of calculations, time taken, and final saddle geometry. We present a method mapping trajectories onto a two-dimension surface defined by a permutation corrected root mean square deviation from the reactant and product configurations. Energy is represented as an interpolated color-mapped surface constructed from all optimization steps using radial basis functions. This representation highlights optimization trajectories, identifies endpoint basins, and diagnoses convergence concerns invisible in one-dimensional profiles. We validate the framework on a cycloaddition reaction, showing that a machine-learned potential saddle and density functional theory reference lie on comparable energy contours despite geometric displacements.

