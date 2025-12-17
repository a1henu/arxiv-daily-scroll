---
layout: default
title: A Comprehensive Safety Metric to Evaluate Perception in Autonomous Systems
---

# A Comprehensive Safety Metric to Evaluate Perception in Autonomous Systems
**arXiv**：[2512.14367v1](https://arxiv.org/abs/2512.14367) · [PDF](https://arxiv.org/pdf/2512.14367.pdf)  
**作者**：Georg Volk, Jörg Gamerdinger, Alexander von Bernuth, Oliver Bringmann  

**一句话要点**：提出综合安全度量以评估自动驾驶系统中的感知性能

**关键词**：自动驾驶感知, 安全评估指标, 对象重要性, 综合度量, 感知性能评估

## 3 点简述
- 核心问题：现有对象感知评估指标未考虑对象重要性差异，如速度、距离等参数对安全的影响。
- 方法要点：设计新安全度量，整合对象速度、方向、距离、尺寸和潜在碰撞伤害等多参数，输出单一可解释安全评分。
- 实验或效果：使用真实世界和虚拟数据集评估新度量，并与现有先进指标进行比较验证。

## 摘要（原文）

> Complete perception of the environment and its correct interpretation is crucial for autonomous vehicles. Object perception is the main component of automotive surround sensing. Various metrics already exist for the evaluation of object perception. However, objects can be of different importance depending on their velocity, orientation, distance, size, or the potential damage that could be caused by a collision due to a missed detection. Thus, these additional parameters have to be considered for safety evaluation. We propose a new safety metric that incorporates all these parameters and returns a single easily interpretable safety assessment score for object perception. This new metric is evaluated with both real world and virtual data sets and compared to state of the art metrics.

