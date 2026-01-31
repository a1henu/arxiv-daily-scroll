---
layout: default
title: Bi-Anchor Interpolation Solver for Accelerating Generative Modeling
---

# Bi-Anchor Interpolation Solver for Accelerating Generative Modeling
**arXiv**：[2601.21542v1](https://arxiv.org/abs/2601.21542) · [PDF](https://arxiv.org/pdf/2601.21542.pdf)  
**作者**：Hongxu Chen, Hongxiang Li, Zhen Wang, Long Chen  

**一句话要点**：提出双锚点插值求解器以加速流匹配生成模型，通过轻量SideNet实现高效推理。

**关键词**：流匹配模型, ODE求解加速, 轻量SideNet, 双向时间感知, 图像生成, 训练成本优化

## 3 点简述
- 核心问题：流匹配模型依赖迭代ODE求解导致高延迟，现有方法在性能与成本间存在权衡。
- 方法要点：引入轻量SideNet学习双向时间感知，结合双锚点速度积分实现大间隔高效近似。
- 实验或效果：在ImageNet-256^2上，10步NFEs达到100+步欧拉求解器质量，训练成本可忽略。

## 摘要（原文）

> Flow Matching (FM) models have emerged as a leading paradigm for high-fidelity synthesis. However, their reliance on iterative Ordinary Differential Equation (ODE) solving creates a significant latency bottleneck. Existing solutions face a dichotomy: training-free solvers suffer from significant performance degradation at low Neural Function Evaluations (NFEs), while training-based one- or few-steps generation methods incur prohibitive training costs and lack plug-and-play versatility. To bridge this gap, we propose the Bi-Anchor Interpolation Solver (BA-solver). BA-solver retains the versatility of standard training-free solvers while achieving significant acceleration by introducing a lightweight SideNet (1-2% backbone size) alongside the frozen backbone. Specifically, our method is founded on two synergistic components: \textbf{1) Bidirectional Temporal Perception}, where the SideNet learns to approximate both future and historical velocities without retraining the heavy backbone; and 2) Bi-Anchor Velocity Integration, which utilizes the SideNet with two anchor velocities to efficiently approximate intermediate velocities for batched high-order integration. By utilizing the backbone to establish high-precision ``anchors'' and the SideNet to densify the trajectory, BA-solver enables large interval sizes with minimized error. Empirical results on ImageNet-256^2 demonstrate that BA-solver achieves generation quality comparable to 100+ NFEs Euler solver in just 10 NFEs and maintains high fidelity in as few as 5 NFEs, incurring negligible training costs. Furthermore, BA-solver ensures seamless integration with existing generative pipelines, facilitating downstream tasks such as image editing.

