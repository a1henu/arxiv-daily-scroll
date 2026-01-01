---
layout: default
title: BandiK: Efficient Multi-Task Decomposition Using a Multi-Bandit Framework
---

# BandiK: Efficient Multi-Task Decomposition Using a Multi-Bandit Framework
**arXiv**：[2512.24708v1](https://arxiv.org/abs/2512.24708) · [PDF](https://arxiv.org/pdf/2512.24708.pdf)  
**作者**：András Millinghoffer, András Formanek, András Antos, Péter Antal  

**一句话要点**：提出BandiK多臂老虎机框架，以高效选择多任务学习中的有益辅助任务子集。

**关键词**：多任务学习, 辅助任务选择, 多臂老虎机, 负迁移, 知识传递, 神经网络

## 3 点简述
- 核心问题：多任务学习中辅助任务子集选择计算成本高、候选集数量大，且负迁移阻碍知识传递。
- 方法要点：分三阶段：估计任务间转移、构建线性候选集、使用多臂老虎机框架评估候选集性能。
- 实验或效果：通过多臂老虎机结构利用神经网络共享，提升选择效率，减少评估开销。

## 摘要（原文）

> The challenge of effectively transferring knowledge across multiple tasks is of critical importance and is also present in downstream tasks with foundation models. However, the nature of transfer, its transitive-intransitive nature, is still an open problem, and negative transfer remains a significant obstacle. Selection of beneficial auxiliary task sets in multi-task learning is frequently hindered by the high computational cost of their evaluation, the high number of plausible candidate auxiliary sets, and the varying complexity of selection across target tasks.
>   To address these constraints, we introduce BandiK, a novel three-stage multi-task auxiliary task subset selection method using multi-bandits, where each arm pull evaluates candidate auxiliary sets by training and testing a multiple output neural network on a single random train-test dataset split. Firstly, BandiK estimates the pairwise transfers between tasks, which helps in identifying which tasks are likely to benefit from joint learning. In the second stage, it constructs a linear number of candidate sets of auxiliary tasks (in the number of all tasks) for each target task based on the initial estimations, significantly reducing the exponential number of potential auxiliary task sets. Thirdly, it employs a Multi-Armed Bandit (MAB) framework for each task, where the arms correspond to the performance of candidate auxiliary sets realized as multiple output neural networks over train-test data set splits. To enhance efficiency, BandiK integrates these individual task-specific MABs into a multi-bandit structure. The proposed multi-bandit solution exploits that the same neural network realizes multiple arms of different individual bandits corresponding to a given candidate set. This semi-overlapping arm property defines a novel multi-bandit cost/reward structure utilized in BandiK.

