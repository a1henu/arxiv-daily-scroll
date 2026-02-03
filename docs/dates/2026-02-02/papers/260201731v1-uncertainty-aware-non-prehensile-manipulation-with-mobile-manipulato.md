---
layout: default
title: Uncertainty-Aware Non-Prehensile Manipulation with Mobile Manipulators under Object-Induced Occlusion
---

# Uncertainty-Aware Non-Prehensile Manipulation with Mobile Manipulators under Object-Induced Occlusion
**arXiv**：[2602.01731v1](https://arxiv.org/abs/2602.01731) · [PDF](https://arxiv.org/pdf/2602.01731.pdf)  
**作者**：Jiwoo Hwang, Taegeun Yang, Jeil Jeong, Minsung Yoon, Sung-Eui Yoon  

**一句话要点**：提出CURA-PPO强化学习框架，以解决移动机械臂在物体遮挡下的非抓取操作安全问题。

**关键词**：非抓取操作, 移动机械臂, 遮挡处理, 不确定性建模, 强化学习, 主动感知

## 3 点简述
- 核心问题：非抓取操作中物体遮挡传感器视野，导致碰撞风险。
- 方法要点：建模部分可观测性下的不确定性，预测碰撞分布，结合置信图引导主动感知。
- 实验或效果：在多种物体大小和障碍配置下，成功率最高提升3倍，实现安全导航。

## 摘要（原文）

> Non-prehensile manipulation using onboard sensing presents a fundamental challenge: the manipulated object occludes the sensor's field of view, creating occluded regions that can lead to collisions. We propose CURA-PPO, a reinforcement learning framework that addresses this challenge by explicitly modeling uncertainty under partial observability. By predicting collision possibility as a distribution, we extract both risk and uncertainty to guide the robot's actions. The uncertainty term encourages active perception, enabling simultaneous manipulation and information gathering to resolve occlusions. When combined with confidence maps that capture observation reliability, our approach enables safe navigation despite severe sensor occlusion. Extensive experiments across varying object sizes and obstacle configurations demonstrate that CURA-PPO achieves up to 3X higher success rates than the baselines, with learned behaviors that handle occlusions. Our method provides a practical solution for autonomous manipulation in cluttered environments using only onboard sensing.

