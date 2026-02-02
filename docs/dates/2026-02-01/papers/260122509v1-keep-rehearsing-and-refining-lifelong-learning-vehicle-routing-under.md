---
layout: default
title: Keep Rehearsing and Refining: Lifelong Learning Vehicle Routing under Continually Drifting Tasks
---

# Keep Rehearsing and Refining: Lifelong Learning Vehicle Routing under Continually Drifting Tasks
**arXiv**：[2601.22509v1](https://arxiv.org/abs/2601.22509) · [PDF](https://arxiv.org/pdf/2601.22509.pdf)  
**作者**：Jiyuan Pei, Yi Mei, Jialin Liu, Mengjie Zhang, Xin Yao  

**一句话要点**：提出DREE框架以解决持续漂移任务下车辆路径规划神经求解器的终身学习问题

**关键词**：车辆路径规划, 终身学习, 持续漂移, 灾难性遗忘, 神经求解器, 经验回放

## 3 点简述
- 核心问题：现有神经求解器忽略问题模式随时间持续漂移，导致任务序列出现但每任务训练资源有限
- 方法要点：DREE框架通过双重回放与经验增强，提升学习效率并缓解灾难性遗忘
- 实验或效果：在持续漂移下，DREE有效学习新任务、保留先验知识、提升泛化能力，适用于多种现有求解器

## 摘要（原文）

> Existing neural solvers for vehicle routing problems (VRPs) are typically trained either in a one-off manner on a fixed set of pre-defined tasks or in a lifelong manner on several tasks arriving sequentially, assuming sufficient training on each task. Both settings overlook a common real-world property: problem patterns may drift continually over time, yielding massive tasks sequentially arising while offering only limited training resources per task. In this paper, we study a novel lifelong learning paradigm for neural VRP solvers under continually drifting tasks over learning time steps, where sufficient training for any given task at any time is not available. We propose Dual Replay with Experience Enhancement (DREE), a general framework to improve learning efficiency and mitigate catastrophic forgetting under such drift. Extensive experiments show that, under such continual drift, DREE effectively learns new tasks, preserves prior knowledge, improves generalization to unseen tasks, and can be applied to diverse existing neural solvers.

