---
layout: default
title: Adaptive Policy Switching of Two-Wheeled Differential Robots for Traversing over Diverse Terrains
---

# Adaptive Policy Switching of Two-Wheeled Differential Robots for Traversing over Diverse Terrains
**arXiv**：[2603.04761v1](https://arxiv.org/abs/2603.04761) · [PDF](https://arxiv.org/pdf/2603.04761.pdf)  
**作者**：Haruki Izawa, Takeshi Takai, Shingo Kitano, Mikita Miyaguchi, Hiroaki Kawashima  

**一句话要点**：提出基于姿态观测的自适应策略切换方法，以解决两轮差动机器人在月球熔岩管中穿越多样地形的问题。

**关键词**：自适应策略切换, 地形分类, 高斯混合模型, 机器人导航, 月球探索

## 3 点简述
- 核心问题：预训练策略无法覆盖所有地形，需自适应切换以提升机器人自主穿越能力。
- 方法要点：利用机器人导航中的3D姿态数据，通过高斯混合模型分类地形，实现策略选择。
- 实验或效果：在模拟环境中，使用70步窗口的分类准确率超过98%，验证了短期姿态数据的有效性。

## 摘要（原文）

> Exploring lunar lava tubes requires robots to traverse without human intervention. Because pre-trained policies cannot fully cover all possible terrain conditions, our goal is to enable adaptive policy switching, where the robot selects an appropriate terrain-specialized model based on its current terrain features. This study investigates whether terrain types can be estimated effectively using posture-related observations collected during navigation. We fine-tuned a pre-trained policy using Proximal Policy Optimization (PPO), and then collected the robot's 3D orientation data as it moved across flat and rough terrain in a simulated lava-tube environment. Our analysis revealed that the standard deviation of the robot's pitch data shows a clear difference between these two terrain types. Using Gaussian mixture models (GMM), we evaluated terrain classification across various window sizes. An accuracy of more than 98% was achieved when using a 70-step window. The result suggests that short-term orientation data are sufficient for reliable terrain estimation, providing a foundation for adaptive policy switching.

