---
layout: default
title: Discriminability-Driven Spatial-Channel Selection with Gradient Norm for Drone Signal OOD Detection
---

# Discriminability-Driven Spatial-Channel Selection with Gradient Norm for Drone Signal OOD Detection
**arXiv**：[2601.18329v1](https://arxiv.org/abs/2601.18329) · [PDF](https://arxiv.org/pdf/2601.18329.pdf)  
**作者**：Chuhan Feng, Jing Li, Jie Li, Lu Lv, Fengkui Gong  

**一句话要点**：提出基于可区分性驱动的空间-通道选择和梯度范数的无人机信号OOD检测算法

**关键词**：无人机信号检测, OOD检测, 空间-通道选择, 梯度范数, 时频图像特征, 协议特定特征

## 3 点简述
- 核心问题：无人机信号OOD检测，需区分已知协议与未知分布信号。
- 方法要点：基于协议特定时频特征自适应加权空间和通道维度，引入梯度范数度量扰动敏感性。
- 实验或效果：仿真结果显示算法在SNR和多种无人机类型下具有优越区分能力和鲁棒性能。

## 摘要（原文）

> We propose a drone signal out-of-distribution (OOD) detection algorithm based on discriminability-driven spatial-channel selection with a gradient norm. Time-frequency image features are adaptively weighted along both spatial and channel dimensions by quantifying inter-class similarity and variance based on protocol-specific time-frequency characteristics. Subsequently, a gradient-norm metric is introduced to measure perturbation sensitivity for capturing the inherent instability of OOD samples, which is then fused with energy-based scores for joint inference. Simulation results demonstrate that the proposed algorithm provides superior discriminative power and robust performance via SNR and various drone types.

