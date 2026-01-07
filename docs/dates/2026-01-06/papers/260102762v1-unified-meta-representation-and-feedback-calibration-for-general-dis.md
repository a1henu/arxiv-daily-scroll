---
layout: default
title: Unified Meta-Representation and Feedback Calibration for General Disturbance Estimation
---

# Unified Meta-Representation and Feedback Calibration for General Disturbance Estimation
**arXiv**：[2601.02762v1](https://arxiv.org/abs/2601.02762) · [PDF](https://arxiv.org/pdf/2601.02762.pdf)  
**作者**：Zihan Yang, Jindou Jia, Meng Wang, Yuhang Liu, Kexin Guo, Xiang Yu  

**一句话要点**：提出统一元表示与反馈校准框架，以解决机器人应用中非结构性时变扰动估计问题。

**关键词**：扰动估计, 元学习, 在线适应, 反馈校准, 机器人控制, 非结构性扰动

## 3 点简述
- 核心问题：现有元学习方法依赖环境结构假设，难以处理现实非结构性扰动，导致预测精度下降。
- 方法要点：通过有限时间窗口提取特征，学习统一元表示捕获非结构性扰动，并引入状态反馈机制校准在线适应过程。
- 实验或效果：理论分析显示在线学习与扰动估计误差可同时收敛，四旋翼飞行实验验证了框架对快速变化扰动的有效估计。

## 摘要（原文）

> Precise control in modern robotic applications is always an open issue due to unknown time-varying disturbances. Existing meta-learning-based approaches require a shared representation of environmental structures, which lack flexibility for realistic non-structural disturbances. Besides, representation error and the distribution shifts can lead to heavy degradation in prediction accuracy. This work presents a generalizable disturbance estimation framework that builds on meta-learning and feedback-calibrated online adaptation. By extracting features from a finite time window of past observations, a unified representation that effectively captures general non-structural disturbances can be learned without predefined structural assumptions. The online adaptation process is subsequently calibrated by a state-feedback mechanism to attenuate the learning residual originating from the representation and generalizability limitations. Theoretical analysis shows that simultaneous convergence of both the online learning error and the disturbance estimation error can be achieved. Through the unified meta-representation, our framework effectively estimates multiple rapidly changing disturbances, as demonstrated by quadrotor flight experiments. See the project page for video, supplementary material and code: https://nonstructural-metalearn.github.io.

