---
layout: default
title: OMP: One-step Meanflow Policy with Directional Alignment
---

# OMP: One-step Meanflow Policy with Directional Alignment
**arXiv**：[2512.19347v1](https://arxiv.org/abs/2512.19347) · [PDF](https://arxiv.org/pdf/2512.19347.pdf)  
**作者**：Han Fang, Yize Huang, Yuheng Zhao, Paul Weng, Xiao Li, Yutong Ban  

**一句话要点**：提出OMP方法以解决机器人操作中单步推理与少样本泛化问题

**关键词**：机器人操作, 生成策略, 单步推理, 少样本泛化, 速度对齐, 实时性能

## 3 点简述
- 核心问题：现有方法如Diffusion Models推理延迟高，Flow-based Methods架构复杂，且MeanFlow在机器人任务中少样本泛化差
- 方法要点：引入轻量级Cosine Loss对齐速度方向，使用DDE优化JVP算子，改进MeanFlow策略
- 实验或效果：在Adroit和Meta-World任务中平均成功率优于MP1和FlowPolicy，提升少样本泛化与轨迹精度，保持实时性能

## 摘要（原文）

> Robot manipulation, a key capability of embodied AI, has turned to data-driven generative policy frameworks, but mainstream approaches like Diffusion Models suffer from high inference latency and Flow-based Methods from increased architectural complexity. While simply applying meanFlow on robotic tasks achieves single-step inference and outperforms FlowPolicy, it lacks few-shot generalization due to fixed temperature hyperparameters in its Dispersive Loss and misaligned predicted-true mean velocities. To solve these issues, this study proposes an improved MeanFlow-based Policies: we introduce a lightweight Cosine Loss to align velocity directions and use the Differential Derivation Equation (DDE) to optimize the Jacobian-Vector Product (JVP) operator. Experiments on Adroit and Meta-World tasks show the proposed method outperforms MP1 and FlowPolicy in average success rate, especially in challenging Meta-World tasks, effectively enhancing few-shot generalization and trajectory accuracy of robot manipulation policies while maintaining real-time performance, offering a more robust solution for high-precision robotic manipulation.

