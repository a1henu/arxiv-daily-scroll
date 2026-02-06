---
layout: default
title: RFM-Pose:Reinforcement-Guided Flow Matching for Fast Category-Level 6D Pose Estimation
---

# RFM-Pose:Reinforcement-Guided Flow Matching for Fast Category-Level 6D Pose Estimation
**arXiv**：[2602.05257v1](https://arxiv.org/abs/2602.05257) · [PDF](https://arxiv.org/pdf/2602.05257.pdf)  
**作者**：Diya He, Qingchen Liu, Cong Zhang, Jiahu Qin  

**一句话要点**：提出RFM-Pose框架，通过强化学习引导流匹配加速类别级6D姿态估计

**关键词**：类别级姿态估计, 流匹配生成模型, 强化学习优化, 6D姿态生成, 计算效率提升

## 3 点简述
- 核心问题：基于分数的生成模型在类别级姿态估计中效率受限，采样成本高
- 方法要点：采用流匹配生成模型优化采样路径，结合强化学习微调策略以主动评估假设
- 实验或效果：在REAL275基准上实现良好性能，显著降低计算成本，并可适应姿态跟踪

## 摘要（原文）

> Object pose estimation is a fundamental problem in computer vision and plays a critical role in virtual reality and embodied intelligence, where agents must understand and interact with objects in 3D space. Recently, score based generative models have to some extent solved the rotational symmetry ambiguity problem in category level pose estimation, but their efficiency remains limited by the high sampling cost of score-based diffusion. In this work, we propose a new framework, RFM-Pose, that accelerates category-level 6D object pose generation while actively evaluating sampled hypotheses. To improve sampling efficiency, we adopt a flow-matching generative model and generate pose candidates along an optimal transport path from a simple prior to the pose distribution. To further refine these candidates, we cast the flow-matching sampling process as a Markov decision process and apply proximal policy optimization to fine-tune the sampling policy. In particular, we interpret the flow field as a learnable policy and map an estimator to a value network, enabling joint optimization of pose generation and hypothesis scoring within a reinforcement learning framework. Experiments on the REAL275 benchmark demonstrate that RFM-Pose achieves favorable performance while significantly reducing computational cost. Moreover, similar to prior work, our approach can be readily adapted to object pose tracking and attains competitive results in this setting.

