---
layout: default
title: A Sliding-Window Filter for Online Continuous-Time Continuum Robot State Estimation
---

# A Sliding-Window Filter for Online Continuous-Time Continuum Robot State Estimation
**arXiv**：[2510.26623v1](https://arxiv.org/abs/2510.26623) · [PDF](https://arxiv.org/pdf/2510.26623.pdf)  
**作者**：Spencer Teetaert, Sven Lilge, Jessica Burgner-Kahrs, Timothy D. Barfoot  

**一句话要点**：提出滑动窗口滤波器以在线连续时间估计连续体机器人状态

**关键词**：连续体机器人, 状态估计, 滑动窗口滤波器, 连续时间方法, 在线操作

## 3 点简述
- 连续体机器人状态估计方法难以平衡精度与计算效率
- 结合滑动窗口与连续时间方法，实现在线快速状态估计
- 在未知实验中，提升精度并运行速度快于实时

## 摘要（原文）

> Stochastic state estimation methods for continuum robots (CRs) often struggle
> to balance accuracy and computational efficiency. While several recent works
> have explored sliding-window formulations for CRs, these methods are limited to
> simplified, discrete-time approximations and do not provide stochastic
> representations. In contrast, current stochastic filter methods must run at the
> speed of measurements, limiting their full potential. Recent works in
> continuous-time estimation techniques for CRs show a principled approach to
> addressing this runtime constraint, but are currently restricted to offline
> operation. In this work, we present a sliding-window filter (SWF) for
> continuous-time state estimation of CRs that improves upon the accuracy of a
> filter approach while enabling continuous-time methods to operate online, all
> while running at faster-than-real-time speeds. This represents the first
> stochastic SWF specifically designed for CRs, providing a promising direction
> for future research in this area.

