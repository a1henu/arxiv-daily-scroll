---
layout: default
title: PINNs for Electromagnetic Wave Propagation
---

# PINNs for Electromagnetic Wave Propagation
**arXiv**：[2512.23396v1](https://arxiv.org/abs/2512.23396) · [PDF](https://arxiv.org/pdf/2512.23396.pdf)  
**作者**：Nilufer K. Bulut  

**一句话要点**：提出混合训练策略以提升PINNs在电磁波传播中的精度与能量一致性

**关键词**：物理信息神经网络, 电磁波传播, 混合训练策略, 能量守恒, 无网格方法, 逆问题

## 3 点简述
- 核心问题：PINNs在电磁波传播中相比FDTD存在精度不足和能量漂移问题
- 方法要点：采用时间推进、因果感知加权和局部Poynting正则化等混合策略
- 实验或效果：在2D PEC腔场景中实现0.09% NRMSE误差和0.024%相对能量失配

## 摘要（原文）

> Physics-Informed Neural Networks (PINNs) are a methodology that aims to solve physical systems by directly embedding PDE constraints into the neural network training process. In electromagnetism, where well-established methodologies such as FDTD and FEM already exist, new methodologies are expected to provide clear advantages to be accepted. Despite their mesh-free nature and applicability to inverse problems, PINNs can exhibit deficiencies in terms of accuracy and energy metrics when compared to FDTD solutions. This study demonstrates hybrid training strategies can bring PINNs closer to FDTD-level accuracy and energy consistency.
>   This study presents a hybrid methodology addressing common challenges in wave propagation scenarios. The causality collapse problem in time-dependent PINN training is addressed via time marching and causality-aware weighting. In order to mitigate the discontinuities that are introduced by time marching, a two-stage interface continuity loss is applied. In order to suppress loss accumulation, which is manifested as cumulative energy drift in electromagnetic waves, a local Poynting-based regularizer has been developed.
>   In the developed PINN model, high field accuracy is achieved with an average 0.09\% $NRMSE$ and 1.01\% $L^2$ error over time. Energy conservation is achieved on the PINN side with only a 0.024\% relative energy mismatch in the 2D PEC cavity scenario. Training is performed without labeled field data, using only physics-based residual losses; FDTD is used solely for post-training evaluation. The results demonstrate that PINNs can achieve competitive results with FDTD in canonical electromagnetic examples and are a viable alternative.

