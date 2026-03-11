---
layout: default
title: WESPR: Wind-adaptive Energy-Efficient Safe Perception & Planning for Robust Flight with Quadrotors
---

# WESPR: Wind-adaptive Energy-Efficient Safe Perception & Planning for Robust Flight with Quadrotors
**arXiv**：[2603.09194v1](https://arxiv.org/abs/2603.09194) · [PDF](https://arxiv.org/pdf/2603.09194.pdf)  
**作者**：Khuzema Habib, Pranav Deshakulkarni Manjunath, Kasra Torshizi, Troi Williams, Pratap Tokekar  

**一句话要点**：提出WESPR框架，通过预测环境几何对风场的影响，实现四旋翼无人机在复杂环境中的高效安全飞行规划与控制。

**关键词**：无人机导航, 风场预测, 路径规划, 自适应控制, 几何感知, 实时系统

## 3 点简述
- 核心问题：现有方法依赖计算昂贵的流体模拟，无法实时适应新环境，导致无人机在风扰下性能受限。
- 方法要点：集成几何感知与天气数据，快速预测风场，优化路径规划与控制策略，处理时间在10秒内。
- 实验或效果：在Crazyflie无人机上验证，相比无风感知控制器，最大轨迹偏差减少12.5-58.7%，稳定性提升24.6%。

## 摘要（原文）

> Local wind conditions strongly influence drone performance: headwinds increase flight time, crosswinds and wind shear hinder agility in cluttered spaces, while tailwinds reduce travel time. Although adaptive controllers can mitigate turbulence, they remain unaware of the surrounding geometry that generates it, preventing proactive avoidance. Existing methods that model how wind interacts with the environment typically rely on computationally expensive fluid dynamics simulations, limiting real-time adaptation to new environments and conditions. To bridge this gap, we present WESPR, a fast framework that predicts how environmental geometry affects local wind conditions, enabling proactive path planning and control adaptation. Our lightweight pipeline integrates geometric perception and local weather data to estimate wind fields, compute cost-efficient paths, and adjust control strategies-all within 10 seconds. We validate WESPR on a Crazyflie drone navigating turbulent obstacle courses. Our results show a 12.5-58.7% reduction in maximum trajectory deviation and a 24.6% improvement in stability compared to a wind-agnostic adaptive controller.

