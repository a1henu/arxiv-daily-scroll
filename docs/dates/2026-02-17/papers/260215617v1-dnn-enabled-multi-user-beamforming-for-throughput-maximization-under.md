---
layout: default
title: DNN-Enabled Multi-User Beamforming for Throughput Maximization under Adjustable Fairness
---

# DNN-Enabled Multi-User Beamforming for Throughput Maximization under Adjustable Fairness
**arXiv**：[2602.15617v1](https://arxiv.org/abs/2602.15617) · [PDF](https://arxiv.org/pdf/2602.15617.pdf)  
**作者**：Kaifeng Lu, Markus Rupp, Stefan Schwarz  

**一句话要点**：提出基于无线Transformer的无监督学习框架，通过拉格朗日乘子优化多用户波束赋形，在可调公平性下最大化吞吐量。

**关键词**：多用户波束赋形, 公平性优化, 无线Transformer, 无监督学习, 拉格朗日乘子, 吞吐量最大化

## 3 点简述
- 核心问题：无线通信中公平性与总速率间的非凸多目标优化，复杂度随网络规模增长。
- 方法要点：使用无线Transformer从信道状态信息学习，结合拉格朗日乘子自动更新，实现可控公平约束。
- 实验或效果：方法在指定公平性下灵活管理权衡，有效逼近帕累托前沿，提升优化性能。

## 摘要（原文）

> Ensuring user fairness in wireless communications is a fundamental challenge, as balancing the trade-off between fairness and sum rate leads to a non-convex, multi-objective optimization whose complexity grows with network scale. To alleviate this conflict, we propose an optimization-based unsupervised learning approach based on the wireless transformer (WiT) architecture that learns from channel state information (CSI) features. We reformulate the trade-off by combining the sum rate and fairness objectives through a Lagrangian multiplier, which is updated automatically via a dual-ascent algorithm. This mechanism allows for a controllable fairness constraint while simultaneously maximizing the sum rate, effectively realizing a trace on the Pareto front between two conflicting objectives. Our findings show that the proposed approach offers a flexible solution for managing the trade-off optimization under prescribed fairness.

