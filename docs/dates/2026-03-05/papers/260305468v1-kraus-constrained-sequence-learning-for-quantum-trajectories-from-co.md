---
layout: default
title: Kraus Constrained Sequence Learning For Quantum Trajectories from Continuous Measurement
---

# Kraus Constrained Sequence Learning For Quantum Trajectories from Continuous Measurement
**arXiv**：[2603.05468v1](https://arxiv.org/abs/2603.05468) · [PDF](https://arxiv.org/pdf/2603.05468.pdf)  
**作者**：Priyanshi Singh, Krishna Bhatia  

**一句话要点**：提出Kraus结构输出层以解决量子轨迹连续测量中物理约束违反问题

**关键词**：量子轨迹重建, 连续测量, 物理约束学习, Kraus结构, 序列模型, 量子反馈控制

## 3 点简述
- 核心问题：标准SME求解器需精确模型，无约束神经网络预测可能违反量子态物理性
- 方法要点：通过Kraus结构输出层将序列模型隐藏表示转换为CPTP量子操作，确保物理有效更新
- 实验或效果：Kraus-LSTM在参数漂移轨迹上提升状态估计质量7%，保证非平稳区域物理有效预测

## 摘要（原文）

> Real-time reconstruction of conditional quantum states from continuous measurement records is a fundamental requirement for quantum feedback control, yet standard stochastic master equation (SME) solvers require exact model specification, known system parameters, and are sensitive to parameter mismatch. While neural sequence models can fit these stochastic dynamics, the unconstrained predictors can violate physicality such as positivity or trace constraints, leading to unstable rollouts and unphysical estimates. We propose a Kraus-structured output layer that converts the hidden representation of a generic sequence backbone into a completely positive trace preserving (CPTP) quantum operation, yielding physically valid state updates by construction. We instantiate this layer across diverse backbones, RNN, GRU, LSTM, TCN, ESN and Mamba; including Neural ODE as a comparative baseline, on stochastic trajectories characterized by parameter drift. Our evaluation reveals distinct trade-offs between gating mechanisms, linear recurrence, and global attention. Across all models, Kraus-LSTM achieves the strongest results, improving state estimation quality by 7% over its unconstrained counterpart while guaranteeing physically valid predictions in non-stationary regimes.

