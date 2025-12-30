---
layout: default
title: A Kalman Filter-Based Disturbance Observer for Steer-by-Wire Systems
---

# A Kalman Filter-Based Disturbance Observer for Steer-by-Wire Systems
**arXiv**：[2512.23593v1](https://arxiv.org/abs/2512.23593) · [PDF](https://arxiv.org/pdf/2512.23593.pdf)  
**作者**：Nikolai Beving, Jonas Marxen, Steffen Mueller, Johannes Betz  

**一句话要点**：提出基于卡尔曼滤波的扰动观测器，用于线控转向系统估计高频驾驶员扭矩扰动。

**关键词**：线控转向系统, 扰动观测器, 卡尔曼滤波, 驾驶员扭矩估计, 非线性系统建模, 仿真验证

## 3 点简述
- 线控转向系统易受驾驶员阻抗产生的高频扰动影响，传统方法成本高或分辨率不足。
- 设计卡尔曼滤波观测器，仅用电机状态测量，通过PT1滞后模型扩展状态估计扰动。
- 仿真验证显示非线性扩展卡尔曼滤波优于线性版本，延迟约14ms，需进一步真实环境测试。

## 摘要（原文）

> Steer-by-Wire systems replace mechanical linkages, which provide benefits like weight reduction, design flexibility, and compatibility with autonomous driving. However, they are susceptible to high-frequency disturbances from unintentional driver torque, known as driver impedance, which can degrade steering performance. Existing approaches either rely on direct torque sensors, which are costly and impractical, or lack the temporal resolution to capture rapid, high-frequency driver-induced disturbances. We address this limitation by designing a Kalman filter-based disturbance observer that estimates high-frequency driver torque using only motor state measurements. We model the drivers passive torque as an extended state using a PT1-lag approximation and integrate it into both linear and nonlinear Steer-by-Wire system models. In this paper, we present the design, implementation and simulation of this disturbance observer with an evaluation of different Kalman filter variants. Our findings indicate that the proposed disturbance observer accurately reconstructs driver-induced disturbances with only minimal delay 14ms. We show that a nonlinear extended Kalman Filter outperforms its linear counterpart in handling frictional nonlinearities, improving estimation during transitions from static to dynamic friction. Given the study's methodology, it was unavoidable to rely on simulation-based validation rather than real-world experimentation. Further studies are needed to investigate the robustness of the observers under real-world driving conditions.

