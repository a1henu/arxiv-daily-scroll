---
layout: default
title: A Hybrid Approach for Visual Multi-Object Tracking
---

# A Hybrid Approach for Visual Multi-Object Tracking
**arXiv**：[2510.24410v1](https://arxiv.org/abs/2510.24410) · [PDF](https://arxiv.org/pdf/2510.24410.pdf)  
**作者**：Toan Van Nguyen, Rasmus G. K. Christiansen, Dirk Kraft, Leon Bodenhagen  

**一句话要点**：提出混合随机与确定性方法以解决未知目标数下的视觉多目标跟踪问题

**关键词**：多目标跟踪, 粒子滤波, 确定性关联, 标识一致性, 非线性动态, 实时视觉跟踪

## 3 点简述
- 核心问题：非线性动态和未知目标数下保持标识一致性的视觉多目标跟踪
- 方法要点：结合粒子滤波与PSO优化，引入运动、外观和社交交互的适应度度量
- 实验或效果：在预录视频和实时流中表现优于先进跟踪器，代码开源

## 摘要（原文）

> This paper proposes a visual multi-object tracking method that jointly
> employs stochastic and deterministic mechanisms to ensure identifier
> consistency for unknown and time-varying target numbers under nonlinear
> dynamics. A stochastic particle filter addresses nonlinear dynamics and
> non-Gaussian noise, with support from particle swarm optimization (PSO) to
> guide particles toward state distribution modes and mitigate divergence through
> proposed fitness measures incorporating motion consistency, appearance
> similarity, and social-interaction cues with neighboring targets. Deterministic
> association further enforces identifier consistency via a proposed cost matrix
> incorporating spatial consistency between particles and current detections,
> detection confidences, and track penalties. Subsequently, a novel scheme is
> proposed for the smooth updating of target states while preserving their
> identities, particularly for weak tracks during interactions with other targets
> and prolonged occlusions. Moreover, velocity regression over past states
> provides trend-seed velocities, enhancing particle sampling and state updates.
> The proposed tracker is designed to operate flexibly for both pre-recorded
> videos and camera live streams, where future frames are unavailable.
> Experimental results confirm superior performance compared to state-of-the-art
> trackers. The source-code reference implementations of both the proposed method
> and compared-trackers are provided on GitHub:
> https://github.com/SDU-VelKoTek/GenTrack2

