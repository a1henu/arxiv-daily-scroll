---
layout: default
title: Meta-RL with Shared Representations Enables Fast Adaptation in Energy Systems
---

# Meta-RL with Shared Representations Enables Fast Adaptation in Energy Systems
**arXiv**：[2603.08418v1](https://arxiv.org/abs/2603.08418) · [PDF](https://arxiv.org/pdf/2603.08418.pdf)  
**作者**：Théo Zangato, Aomar Osmani, Pegah Alizadeh  

**一句话要点**：提出基于共享表示的元强化学习框架，以提升能源系统中任务适应效率。

**关键词**：元强化学习, 共享表示学习, 能源系统优化, 任务适应, 双层优化

## 3 点简述
- 核心问题：传统强化学习在多任务和非平稳环境中适应慢、泛化差。
- 方法要点：结合双层优化与混合演员-评论家架构，元学习共享特征提取器。
- 实验或效果：在建筑能源管理数据集上验证，优于传统RL和Meta-RL方法。

## 摘要（原文）

> Meta-Reinforcement Learning addresses the critical limitations of conventional Reinforcement Learning in multi-task and non-stationary environments by enabling fast policy adaptation and improved generalization. We introduce a novel Meta-RL framework that integrates a bi-level optimization scheme with a hybrid actor-critic architecture specially designed to enhance sample efficiency and inter-task adaptability. To improve knowledge transfer, we meta-learn a shared state feature extractor jointly optimized across actor and critic networks, providing efficient representation learning and limiting overfitting to individual tasks or dominant profiles. Additionally, we propose a parameter-sharing mechanism between the outer- and inner-loop actor networks, to reduce redundant learning and accelerate adaptation during task revisitation. The approach is validated on a real-world Building Energy Management Systems dataset covering nearly a decade of temporal and structural variability, for which we propose a task preparation method to promote generalization. Experiments demonstrate effective task adaptation and better performance compared to conventional RL and Meta-RL methods.

