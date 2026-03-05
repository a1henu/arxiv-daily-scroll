---
layout: default
title: UrbanHuRo: A Two-Layer Human-Robot Collaboration Framework for the Joint Optimization of Heterogeneous Urban Services
---

# UrbanHuRo: A Two-Layer Human-Robot Collaboration Framework for the Joint Optimization of Heterogeneous Urban Services
**arXiv**：[2603.03701v1](https://arxiv.org/abs/2603.03701) · [PDF](https://arxiv.org/pdf/2603.03701.pdf)  
**作者**：Tonmoy Dey, Lin Jiang, Zheng Dong, Guang Wang  

**一句话要点**：提出UrbanHuRo框架，通过人机协作联合优化众包配送与城市感知服务。

**关键词**：人机协作, 城市服务优化, 子模最大化, 强化学习, 众包配送, 城市感知

## 3 点简述
- 核心问题：异构城市服务（如配送与感知）孤立优化，忽略交互潜力，导致效率低下。
- 方法要点：采用双层框架，包括基于MapReduce的K-子模最大化订单调度和深度子模奖励强化学习感知路径规划。
- 实验或效果：在真实数据集上，平均提升感知覆盖率29.7%和配送员收入39.2%，减少逾期订单。

## 摘要（原文）

> In the vision of smart cities, technologies are being developed to enhance the efficiency of urban services and improve residents' quality of life. However, most existing research focuses on optimizing individual services in isolation, without adequately considering reciprocal interactions among heterogeneous urban services that could yield higher efficiency and improved resource utilization. For example, human couriers could collect traffic and air quality data along their delivery routes, while sensing robots could assist with on-demand delivery during peak hours, enhancing both sensing coverage and delivery efficiency. However, the joint optimization of different urban services is challenging due to potentially conflicting objectives and the need for real-time coordination in dynamic environments. In this paper, we propose UrbanHuRo, a two-layer human-robot collaboration framework for joint optimization of heterogeneous urban services, demonstrated through crowdsourced delivery and urban sensing. UrbanHuRo includes two key designs: (i) a scalable distributed MapReduce-based K-submodular maximization module for efficient order dispatch, and (ii) a deep submodular reward reinforcement learning algorithm for sensing route planning. Experimental evaluations on real-world datasets from a food delivery platform demonstrate that UrbanHuRo improves sensing coverage by 29.7% and courier income by 39.2% on average in most settings, while also significantly reducing the number of overdue orders.

