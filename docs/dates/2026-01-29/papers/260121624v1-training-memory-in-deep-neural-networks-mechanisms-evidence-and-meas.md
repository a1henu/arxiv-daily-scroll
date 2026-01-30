---
layout: default
title: Training Memory in Deep Neural Networks: Mechanisms, Evidence, and Measurement Gaps
---

# Training Memory in Deep Neural Networks: Mechanisms, Evidence, and Measurement Gaps
**arXiv**：[2601.21624v1](https://arxiv.org/abs/2601.21624) · [PDF](https://arxiv.org/pdf/2601.21624.pdf)  
**作者**：Vasileios Sevetlidis, George Pavlidis  

**一句话要点**：提出训练记忆测量协议，以因果方式评估深度学习训练中历史依赖的影响

**关键词**：训练记忆, 深度学习优化, 因果估计, 扰动原语, 测量协议, 审计工具

## 3 点简述
- 核心问题：深度学习训练非无记忆，依赖优化器状态、数据顺序等机制，影响模型性能
- 方法要点：组织机制分类，引入因果估计量和便携扰动原语，用于测量训练记忆
- 实验或效果：提供报告清单和审计工具，支持跨模型、数据和训练制度的可移植因果测量

## 摘要（原文）

> Modern deep-learning training is not memoryless. Updates depend on optimizer moments and averaging, data-order policies (random reshuffling vs with-replacement, staged augmentations and replay), the nonconvex path, and auxiliary state (teacher EMA/SWA, contrastive queues, BatchNorm statistics). This survey organizes mechanisms by source, lifetime, and visibility. It introduces seed-paired, function-space causal estimands; portable perturbation primitives (carry/reset of momentum/Adam/EMA/BN, order-window swaps, queue/teacher tweaks); and a reporting checklist with audit artifacts (order hashes, buffer/BN checksums, RNG contracts). The conclusion is a protocol for portable, causal, uncertainty-aware measurement that attributes how much training history matters across models, data, and regimes.

