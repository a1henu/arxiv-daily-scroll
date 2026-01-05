---
layout: default
title: NMPC-Augmented Visual Navigation and Safe Learning Control for Large-Scale Mobile Robots
---

# NMPC-Augmented Visual Navigation and Safe Learning Control for Large-Scale Mobile Robots
**arXiv**：[2601.00609v1](https://arxiv.org/abs/2601.00609) · [PDF](https://arxiv.org/pdf/2601.00609.pdf)  
**作者**：Mehdi Heydari Shahna, Pauli Mustalahti, Jouni Mattila  

**一句话要点**：提出综合导航控制框架，确保大型移动机器人在易滑地形上的稳定安全操作。

**关键词**：大型移动机器人, 视觉导航, 非线性模型预测控制, 深度神经网络控制, 安全模块, 易滑地形操作

## 3 点简述
- 核心问题：大型移动机器人在松散易滑地形上操作时，牵引力降低，影响稳定性和安全性。
- 方法要点：结合视觉位姿估计、非线性模型预测控制、深度神经网络控制策略和安全模块，实现高精度低延迟导航与鲁棒控制。
- 实验或效果：在6000公斤大型移动机器人上进行了比较实验，验证了框架的有效性和系统级安全性。

## 摘要（原文）

> A large-scale mobile robot (LSMR) is a high-order multibody system that often operates on loose, unconsolidated terrain, which reduces traction. This paper presents a comprehensive navigation and control framework for an LSMR that ensures stability and safety-defined performance, delivering robust operation on slip-prone terrain by jointly leveraging high-performance techniques. The proposed architecture comprises four main modules: (1) a visual pose-estimation module that fuses onboard sensors and stereo cameras to provide an accurate, low-latency robot pose, (2) a high-level nonlinear model predictive control that updates the wheel motion commands to correct robot drift from the robot reference pose on slip-prone terrain, (3) a low-level deep neural network control policy that approximates the complex behavior of the wheel-driven actuation mechanism in LSMRs, augmented with robust adaptive control to handle out-of-distribution disturbances, ensuring that the wheels accurately track the updated commands issued by high-level control module, and (4) a logarithmic safety module to monitor the entire robot stack and guarantees safe operation. The proposed low-level control framework guarantees uniform exponential stability of the actuation subsystem, while the safety module ensures the whole system-level safety during operation. Comparative experiments on a 6,000 kg LSMR actuated by two complex electro-hydrostatic drives, while synchronizing modules operating at different frequencies.

