---
layout: default
title: The impact of tactile sensor configurations on grasp learning efficiency -- a comparative evaluation in simulation
---

# The impact of tactile sensor configurations on grasp learning efficiency -- a comparative evaluation in simulation
**arXiv**：[2601.10268v1](https://arxiv.org/abs/2601.10268) · [PDF](https://arxiv.org/pdf/2601.10268.pdf)  
**作者**：Eszter Birtalan, Miklós Koller  

**一句话要点**：评估触觉传感器配置对强化学习抓取效率的影响，识别最优布局

**关键词**：触觉传感器, 强化学习, 机器人手设计, 模拟评估, 抓取稳定性

## 3 点简述
- 核心问题：触觉传感器在机器人手上的密度和布局差异大，影响抓取稳定性。
- 方法要点：通过模拟比较6种不同传感器配置，使用双设置系统确保结果鲁棒性。
- 实验或效果：发现配置对性能有特定和普遍影响，识别出一种跨设置表现最佳的配置。

## 摘要（原文）

> Tactile sensors are breaking into the field of robotics to provide direct information related to contact surfaces, including contact events, slip events and even texture identification. These events are especially important for robotic hand designs, including prosthetics, as they can greatly improve grasp stability. Most presently published robotic hand designs, however, implement them in vastly different densities and layouts on the hand surface, often reserving the majority of the available space. We used simulations to evaluate 6 different tactile sensor configurations with different densities and layouts, based on their impact on reinforcement learning. Our two-setup system allows for robust results that are not dependent on the use of a given physics simulator, robotic hand model or machine learning algorithm. Our results show setup-specific, as well as generalized effects across the 6 sensorized simulations, and we identify one configuration as consistently yielding the best performance across both setups. These results could help future research aimed at robotic hand designs, including prostheses.

