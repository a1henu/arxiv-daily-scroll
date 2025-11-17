---
layout: default
title: Scalable Coverage Trajectory Synthesis on GPUs as Statistical Inference
---

# Scalable Coverage Trajectory Synthesis on GPUs as Statistical Inference
**arXiv**：[2511.11514v1](https://arxiv.org/abs/2511.11514) · [PDF](https://arxiv.org/pdf/2511.11514.pdf)  
**作者**：Max M. Sun, Jueun Kwon, Todd Murphey  

**一句话要点**：提出基于流匹配的覆盖运动规划方法，以提升GPU并行计算效率

**关键词**：覆盖运动规划, 流匹配, 统计推断, GPU并行计算, 轨迹合成

## 3 点简述
- 覆盖运动规划需处理轨迹空间分布，传统方法计算效率低且难以并行化
- 将问题建模为统计推断，统一KL与Sinkhorn散度，并解耦轨迹梯度与控制合成
- 在GPU上实现显著加速，相比基于路径点跟踪的方法更具计算优势

## 摘要（原文）

> Coverage motion planning is essential to a wide range of robotic tasks. Unlike conventional motion planning problems, which reason over temporal sequences of states, coverage motion planning requires reasoning over the spatial distribution of entire trajectories, making standard motion planning methods limited in computational efficiency and less amenable to modern parallelization frameworks. In this work, we formulate the coverage motion planning problem as a statistical inference problem from the perspective of flow matching, a generative modeling technique that has gained significant attention in recent years. The proposed formulation unifies commonly used statistical discrepancy measures, such as Kullback-Leibler divergence and Sinkhorn divergence, with a standard linear quadratic regulator problem. More importantly, it decouples the generation of trajectory gradients for coverage from the synthesis of control under nonlinear system dynamics, enabling significant acceleration through parallelization on modern computational architectures, particularly Graphics Processing Units (GPUs). This paper focuses on the advantages of this formulation in terms of scalability through parallelization, highlighting its computational benefits compared to conventional methods based on waypoint tracking.

