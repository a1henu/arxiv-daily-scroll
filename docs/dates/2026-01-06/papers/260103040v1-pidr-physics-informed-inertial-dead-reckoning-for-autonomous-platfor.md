---
layout: default
title: PiDR: Physics-Informed Inertial Dead Reckoning for Autonomous Platforms
---

# PiDR: Physics-Informed Inertial Dead Reckoning for Autonomous Platforms
**arXiv**：[2601.03040v1](https://arxiv.org/abs/2601.03040) · [PDF](https://arxiv.org/pdf/2601.03040.pdf)  
**作者**：Arup Kumar Sahoo, Itzik Klein  

**一句话要点**：提出PiDR框架，通过物理信息残差组件提升纯惯性导航精度与泛化能力。

**关键词**：惯性导航, 物理信息学习, 残差网络, 自主平台, 传感器融合

## 3 点简述
- 纯惯性导航中传感器噪声导致轨迹漂移，传统深度学习模型缺乏透明性且难以学习物理原理。
- PiDR集成惯性导航物理原理于网络训练，通过物理信息残差组件增强模型透明性与鲁棒性。
- 在移动机器人和自主水下车辆数据集上评估，位置精度提升超过29%，展示跨平台泛化能力。

## 摘要（原文）

> A fundamental requirement for full autonomy is the ability to sustain accurate navigation in the absence of external data, such as GNSS signals or visual information. In these challenging environments, the platform must rely exclusively on inertial sensors, leading to pure inertial navigation. However, the inherent noise and other error terms of the inertial sensors in such real-world scenarios will cause the navigation solution to drift over time. Although conventional deep-learning models have emerged as a possible approach to inertial navigation, they are inherently black-box in nature. Furthermore, they struggle to learn effectively with limited supervised sensor data and often fail to preserve physical principles. To address these limitations, we propose PiDR, a physics-informed inertial dead-reckoning framework for autonomous platforms in situations of pure inertial navigation. PiDR offers transparency by explicitly integrating inertial navigation principles into the network training process through the physics-informed residual component. PiDR plays a crucial role in mitigating abrupt trajectory deviations even under limited or sparse supervision. We evaluated PiDR on real-world datasets collected by a mobile robot and an autonomous underwater vehicle. We obtained more than 29% positioning improvement in both datasets, demonstrating the ability of PiDR to generalize different platforms operating in various environments and dynamics. Thus, PiDR offers a robust, lightweight, yet effective architecture and can be deployed on resource-constrained platforms, enabling real-time pure inertial navigation in adverse scenarios.

