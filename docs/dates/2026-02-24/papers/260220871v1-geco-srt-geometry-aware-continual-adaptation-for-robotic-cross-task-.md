---
layout: default
title: GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer
---

# GeCo-SRT: Geometry-aware Continual Adaptation for Robotic Cross-Task Sim-to-Real Transfer
**arXiv**：[2602.20871v1](https://arxiv.org/abs/2602.20871) · [PDF](https://arxiv.org/pdf/2602.20871.pdf)  
**作者**：Wenbo Yu, Wenke Xia, Weitao Zhang, Di Hu  

**一句话要点**：提出GeCo-SRT方法，通过几何感知持续适应实现机器人跨任务仿真到现实的连续迁移。

**关键词**：仿真到现实迁移, 持续学习, 几何感知, 机器人适应, 跨任务学习, 经验回放

## 3 点简述
- 核心问题：传统仿真到现实迁移方法孤立处理每次任务，导致重复调优和知识浪费。
- 方法要点：利用局部几何特征的领域不变和任务不变知识作为可迁移基础，结合专家模块和优先经验回放。
- 实验或效果：相比基线平均性能提升52%，新任务适应仅需1/6数据，显著提高数据效率。

## 摘要（原文）

> Bridging the sim-to-real gap is important for applying low-cost simulation data to real-world robotic systems. However, previous methods are severely limited by treating each transfer as an isolated endeavor, demanding repeated, costly tuning and wasting prior transfer experience.To move beyond isolated sim-to-real, we build a continual cross-task sim-to-real transfer paradigm centered on knowledge accumulation across iterative transfers, thereby enabling effective and efficient adaptation to novel tasks. Thus, we propose GeCo-SRT, a geometry-aware continual adaptation method. It utilizes domain-invariant and task-invariant knowledge from local geometric features as a transferable foundation to accelerate adaptation during subsequent sim-to-real transfers. This method starts with a geometry-aware mixture-of-experts module, which dynamically activates experts to specialize in distinct geometric knowledge to bridge observation sim-to-real gap. Further, the geometry-expert-guided prioritized experience replay module preferentially samples from underutilized experts, refreshing specialized knowledge to combat forgetting and maintain robust cross-task performance. Leveraging knowledge accumulated during iterative transfer, GeCo-SRT method not only achieves 52% average performance improvement over the baseline, but also demonstrates significant data efficiency for new task adaptation with only 1/6 data.We hope this work inspires approaches for efficient, low-cost cross-task sim-to-real transfer.

