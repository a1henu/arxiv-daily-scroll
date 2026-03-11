---
layout: default
title: Physics-Informed Neural Engine Sound Modeling with Differentiable Pulse-Train Synthesis
---

# Physics-Informed Neural Engine Sound Modeling with Differentiable Pulse-Train Synthesis
**arXiv**：[2603.09391v1](https://arxiv.org/abs/2603.09391) · [PDF](https://arxiv.org/pdf/2603.09391.pdf)  
**作者**：Robin Doerfler, Lonce Wyse  

**一句话要点**：提出脉冲序列谐振器模型以直接建模发动机声音的物理脉冲结构

**关键词**：物理信息神经网络, 可微分音频合成, 脉冲序列建模, 发动机声音模拟, 谐振器架构

## 3 点简述
- 核心问题：发动机声音源于排气压力脉冲，而非持续谐波振荡，现有神经合成方法通常仅近似频谱特征。
- 方法要点：使用可微分脉冲序列合成架构，参数化脉冲序列对齐发动机点火模式，并通过递归Karplus-Strong谐振器模拟排气声学。
- 实验或效果：在三种发动机类型上验证，谐波重建提升21%，总损失降低5.7%，提供可解释的物理参数。

## 摘要（原文）

> Engine sounds originate from sequential exhaust pressure pulses rather than sustained harmonic oscillations. While neural synthesis methods typically aim to approximate the resulting spectral characteristics, we propose directly modeling the underlying pulse shapes and temporal structure. We present the Pulse-Train-Resonator (PTR) model, a differentiable synthesis architecture that generates engine audio as parameterized pulse trains aligned to engine firing patterns and propagates them through recursive Karplus-Strong resonators simulating exhaust acoustics. The architecture integrates physics-informed inductive biases including harmonic decay, thermodynamic pitch modulation, valve-dynamics envelopes, exhaust system resonances and derived engine operating modes such as throttle operation and deceleration fuel cutoff (DCFO).
>   Validated on three diverse engine types totaling 7.5 hours of audio, PTR achieves a 21% improvement in harmonic reconstruction and a 5.7% reduction in total loss over a harmonic-plus-noise baseline model, while providing interpretable parameters corresponding to physical phenomena.
>   Complete code, model weights, and audio examples are openly available.

