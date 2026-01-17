---
layout: default
title: Continuous-Depth Transformers with Learned Control Dynamics
---

# Continuous-Depth Transformers with Learned Control Dynamics
**arXiv**：[2601.10007v1](https://arxiv.org/abs/2601.10007) · [PDF](https://arxiv.org/pdf/2601.10007.pdf)  
**作者**：Peter Jemley  

**一句话要点**：提出连续深度变换器，通过学习的控制信号实现生成属性的推理时控制。

**关键词**：连续深度变换器, 神经ODE, 可控生成, 向量场学习, 推理时控制

## 3 点简述
- 核心问题：标准变换器使用离散层处理表示，缺乏深度连续性和可控性。
- 方法要点：用连续深度神经ODE块替换离散中间层，引入低维控制信号调节向量场。
- 实验或效果：验证梯度稳定性、语义控制准确性、连续插值精度和效率对标基线。

## 摘要（原文）

> We present a hybrid transformer architecture that replaces discrete middle layers with a continuous-depth Neural Ordinary Differential Equation (ODE) block, enabling inference-time control over generation attributes via a learned steering signal. Unlike standard transformers that process representations through fixed discrete layers, our approach treats depth as a continuous variable governed by a learned vector field $F_θ(H, τ, u)$, where $u$ is a low-dimensional control signal injected via explicit concatenation. We validate the architecture through four experiments: (1) gradient flow stability with zero exploding/vanishing gradient events, (2) semantic steering achieving 98\%/88\% accuracy for positive/negative sentiment control, (3) continuous interpolation validated by a negligible 0.068\% trajectory divergence between fixed and adaptive solvers, and (4) efficiency benchmarking demonstrating latency parity with standard discrete baselines. Additionally, we show that adaptive ODE solvers reveal geometric structure in the learned dynamics: the control signal partitions the vector field into distinct dynamical regimes with different curvature characteristics. The adjoint method enables $O(1)$ memory training regardless of integration depth. Our results demonstrate that continuous-depth dynamics with learned control signals provide a viable, efficient mechanism for steerable language generation.

