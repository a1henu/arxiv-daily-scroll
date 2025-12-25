---
layout: default
title: RoboCade: Gamifying Robot Data Collection
---

# RoboCade: Gamifying Robot Data Collection
**arXiv**：[2512.21235v1](https://arxiv.org/abs/2512.21235) · [PDF](https://arxiv.org/pdf/2512.21235.pdf)  
**作者**：Suvir Mirchandani, Mia Tang, Jiafei Duan, Jubayer Ibn Hamid, Michael Cho, Dorsa Sadigh  

**一句话要点**：提出RoboCade游戏化平台以解决机器人模仿学习数据收集的可扩展性挑战

**关键词**：游戏化数据收集, 机器人模仿学习, 远程遥操作, 人机交互, 可扩展性

## 3 点简述
- 核心问题：机器人模仿学习依赖人类演示数据，但数据收集成本高、过程枯燥，限制训练规模。
- 方法要点：开发游戏化远程遥操作平台，通过视觉反馈、进度条、排行榜等元素提升用户参与度，并设计任务与下游目标重叠。
- 实验或效果：在三个操作任务上收集数据，与标准平台相比，下游任务成功率提升16-56%，用户研究显示游戏化平台更受欢迎（+24%）。

## 摘要（原文）

> Imitation learning from human demonstrations has become a dominant approach for training autonomous robot policies. However, collecting demonstration datasets is costly: it often requires access to robots and needs sustained effort in a tedious, long process. These factors limit the scale of data available for training policies. We aim to address this scalability challenge by involving a broader audience in a gamified data collection experience that is both accessible and motivating. Specifically, we develop a gamified remote teleoperation platform, RoboCade, to engage general users in collecting data that is beneficial for downstream policy training. To do this, we embed gamification strategies into the design of the system interface and data collection tasks. In the system interface, we include components such as visual feedback, sound effects, goal visualizations, progress bars, leaderboards, and badges. We additionally propose principles for constructing gamified tasks that have overlapping structure with useful downstream target tasks. We instantiate RoboCade on three manipulation tasks -- including spatial arrangement, scanning, and insertion. To illustrate the viability of gamified robot data collection, we collect a demonstration dataset through our platform, and show that co-training robot policies with this data can improve success rate on non-gamified target tasks (+16-56%). Further, we conduct a user study to validate that novice users find the gamified platform significantly more enjoyable than a standard non-gamified platform (+24%). These results highlight the promise of gamified data collection as a scalable, accessible, and engaging method for collecting demonstration data.

