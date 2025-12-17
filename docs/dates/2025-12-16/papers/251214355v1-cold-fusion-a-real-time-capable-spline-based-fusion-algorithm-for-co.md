---
layout: default
title: CoLD Fusion: A Real-time Capable Spline-based Fusion Algorithm for Collective Lane Detection
---

# CoLD Fusion: A Real-time Capable Spline-based Fusion Algorithm for Collective Lane Detection
**arXiv**：[2512.14355v1](https://arxiv.org/abs/2512.14355) · [PDF](https://arxiv.org/pdf/2512.14355.pdf)  
**作者**：Jörg Gamerdinger, Sven Teufel, Georg Volk, Oliver Bringmann  

**一句话要点**：提出基于样条的实时集体车道检测融合算法，以扩展感知范围并应对遮挡和曲线场景。

**关键词**：集体感知, 车道检测, 样条估计, 实时融合, 自动驾驶, 车对车通信

## 3 点简述
- 核心问题：传感器限制和遮挡导致车道检测不完整，影响自动驾驶安全规划。
- 方法要点：利用车对车通信实现集体感知，采用样条估计未检测路段，确保实时性。
- 实验或效果：在多种路况下评估，感知范围扩展达200%，具备实时处理能力。

## 摘要（原文）

> Comprehensive environment perception is essential for autonomous vehicles to operate safely. It is crucial to detect both dynamic road users and static objects like traffic signs or lanes as these are required for safe motion planning. However, in many circumstances a complete perception of other objects or lanes is not achievable due to limited sensor ranges, occlusions, and curves. In scenarios where an accurate localization is not possible or for roads where no HD maps are available, an autonomous vehicle must rely solely on its perceived road information. Thus, extending local sensing capabilities through collective perception using vehicle-to-vehicle communication is a promising strategy that has not yet been explored for lane detection. Therefore, we propose a real-time capable approach for collective perception of lanes using a spline-based estimation of undetected road sections. We evaluate our proposed fusion algorithm in various situations and road types. We were able to achieve real-time capability and extend the perception range by up to 200%.

