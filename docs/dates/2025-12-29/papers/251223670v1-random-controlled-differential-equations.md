---
layout: default
title: Random Controlled Differential Equations
---

# Random Controlled Differential Equations
**arXiv**：[2512.23670v1](https://arxiv.org/abs/2512.23670) · [PDF](https://arxiv.org/pdf/2512.23670.pdf)  
**作者**：Francesco Piatti, Thomas Cass, William F. Turner  

**一句话要点**：提出随机控制微分方程框架，结合随机特征与CDE实现高效时间序列学习。

**关键词**：时间序列学习, 控制微分方程, 随机特征, 路径签名理论, 连续时间模型

## 3 点简述
- 核心问题：时间序列学习需高效模型以处理连续时间数据并捕获高阶交互。
- 方法要点：使用随机参数化CDE作为连续时间储层，仅训练线性读出层，提出RF-CDE和R-RDE变体。
- 实验或效果：在多个基准测试中展示竞争性或最先进性能，提供签名计算的实用替代方案。

## 摘要（原文）

> We introduce a training-efficient framework for time-series learning that combines random features with controlled differential equations (CDEs). In this approach, large randomly parameterized CDEs act as continuous-time reservoirs, mapping input paths to rich representations. Only a linear readout layer is trained, resulting in fast, scalable models with strong inductive bias. Building on this foundation, we propose two variants: (i) Random Fourier CDEs (RF-CDEs): these lift the input signal using random Fourier features prior to the dynamics, providing a kernel-free approximation of RBF-enhanced sequence models; (ii) Random Rough DEs (R-RDEs): these operate directly on rough-path inputs via a log-ODE discretization, using log-signatures to capture higher-order temporal interactions while remaining stable and efficient. We prove that in the infinite-width limit, these model induces the RBF-lifted signature kernel and the rough signature kernel, respectively, offering a unified perspective on random-feature reservoirs, continuous-time deep architectures, and path-signature theory.
>   We evaluate both models across a range of time-series benchmarks, demonstrating competitive or state-of-the-art performance. These methods provide a practical alternative to explicit signature computations, retaining their inductive bias while benefiting from the efficiency of random features.

