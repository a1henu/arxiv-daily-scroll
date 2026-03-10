---
layout: default
title: Trajectory Tracking Control Design for Autonomous Helicopters with Guaranteed Error Bounds
---

# Trajectory Tracking Control Design for Autonomous Helicopters with Guaranteed Error Bounds
**arXiv**：[2603.08045v1](https://arxiv.org/abs/2603.08045) · [PDF](https://arxiv.org/pdf/2603.08045.pdf)  
**作者**：Philipp Schitz, Johann C. Dauer, Paolo Mercorelli  

**一句话要点**：提出基于鲁棒正不变集框架，为自主直升机轨迹跟踪计算形式化保证的误差界。

**关键词**：自主直升机, 轨迹跟踪, 鲁棒正不变集, 误差界保证, 控制器架构比较, 非线性仿真

## 3 点简述
- 核心问题：自主直升机轨迹跟踪中，如何形式化保证误差界以支持上层轨迹规划。
- 方法要点：建立闭环平移误差动力学，采用多面体线性参数变化形式，计算椭球鲁棒正不变集。
- 实验或效果：在非线性直升机模型上仿真，比较三种控制器架构，验证误差界并分析保守性与性能权衡。

## 摘要（原文）

> This paper presents a systematic framework for computing formally guaranteed trajectory tracking error bounds for autonomous helicopters based on Robust Positive Invariant (RPI) sets. The approach focuses on establishing a closed-loop translational error dynamics which is cast into polytopic linear parameter-varying form with bounded additive and state-dependent disturbances. Ellipsoidal RPI sets are computed, yielding explicit position error bounds suitable as certified buffer zones in upper-level trajectory planning. Three controller architectures are compared with respect to the conservatism of their error bounds and tracking performance. Simulation results on a nonlinear helicopter model demonstrate that all architectures respect the derived bounds, while highlighting trade-offs between dynamical fidelity and conservatism in invariant set computation.

