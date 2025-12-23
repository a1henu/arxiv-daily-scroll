---
layout: default
title: Translating Flow to Policy via Hindsight Online Imitation
---

# Translating Flow to Policy via Hindsight Online Imitation
**arXiv**：[2512.19269v1](https://arxiv.org/abs/2512.19269) · [PDF](https://arxiv.org/pdf/2512.19269.pdf)  
**作者**：Yitian Zheng, Zhangchen Ye, Weijun Dong, Shengjie Wang, Yuyang Liu, Chongjie Zhang, Chuan Wen, Yang Gao  

**一句话要点**：提出HinFlow方法，通过后见在线模仿提升分层机器人系统的低层策略性能。

**关键词**：分层机器人系统, 后见学习, 在线模仿, 目标条件策略, 跨具身学习, 机器人操作

## 3 点简述
- 核心问题：分层机器人系统中，高层规划器生成的任务计划难以落地为可执行动作，高质量机器人数据有限。
- 方法要点：在线收集轨迹，后见重标注高层目标，聚合经验更新目标条件模仿策略。
- 实验或效果：在模拟和物理世界多样操作任务中，性能提升超2倍，优于现有方法，支持跨具身视频数据训练。

## 摘要（原文）

> Recent advances in hierarchical robot systems leverage a high-level planner to propose task plans and a low-level policy to generate robot actions. This design allows training the planner on action-free or even non-robot data sources (e.g., videos), providing transferable high-level guidance. Nevertheless, grounding these high-level plans into executable actions remains challenging, especially with the limited availability of high-quality robot data. To this end, we propose to improve the low-level policy through online interactions. Specifically, our approach collects online rollouts, retrospectively annotates the corresponding high-level goals from achieved outcomes, and aggregates these hindsight-relabeled experiences to update a goal-conditioned imitation policy. Our method, Hindsight Flow-conditioned Online Imitation (HinFlow), instantiates this idea with 2D point flows as the high-level planner. Across diverse manipulation tasks in both simulation and physical world, our method achieves more than $2\times$ performance improvement over the base policy, significantly outperforming the existing methods. Moreover, our framework enables policy acquisition from planners trained on cross-embodiment video data, demonstrating its potential for scalable and transferable robot learning.

