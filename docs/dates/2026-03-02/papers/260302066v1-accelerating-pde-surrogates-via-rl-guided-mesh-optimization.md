---
layout: default
title: Accelerating PDE Surrogates via RL-Guided Mesh Optimization
---

# Accelerating PDE Surrogates via RL-Guided Mesh Optimization
**arXiv**：[2603.02066v1](https://arxiv.org/abs/2603.02066) · [PDF](https://arxiv.org/pdf/2603.02066.pdf)  
**作者**：Yang Meng, Ruoxi Jiang, Zhuokai Zhao, Chong Liu, Rebecca Willett, Yuxin Chen  

**一句话要点**：提出RLMesh框架，通过强化学习优化网格分配，以降低参数化PDE代理模型训练的计算成本。

**关键词**：参数化PDE代理模型, 强化学习, 网格优化, 计算效率, 空间自适应

## 3 点简述
- 核心问题：参数化PDE代理模型训练需大量精细网格模拟，计算成本高昂。
- 方法要点：使用强化学习自适应分配网格点，聚焦关键区域，结合轻量代理模型加速训练。
- 实验效果：在PDE基准测试中，以更少模拟查询实现与基线相当的精度。

## 摘要（原文）

> Deep surrogate models for parametric partial differential equations (PDEs) can deliver high-fidelity approximations but remain prohibitively data-hungry: training often requires thousands of fine-grid simulations, each incurring substantial computational cost. To address this challenge, we introduce RLMesh, an end-to-end framework for efficient surrogate training under limited simulation budget. The key idea is to use reinforcement learning (RL) to adaptively allocate mesh grid points non-uniformly within each simulation domain, focusing numerical resolution in regions most critical for accurate PDE solutions. A lightweight proxy model further accelerates RL training by providing efficient reward estimates without full surrogate retraining. Experiments on PDE benchmarks demonstrate that RLMesh achieves competitive accuracy to baselines but with substantially fewer simulation queries. These results show that solver-level spatial adaptivity can dramatically improve the efficiency of surrogate training pipelines, enabling practical deployment of learning-based PDE surrogates across a wide range of problems.

