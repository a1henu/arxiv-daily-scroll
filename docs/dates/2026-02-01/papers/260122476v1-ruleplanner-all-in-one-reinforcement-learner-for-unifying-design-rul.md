---
layout: default
title: RulePlanner: All-in-One Reinforcement Learner for Unifying Design Rules in 3D Floorplanning
---

# RulePlanner: All-in-One Reinforcement Learner for Unifying Design Rules in 3D Floorplanning
**arXiv**：[2601.22476v1](https://arxiv.org/abs/2601.22476) · [PDF](https://arxiv.org/pdf/2601.22476.pdf)  
**作者**：Ruizhe Zhong, Xingbo Du, Junchi Yan  

**一句话要点**：提出RulePlanner统一设计规则的强化学习框架，解决3D集成电路布局中的复杂规则遵守问题。

**关键词**：3D集成电路布局, 设计规则遵守, 强化学习, 动作空间约束, 矩阵表示, 可扩展框架

## 3 点简述
- 核心问题：3D集成电路布局需遵守复杂硬件设计规则，现有方法处理有限，导致人工调整耗时。
- 方法要点：统一框架包含矩阵表示、动作空间约束和奖励信号，以强化学习处理多种规则。
- 实验或效果：在公开基准测试中验证有效性，展示对未见电路的迁移性和框架可扩展性。

## 摘要（原文）

> Floorplanning determines the coordinate and shape of each module in Integrated Circuits. With the scaling of technology nodes, in floorplanning stage especially 3D scenarios with multiple stacked layers, it has become increasingly challenging to adhere to complex hardware design rules. Current methods are only capable of handling specific and limited design rules, while violations of other rules require manual and meticulous adjustment. This leads to labor-intensive and time-consuming post-processing for expert engineers. In this paper, we propose an all-in-one deep reinforcement learning-based approach to tackle these challenges, and design novel representations for real-world IC design rules that have not been addressed by previous approaches. Specifically, the processing of various hardware design rules is unified into a single framework with three key components: 1) novel matrix representations to model the design rules, 2) constraints on the action space to filter out invalid actions that cause rule violations, and 3) quantitative analysis of constraint satisfaction as reward signals. Experiments on public benchmarks demonstrate the effectiveness and validity of our approach. Furthermore, transferability is well demonstrated on unseen circuits. Our framework is extensible to accommodate new design rules, thus providing flexibility to address emerging challenges in future chip design. Code will be available at: https://github.com/Thinklab-SJTU/EDA-AI

