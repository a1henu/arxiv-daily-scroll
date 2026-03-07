---
layout: default
title: SPIRIT: Perceptive Shared Autonomy for Robust Robotic Manipulation under Deep Learning Uncertainty
---

# SPIRIT: Perceptive Shared Autonomy for Robust Robotic Manipulation under Deep Learning Uncertainty
**arXiv**：[2603.05111v1](https://arxiv.org/abs/2603.05111) · [PDF](https://arxiv.org/pdf/2603.05111.pdf)  
**作者**：Jongseok Lee, Ribin Balachandran, Harsimran Singh, Jianxiang Feng, Hrishik Mishra, Marco De Stefano, Rudolph Triebel, Alin Albu-Schaeffer, Konstantin Kondak  

**一句话要点**：提出感知共享自主性SPIRIT，利用深度学习不确定性调节自主水平以提升机器人操作鲁棒性。

**关键词**：感知共享自主性, 深度学习不确定性, 点云配准, 机器人操作, 触觉遥操作, NTK

## 3 点简述
- 核心问题：深度学习在机器人感知中鲁棒性不足且缺乏可解释性，阻碍安全关键应用部署。
- 方法要点：基于不确定性感知的点云配准，通过NTK估计不确定性，动态切换半自主操作与触觉遥操作。
- 实验或效果：用户研究和工业场景验证，SPIRIT在感知失败时仍能可靠操作，提升性能和系统可靠性。

## 摘要（原文）

> Deep learning (DL) has enabled impressive advances in robotic perception, yet its limited robustness and lack of interpretability hinder reliable deployment in safety critical applications. We propose a concept termed perceptive shared autonomy, in which uncertainty estimates from DL based perception are used to regulate the level of autonomy. Specifically, when the robot's perception is confident, semi-autonomous manipulation is enabled to improve performance; when uncertainty increases, control transitions to haptic teleoperation for maintaining robustness. In this way, high-performing but uninterpretable DL methods can be integrated safely into robotic systems. A key technical enabler is an uncertainty aware DL based point cloud registration approach based on the so called Neural Tangent Kernels (NTK). We evaluate perceptive shared autonomy on challenging aerial manipulation tasks through a user study of 15 participants and realization of mock-up industrial scenarios, demonstrating reliable robotic manipulation despite failures in DL based perception. The resulting system, named SPIRIT, improves both manipulation performance and system reliability. SPIRIT was selected as a finalist of a major industrial innovation award.

