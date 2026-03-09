---
layout: default
title: Data Analogies Enable Efficient Cross-Embodiment Transfer
---

# Data Analogies Enable Efficient Cross-Embodiment Transfer
**arXiv**：[2603.06450v1](https://arxiv.org/abs/2603.06450) · [PDF](https://arxiv.org/pdf/2603.06450.pdf)  
**作者**：Jonathan Yang, Chelsea Finn, Dorsa Sadigh  

**一句话要点**：提出数据类比方法以提升跨机器人具身迁移效率

**关键词**：跨具身迁移, 数据组织, 机器人策略, 演示数据, 模拟实验

## 3 点简述
- 核心问题：异构机器人演示数据如何有效组织以提升目标场景性能
- 方法要点：通过配对演示对齐场景、任务和轨迹，构建数据类比
- 实验或效果：模拟实验显示形态迁移受益于数据类比，真实世界成功率平均提升22.5%

## 摘要（原文）

> Generalist robot policies are trained on demonstrations collected across a wide variety of robots, scenes, and viewpoints. Yet it remains unclear how to best organize and scale such heterogeneous data so that it genuinely improves performance in a given target setting. In this work, we ask: what form of demonstration data is most useful for enabling transfer across robot set-ups? We conduct controlled experiments that vary end-effector morphology, robot platform appearance, and camera perspective, and compare the effects of simply scaling the number of demonstrations against systematically broadening the diversity in different ways. Our simulated experiments show that while perceptual shifts such as viewpoint benefit most from broad diversity, morphology shifts benefit far less from unstructured diversity and instead see the largest gains from data analogies, i.e. paired demonstrations that align scenes, tasks, and/or trajectories across different embodiments. Informed by the simulation results, we improve real-world cross-embodiment transfer success by an average of $22.5\%$ over large-scale, unpaired datasets by changing only the composition of the data.

