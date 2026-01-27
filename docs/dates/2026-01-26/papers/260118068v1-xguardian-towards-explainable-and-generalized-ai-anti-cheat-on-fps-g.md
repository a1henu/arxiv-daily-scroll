---
layout: default
title: XGuardian: Towards Explainable and Generalized AI Anti-Cheat on FPS Games
---

# XGuardian: Towards Explainable and Generalized AI Anti-Cheat on FPS Games
**arXiv**：[2601.18068v1](https://arxiv.org/abs/2601.18068) · [PDF](https://arxiv.org/pdf/2601.18068.pdf)  
**作者**：Jiayi Zhang, Chenxin Sun, Chenxiong Qian  

**一句话要点**：提出XGuardian系统以解决FPS游戏中瞄准辅助作弊的检测问题

**关键词**：FPS游戏反作弊, 瞄准辅助检测, 时间特征分析, 可解释AI, 服务器端检测, 泛化性能

## 3 点简述
- 核心问题：现有瞄准辅助作弊检测方法存在可靠性低、泛化性差、开销大、性能不足和缺乏可解释性等局限
- 方法要点：基于俯仰角和偏航角构建时间特征描述瞄准轨迹，实现服务器端通用可解释检测
- 实验或效果：在CS2等游戏中验证高检测性能、低开销和强泛化能力，并公开数据集和系统

## 摘要（原文）

> Aim-assist cheats are the most prevalent and infamous form of cheating in First-Person Shooter (FPS) games, which help cheaters illegally reveal the opponent's location and auto-aim and shoot, and thereby pose significant threats to the game industry. Although a considerable research effort has been made to automatically detect aim-assist cheats, existing works suffer from unreliable frameworks, limited generalizability, high overhead, low detection performance, and a lack of explainability of detection results. In this paper, we propose XGuardian, a server-side generalized and explainable system for detecting aim-assist cheats to overcome these limitations. It requires only two raw data inputs, pitch and yaw, which are all FPS games' must-haves, to construct novel temporal features and describe aim trajectories, which are essential for distinguishing cheaters and normal players. XGuardian is evaluated with the latest mainstream FPS game CS2, and validates its generalizability with another two different games. It achieves high detection performance and low overhead compared to prior works across different games with real-world and large-scale datasets, demonstrating wide generalizability and high effectiveness. It is able to justify its predictions and thereby shorten the ban cycle. We make XGuardian as well as our datasets publicly available.

