---
layout: default
title: Backpropagation as Physical Relaxation: Exact Gradients in Finite Time
---

# Backpropagation as Physical Relaxation: Exact Gradients in Finite Time
**arXiv**：[2602.02281v1](https://arxiv.org/abs/2602.02281) · [PDF](https://arxiv.org/pdf/2602.02281.pdf)  
**作者**：Antonino Emanuele Scurria  

**一句话要点**：提出Dyadic Backpropagation框架，将反向传播解释为物理松弛过程，在有限时间内精确计算梯度。

**关键词**：反向传播, 物理松弛, 梯度计算, 连续动力学, 能量泛函, 有限时间收敛

## 3 点简述
- 核心问题：传统反向传播被视为符号计算，缺乏物理系统解释。
- 方法要点：基于连续时间推理和非保守系统拉格朗日理论，构建双状态空间能量泛函。
- 实验或效果：证明单位步长欧拉离散化在2L步内精确恢复标准反向传播，无近似。

## 摘要（原文）

> Backpropagation, the foundational algorithm for training neural networks, is typically understood as a symbolic computation that recursively applies the chain rule. We show it emerges exactly as the finite-time relaxation of a physical dynamical system. By formulating feedforward inference as a continuous-time process and applying Lagrangian theory of non-conservative systems to handle asymmetric interactions, we derive a global energy functional on a doubled state space encoding both activations and sensitivities. The saddle-point dynamics of this energy perform inference and credit assignment simultaneously through local interactions. We term this framework ''Dyadic Backpropagation''. Crucially, we prove that unit-step Euler discretization, the natural timescale of layer transitions, recovers standard backpropagation exactly in precisely 2L steps for an L-layer network, with no approximations. Unlike prior energy-based methods requiring symmetric weights, asymptotic convergence, or vanishing perturbations, our framework guarantees exact gradients in finite time. This establishes backpropagation as the digitally optimized shadow of a continuous physical relaxation, providing a rigorous foundation for exact gradient computation in analog and neuromorphic substrates where continuous dynamics are native.

