---
layout: default
title: Error Amplification Limits ANN-to-SNN Conversion in Continuous Control
---

# Error Amplification Limits ANN-to-SNN Conversion in Continuous Control
**arXiv**：[2601.21778v1](https://arxiv.org/abs/2601.21778) · [PDF](https://arxiv.org/pdf/2601.21778.pdf)  
**作者**：Zijie Xu, Zihan Huang, Yiting Dong, Kang Chen, Wenxuan Liu, Zhaofei Yu  

**一句话要点**：提出跨步残差电位初始化以抑制连续控制中ANN转SNN的误差放大问题

**关键词**：脉冲神经网络转换, 连续控制, 误差放大, 残差电位初始化, 强化学习

## 3 点简述
- 核心问题：连续控制中ANN转SNN时，小动作近似误差跨决策步时间相关，导致累积状态分布偏移和性能下降
- 方法要点：提出CRPI，一种轻量级免训练机制，通过跨步传递残差膜电位来抑制时间相关误差
- 实验或效果：在向量和视觉观测的连续控制基准上，CRPI集成现有转换流程，显著恢复性能损失

## 摘要（原文）

> Spiking Neural Networks (SNNs) can achieve competitive performance by converting already existing well-trained Artificial Neural Networks (ANNs), avoiding further costly training. This property is particularly attractive in Reinforcement Learning (RL), where training through environment interaction is expensive and potentially unsafe. However, existing conversion methods perform poorly in continuous control, where suitable baselines are largely absent. We identify error amplification as the key cause: small action approximation errors become temporally correlated across decision steps, inducing cumulative state distribution shift and severe performance degradation. To address this issue, we propose Cross-Step Residual Potential Initialization (CRPI), a lightweight training-free mechanism that carries over residual membrane potentials across decision steps to suppress temporally correlated errors. Experiments on continuous control benchmarks with both vector and visual observations demonstrate that CRPI can be integrated into existing conversion pipelines and substantially recovers lost performance. Our results highlight continuous control as a critical and challenging benchmark for ANN-to-SNN conversion, where small errors can be strongly amplified and impact performance.

