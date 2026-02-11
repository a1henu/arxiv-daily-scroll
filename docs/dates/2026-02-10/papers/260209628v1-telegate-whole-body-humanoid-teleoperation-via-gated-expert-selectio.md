---
layout: default
title: TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior
---

# TeleGate: Whole-Body Humanoid Teleoperation via Gated Expert Selection with Motion Prior
**arXiv**：[2602.09628v1](https://arxiv.org/abs/2602.09628) · [PDF](https://arxiv.org/pdf/2602.09628.pdf)  
**作者**：Jie Li, Bing Tang, Feng Wu, Rongyun Cao  

**一句话要点**：提出TeleGate框架，通过门控专家选择与运动先验实现人形机器人全身高精度实时遥操作

**关键词**：人形机器人遥操作, 门控专家选择, 运动先验模块, 实时控制, 高精度跟踪, 动态运动

## 3 点简述
- 核心问题：现有统一控制器在蒸馏多专家策略时导致性能下降，难以支持动态运动。
- 方法要点：训练轻量门控网络动态激活专家策略，并引入VAE运动先验模块预测未来意图。
- 实验或效果：仅用2.5小时动捕数据训练，在仿真和Unitree G1机器人上实现高精度跟踪，优于基线方法。

## 摘要（原文）

> Real-time whole-body teleoperation is a critical method for humanoid robots to perform complex tasks in unstructured environments. However, developing a unified controller that robustly supports diverse human motions remains a significant challenge. Existing methods typically distill multiple expert policies into a single general policy, which often inevitably leads to performance degradation, particularly on highly dynamic motions. This paper presents TeleGate, a unified whole-body teleoperation framework for humanoid robots that achieves high-precision tracking across various motions while avoiding the performance loss inherent in knowledge distillation. Our key idea is to preserve the full capability of domain-specific expert policies by training a lightweight gating network, which dynamically activates experts in real-time based on proprioceptive states and reference trajectories. Furthermore, to compensate for the absence of future reference trajectories in real-time teleoperation, we introduce a VAE-based motion prior module that extracts implicit future motion intent from historical observations, enabling anticipatory control for motions requiring prediction such as jumping and standing up. We conducted empirical evaluations in simulation and also deployed our technique on the Unitree G1 humanoid robot. Using only 2.5 hours of motion capture data for training, our TeleGate achieves high-precision real-time teleoperation across diverse dynamic motions (e.g., running, fall recovery, and jumping), significantly outperforming the baseline methods in both tracking accuracy and success rate.

