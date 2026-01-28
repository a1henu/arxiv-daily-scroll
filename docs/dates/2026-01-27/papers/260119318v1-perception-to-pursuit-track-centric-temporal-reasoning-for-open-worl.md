---
layout: default
title: Perception-to-Pursuit: Track-Centric Temporal Reasoning for Open-World Drone Detection and Autonomous Chasing
---

# Perception-to-Pursuit: Track-Centric Temporal Reasoning for Open-World Drone Detection and Autonomous Chasing
**arXiv**：[2601.19318v1](https://arxiv.org/abs/2601.19318) · [PDF](https://arxiv.org/pdf/2601.19318.pdf)  
**作者**：Venkatakrishna Reddy Oruganti  

**一句话要点**：提出Perception-to-Pursuit框架，通过轨迹中心时序推理解决无人机自主追逐中的预测与拦截可行性问题。

**关键词**：无人机检测, 自主追逐, 时序推理, 轨迹预测, 拦截可行性, Transformer模型

## 3 点简述
- 现有跟踪方法忽略追逐可行性，导致99.9%的预测轨迹无法物理拦截。
- P2P使用8维运动令牌和因果Transformer，在12帧内推理未来行为以实现可行动追逐规划。
- 在Anti-UAV-RGBT数据集上，P2P提升轨迹预测77%，拦截成功率提高597倍，保持100%分类准确率。

## 摘要（原文）

> Autonomous drone pursuit requires not only detecting drones but also predicting their trajectories in a manner that enables kinematically feasible interception. Existing tracking methods optimize for prediction accuracy but ignore pursuit feasibility, resulting in trajectories that are physically impossible to intercept 99.9% of the time. We propose Perception-to-Pursuit (P2P), a track-centric temporal reasoning framework that bridges detection and actionable pursuit planning. Our method represents drone motion as compact 8-dimensional tokens capturing velocity, acceleration, scale, and smoothness, enabling a 12-frame causal transformer to reason about future behavior. We introduce the Intercept Success Rate (ISR) metric to measure pursuit feasibility under realistic interceptor constraints. Evaluated on the Anti-UAV-RGBT dataset with 226 real drone sequences, P2P achieves 28.12 pixel average displacement error and 0.597 ISR, representing a 77% improvement in trajectory prediction and 597x improvement in pursuit feasibility over tracking-only baselines, while maintaining perfect drone classification accuracy (100%). Our work demonstrates that temporal reasoning over motion patterns enables both accurate prediction and actionable pursuit planning.

