---
layout: default
title: Viewpoint Matters: Dynamically Optimizing Viewpoints with Masked Autoencoder for Visual Manipulation
---

# Viewpoint Matters: Dynamically Optimizing Viewpoints with Masked Autoencoder for Visual Manipulation
**arXiv**：[2602.04243v1](https://arxiv.org/abs/2602.04243) · [PDF](https://arxiv.org/pdf/2602.04243.pdf)  
**作者**：Pengfei Yi, Yifan Han, Junyan Li, Litao Liu, Wenzhao Lian  

**一句话要点**：提出MAE-Select框架，通过动态优化单摄像头视角以提升机器人视觉操作性能

**关键词**：机器人视觉操作, 动态视角选择, 掩码自编码器, 模仿学习, 主动感知

## 3 点简述
- 核心问题：模仿学习中固定摄像头设置限制机器人操作的适应性和覆盖范围
- 方法要点：利用预训练多视角掩码自编码器表示，动态选择信息最丰富的下一个视角
- 实验或效果：实验表明MAE-Select增强单摄像头系统能力，部分情况下超越多摄像头设置

## 摘要（原文）

> Robotic manipulation continues to be a challenge, and imitation learning (IL) enables robots to learn tasks from expert demonstrations. Current IL methods typically rely on fixed camera setups, where cameras are manually positioned in static locations, imposing significant limitations on adaptability and coverage. Inspired by human active perception, where humans dynamically adjust their viewpoint to capture the most relevant and least noisy information, we propose MAE-Select, a novel framework for active viewpoint selection in single-camera robotic systems. MAE-Select fully leverages pre-trained multi-view masked autoencoder representations and dynamically selects the next most informative viewpoint at each time chunk without requiring labeled viewpoints. Extensive experiments demonstrate that MAE-Select improves the capabilities of single-camera systems and, in some cases, even surpasses multi-camera setups. The project will be available at https://mae-select.github.io.

