---
layout: default
title: Learning Generalizable Hand-Object Tracking from Synthetic Demonstrations
---

# Learning Generalizable Hand-Object Tracking from Synthetic Demonstrations
**arXiv**：[2512.19583v1](https://arxiv.org/abs/2512.19583) · [PDF](https://arxiv.org/pdf/2512.19583.pdf)  
**作者**：Yinhuai Wang, Runyi Yu, Hok Wai Tsui, Xiaoyi Lin, Hui Zhang, Qihan Zhao, Ke Fan, Miao Li, Jie Song, Jingbo Wang, Qifeng Chen, Ping Tan  

**一句话要点**：提出基于合成数据的通用手-物追踪控制器，无需人类演示，解决灵巧操作的数据瓶颈问题。

**关键词**：手-物追踪, 合成数据学习, 强化学习, 交互模仿学习, 通用控制器, 灵巧操作

## 3 点简述
- 核心问题：灵巧操作依赖人类演示，数据获取困难，限制通用控制器发展。
- 方法要点：开发HOP合成多样手-物轨迹，HOT通过强化学习和交互模仿学习实现合成到物理的迁移。
- 实验或效果：在多样物体形状和手部形态下，实现长序列追踪，如物体重排和敏捷手内重定向。

## 摘要（原文）

> We present a system for learning generalizable hand-object tracking controllers purely from synthetic data, without requiring any human demonstrations. Our approach makes two key contributions: (1) HOP, a Hand-Object Planner, which can synthesize diverse hand-object trajectories; and (2) HOT, a Hand-Object Tracker that bridges synthetic-to-physical transfer through reinforcement learning and interaction imitation learning, delivering a generalizable controller conditioned on target hand-object states. Our method extends to diverse object shapes and hand morphologies. Through extensive evaluations, we show that our approach enables dexterous hands to track challenging, long-horizon sequences including object re-arrangement and agile in-hand reorientation. These results represent a significant step toward scalable foundation controllers for manipulation that can learn entirely from synthetic data, breaking the data bottleneck that has long constrained progress in dexterous manipulation.

