---
layout: default
title: GNSS-based Lunar Orbit and Clock Estimation With Stochastic Cloning UD Filter
---

# GNSS-based Lunar Orbit and Clock Estimation With Stochastic Cloning UD Filter
**arXiv**：[2601.16393v1](https://arxiv.org/abs/2601.16393) · [PDF](https://arxiv.org/pdf/2601.16393.pdf)  
**作者**：Keidai Iiyama, Grace Gao  

**一句话要点**：提出基于GNSS的月球轨道与时钟估计框架，采用随机克隆UD滤波器处理低可观测性条件。

**关键词**：月球导航, GNSS轨道估计, 随机克隆滤波器, TDCP测量, 数值稳定性, 蒙特卡洛模拟

## 3 点简述
- 核心问题：月球导航卫星在远距离下GNSS观测性低，影响轨道与时钟估计精度。
- 方法要点：开发随机克隆UD因子化滤波器与延迟状态平滑器，结合TDCP测量增强数值稳定性。
- 实验或效果：通过高保真模拟验证，实现米级轨道精度和亚毫米/秒速度精度，满足LANS要求。

## 摘要（原文）

> This paper presents a terrestrial GNSS-based orbit and clock estimation framework for lunar navigation satellites. To enable high-precision estimation under the low-observability conditions encountered at lunar distances, we develop a stochastic-cloning UD-factorized filter and delayed-state smoother that provide enhanced numerical stability when processing precise time-differenced carrier phase (TDCP) measurements. A comprehensive dynamics and measurement model is formulated, explicitly accounting for relativistic coupling between orbital and clock states, lunar time-scale transformations, and signal propagation delays including ionospheric, plasmaspheric, and Shapiro effects. The proposed approach is evaluated using high-fidelity Monte-Carlo simulations incorporating realistic multi-constellation GNSS geometry, broadcast ephemeris errors, lunar satellite dynamics, and ionospheric and plasmaspheric delay computed from empirical electron density models. Simulation results demonstrate that combining ionosphere-free pseudorange and TDCP measurements achieves meter-level orbit accuracy and sub-millimeter-per-second velocity accuracy, satisfying the stringent signal-in-space error requirements of future Lunar Augmented Navigation Services (LANS).

