---
layout: default
title: PDF-HR: Pose Distance Fields for Humanoid Robots
---

# PDF-HR: Pose Distance Fields for Humanoid Robots
**arXiv**：[2602.04851v1](https://arxiv.org/abs/2602.04851) · [PDF](https://arxiv.org/pdf/2602.04851.pdf)  
**作者**：Yi Gu, Yukang Gao, Yangchen Zhou, Xingyu Chen, Yixiao Feng, Mingle Zhao, Yunyang Mo, Zhaorui Wang, Lixin Xu, Renjing Xu  

**一句话要点**：提出PDF-HR姿态距离场，为人形机器人提供轻量级姿态先验以增强优化与控制。

**关键词**：姿态先验, 人形机器人, 距离场, 运动优化, 姿态分布建模

## 3 点简述
- 核心问题：人形机器人领域缺乏高质量运动数据，姿态先验应用受限。
- 方法要点：将机器人姿态分布建模为连续可微流形，预测姿态到大规模重定向姿态的距离。
- 实验或效果：在多种任务中作为即插即用先验，显著提升基线性能，支持优化与控制。

## 摘要（原文）

> Pose and motion priors play a crucial role in humanoid robotics. Although such priors have been widely studied in human motion recovery (HMR) domain with a range of models, their adoption for humanoid robots remains limited, largely due to the scarcity of high-quality humanoid motion data. In this work, we introduce Pose Distance Fields for Humanoid Robots (PDF-HR), a lightweight prior that represents the robot pose distribution as a continuous and differentiable manifold. Given an arbitrary pose, PDF-HR predicts its distance to a large corpus of retargeted robot poses, yielding a smooth measure of pose plausibility that is well suited for optimization and control. PDF-HR can be integrated as a reward shaping term, a regularizer, or a standalone plausibility scorer across diverse pipelines. We evaluate PDF-HR on various humanoid tasks, including single-trajectory motion tracking, general motion tracking, style-based motion mimicry, and general motion retargeting. Experiments show that this plug-and-play prior consistently and substantially strengthens strong baselines. Code and models will be released.

