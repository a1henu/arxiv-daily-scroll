---
layout: default
title: Oscillators Are All You Need: Irregular Time Series Modelling via Damped Harmonic Oscillators with Closed-Form Solutions
---

# Oscillators Are All You Need: Irregular Time Series Modelling via Damped Harmonic Oscillators with Closed-Form Solutions
**arXiv**：[2602.12139v1](https://arxiv.org/abs/2602.12139) · [PDF](https://arxiv.org/pdf/2602.12139.pdf)  
**作者**：Yashas Shende, Aritra Das, Reva Laxmi Chauhan, Arghya Pathak, Debayan Gupta  

**一句话要点**：提出基于阻尼谐振子闭式解的方法，以高效建模不规则时间序列

**关键词**：不规则时间序列, 阻尼谐振子, 闭式解, 注意力机制, 计算效率, 连续时间建模

## 3 点简述
- 核心问题：Transformer处理不规则时间序列时因假设均匀间隔而受限，现有方法如ContiFormer计算开销大
- 方法要点：用阻尼谐振子类比键值，闭式解替代数值求解，通过共振现象模拟注意力机制
- 实验或效果：在基准测试中实现最佳性能，计算速度显著提升，保持通用逼近性质

## 摘要（原文）

> Transformers excel at time series modelling through attention mechanisms that capture long-term temporal patterns. However, they assume uniform time intervals and therefore struggle with irregular time series. Neural Ordinary Differential Equations (NODEs) effectively handle irregular time series by modelling hidden states as continuously evolving trajectories. ContiFormers arxiv:2402.10635 combine NODEs with Transformers, but inherit the computational bottleneck of the former by using heavy numerical solvers. This bottleneck can be removed by using a closed-form solution for the given dynamical system - but this is known to be intractable in general! We obviate this by replacing NODEs with a novel linear damped harmonic oscillator analogy - which has a known closed-form solution. We model keys and values as damped, driven oscillators and expand the query in a sinusoidal basis up to a suitable number of modes. This analogy naturally captures the query-key coupling that is fundamental to any transformer architecture by modelling attention as a resonance phenomenon. Our closed-form solution eliminates the computational overhead of numerical ODE solvers while preserving expressivity. We prove that this oscillator-based parameterisation maintains the universal approximation property of continuous-time attention; specifically, any discrete attention matrix realisable by ContiFormer's continuous keys can be approximated arbitrarily well by our fixed oscillator modes. Our approach delivers both theoretical guarantees and scalability, achieving state-of-the-art performance on irregular time series benchmarks while being orders of magnitude faster.

