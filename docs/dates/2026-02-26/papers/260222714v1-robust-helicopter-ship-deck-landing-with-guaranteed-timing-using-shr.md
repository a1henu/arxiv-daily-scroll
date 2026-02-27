---
layout: default
title: Robust Helicopter Ship Deck Landing With Guaranteed Timing Using Shrinking-Horizon Model Predictive Control
---

# Robust Helicopter Ship Deck Landing With Guaranteed Timing Using Shrinking-Horizon Model Predictive Control
**arXiv**：[2602.22714v1](https://arxiv.org/abs/2602.22714) · [PDF](https://arxiv.org/pdf/2602.22714.pdf)  
**作者**：Philipp Schitz, Paolo Mercorelli, Johann C. Dauer  

**一句话要点**：提出基于收缩时域模型预测控制的算法，实现直升机在移动甲板上的鲁棒自主着陆。

**关键词**：直升机自主着陆, 收缩时域模型预测控制, 扰动反馈控制, 移动甲板着陆, 时序保证, 鲁棒控制

## 3 点简述
- 核心问题：直升机在扰动下（如强风）于移动甲板精确着陆，需保证预定时序与安全。
- 方法要点：采用收缩时域模型预测控制结合扰动反馈辅助控制器，确保着陆时间窗口与高抗扰性能。
- 实验或效果：仿真显示，在强风下所有机动均实现高精度着陆，满足时序约束，计算时间在毫秒级。

## 摘要（原文）

> We present a runtime efficient algorithm for autonomous helicopter landings on moving ship decks based on Shrinking-Horizon Model Predictive Control (SHMPC). First, a suitable planning model capturing the relevant aspects of the full nonlinear helicopter dynamics is derived. Next, we use the SHMPC together with a touchdown controller stage to ensure a pre-specified maneuver time and an associated landing time window despite the presence of disturbances. A high disturbance rejection performance is achieved by designing an ancillary controller with disturbance feedback. Thus, given a target position and time, a safe landing with suitable terminal conditions is be guaranteed if the initial optimization problem is feasible. The efficacy of our approach is shown in simulation where all maneuvers achieve a high landing precision in strong winds while satisfying timing and operational constraints with maximum computation times in the millisecond range.

