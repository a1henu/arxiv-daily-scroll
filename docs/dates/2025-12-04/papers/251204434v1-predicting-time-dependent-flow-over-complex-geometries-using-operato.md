---
layout: default
title: Predicting Time-Dependent Flow Over Complex Geometries Using Operator Networks
---

# Predicting Time-Dependent Flow Over Complex Geometries Using Operator Networks
**arXiv**：[2512.04434v1](https://arxiv.org/abs/2512.04434) · [PDF](https://arxiv.org/pdf/2512.04434.pdf)  
**作者**：Ali Rabeh, Suresh Murugaiyan, Adarsh Krishnamurthy, Baskar Ganapathysubramanian  

**一句话要点**：提出时间依赖的几何感知深度算子网络，以预测参数化与非参数化形状周围的中等雷诺数非定常流场。

**关键词**：非定常流预测, 深度算子网络, 几何感知建模, 计算流体力学加速, 符号距离场, 误差分析

## 3 点简述
- 核心问题：快速且泛化几何的非定常流代理模型仍具挑战。
- 方法要点：使用符号距离场编码几何和CNN分支编码流历史，基于841个高保真模拟训练。
- 实验或效果：在未见形状上实现约5%相对L2单步误差和高达1000倍加速，但精细尾流中误差累积。

## 摘要（原文）

> Fast, geometry-generalizing surrogates for unsteady flow remain challenging. We present a time-dependent, geometry-aware Deep Operator Network that predicts velocity fields for moderate-Re flows around parametric and non-parametric shapes. The model encodes geometry via a signed distance field (SDF) trunk and flow history via a CNN branch, trained on 841 high-fidelity simulations. On held-out shapes, it attains $\sim 5\%$ relative L2 single-step error and up to 1000X speedups over CFD. We provide physics-centric rollout diagnostics, including phase error at probes and divergence norms, to quantify long-horizon fidelity. These reveal accurate near-term transients but error accumulation in fine-scale wakes, most pronounced for sharp-cornered geometries. We analyze failure modes and outline practical mitigations. Code, splits, and scripts are openly released at: https://github.com/baskargroup/TimeDependent-DeepONet to support reproducibility and benchmarking.

