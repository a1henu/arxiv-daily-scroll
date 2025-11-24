---
layout: default
title: Neighbor GRPO: Contrastive ODE Policy Optimization Aligns Flow Models
---

# Neighbor GRPO: Contrastive ODE Policy Optimization Aligns Flow Models
**arXiv**：[2511.16955v1](https://arxiv.org/abs/2511.16955) · [PDF](https://arxiv.org/pdf/2511.16955.pdf)  
**作者**：Dailan He, Guanlin Feng, Xingtong Ge, Yazhe Niu, Yi Zhang, Bingqi Ma, Guanglu Song, Yu Liu, Hongsheng Li  

**一句话要点**：提出Neighbor GRPO以解决流匹配模型对齐中的采样效率问题

**关键词**：流匹配模型, 策略优化, 对比学习, ODE采样, 对齐算法

## 3 点简述
- 核心问题：SDE-based GRPO在流匹配模型中存在信用分配低效和与高阶求解器不兼容
- 方法要点：通过扰动ODE初始噪声生成多样轨迹，使用基于距离的代理策略优化模型
- 实验或效果：在训练成本、收敛速度和生成质量上显著优于SDE-based方法

## 摘要（原文）

> Group Relative Policy Optimization (GRPO) has shown promise in aligning image and video generative models with human preferences. However, applying it to modern flow matching models is challenging because of its deterministic sampling paradigm. Current methods address this issue by converting Ordinary Differential Equations (ODEs) to Stochastic Differential Equations (SDEs), which introduce stochasticity. However, this SDE-based GRPO suffers from issues of inefficient credit assignment and incompatibility with high-order solvers for fewer-step sampling. In this paper, we first reinterpret existing SDE-based GRPO methods from a distance optimization perspective, revealing their underlying mechanism as a form of contrastive learning. Based on this insight, we propose Neighbor GRPO, a novel alignment algorithm that completely bypasses the need for SDEs. Neighbor GRPO generates a diverse set of candidate trajectories by perturbing the initial noise conditions of the ODE and optimizes the model using a softmax distance-based surrogate leaping policy. We establish a theoretical connection between this distance-based objective and policy gradient optimization, rigorously integrating our approach into the GRPO framework. Our method fully preserves the advantages of deterministic ODE sampling, including efficiency and compatibility with high-order solvers. We further introduce symmetric anchor sampling for computational efficiency and group-wise quasi-norm reweighting to address reward flattening. Extensive experiments demonstrate that Neighbor GRPO significantly outperforms SDE-based counterparts in terms of training cost, convergence speed, and generation quality.

