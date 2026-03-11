---
layout: default
title: From Flow to One Step: Real-Time Multi-Modal Trajectory Policies via Implicit Maximum Likelihood Estimation-based Distribution Distillation
---

# From Flow to One Step: Real-Time Multi-Modal Trajectory Policies via Implicit Maximum Likelihood Estimation-based Distribution Distillation
**arXiv**：[2603.09415v1](https://arxiv.org/abs/2603.09415) · [PDF](https://arxiv.org/pdf/2603.09415.pdf)  
**作者**：Ju Dong, Liding Zhang, Lei Zhang, Yu Fu, Kaixin Bai, Zoltan-Csaba Marton, Zhenshan Bing, Zhaopeng Chen, Alois Christian Knoll, Jianwei Zhang  

**一句话要点**：提出基于隐式最大似然估计的分布蒸馏框架，将条件流匹配蒸馏为单步策略，实现机器人实时多模态轨迹控制。

**关键词**：机器人操作, 轨迹生成, 分布蒸馏, 实时控制, 多模态感知, 隐式最大似然估计

## 3 点简述
- 核心问题：基于扩散和流匹配的生成策略在机器人操作中性能强，但迭代ODE积分导致延迟高，限制闭环控制频率。
- 方法要点：通过隐式最大似然估计和双向Chamfer距离，将条件流匹配专家蒸馏为单步学生策略，保持多模态分布。
- 实验或效果：支持实时重规划，在动态干扰下提高鲁棒性，集成多视图RGB、深度、点云和本体感知。

## 摘要（原文）

> Generative policies based on diffusion and flow matching achieve strong performance in robotic manipulation by modeling multi-modal human demonstrations. However, their reliance on iterative Ordinary Differential Equation (ODE) integration introduces substantial latency, limiting high-frequency closed-loop control. Recent single-step acceleration methods alleviate this overhead but often exhibit distributional collapse, producing averaged trajectories that fail to execute coherent manipulation strategies. We propose a framework that distills a Conditional Flow Matching (CFM) expert into a fast single-step student via Implicit Maximum Likelihood Estimation (IMLE). A bi-directional Chamfer distance provides a set-level objective that promotes both mode coverage and fidelity, enabling preservation of the teacher multi-modal action distribution in a single forward pass. A unified perception encoder further integrates multi-view RGB, depth, point clouds, and proprioception into a geometry-aware representation. The resulting high-frequency control supports real-time receding-horizon re-planning and improved robustness under dynamic disturbances.

