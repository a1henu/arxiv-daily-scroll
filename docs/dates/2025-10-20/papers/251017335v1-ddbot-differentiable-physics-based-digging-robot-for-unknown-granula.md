---
layout: default
title: DDBot: Differentiable Physics-based Digging Robot for Unknown Granular Materials
---

# DDBot: Differentiable Physics-based Digging Robot for Unknown Granular Materials
**arXiv**：[2510.17335v1](https://arxiv.org/abs/2510.17335) · [PDF](https://arxiv.org/pdf/2510.17335.pdf)  
**作者**：Xintong Yang, Minglun Wei, Ze Ji, Yu-Kun Lai  

**一句话要点**：提出可微分物理挖掘机器人DDBot，用于未知颗粒材料的高精度挖掘任务。

**关键词**：可微分物理模拟, 颗粒材料操作, 系统识别, 挖掘技能优化, GPU加速计算, 零样本部署

## 3 点简述
- 核心问题：颗粒材料操作因复杂接触动态和未知物理属性而难以实现高效精准。
- 方法要点：采用可微分物理模拟器，结合GPU加速和自动微分，优化系统识别与挖掘技能。
- 实验效果：在5-20分钟内收敛，零样本真实部署中实现高精度，优于现有基线。

## 摘要（原文）

> Automating the manipulation of granular materials poses significant
> challenges due to complex contact dynamics, unpredictable material properties,
> and intricate system states. Existing approaches often fail to achieve
> efficiency and accuracy in such tasks. To fill the research gap, this paper
> studies the small-scale and high-precision granular material digging task with
> unknown physical properties. A new framework, named differentiable digging
> robot (DDBot), is proposed to manipulate granular materials, including sand and
> soil.
>   Specifically, we equip DDBot with a differentiable physics-based simulator,
> tailored for granular material manipulation, powered by GPU-accelerated
> parallel computing and automatic differentiation. DDBot can perform efficient
> differentiable system identification and high-precision digging skill
> optimisation for unknown granular materials, which is enabled by a
> differentiable skill-to-action mapping, a task-oriented demonstration method,
> gradient clipping and line search-based gradient descent.
>   Experimental results show that DDBot can efficiently (converge within 5 to 20
> minutes) identify unknown granular material dynamics and optimise digging
> skills, with high-precision results in zero-shot real-world deployments,
> highlighting its practicality. Benchmark results against state-of-the-art
> baselines also confirm the robustness and efficiency of DDBot in such digging
> tasks.

