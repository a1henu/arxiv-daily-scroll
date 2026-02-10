---
layout: default
title: Time-Delayed Transformers for Data-Driven Modeling of Low-Dimensional Dynamics
---

# Time-Delayed Transformers for Data-Driven Modeling of Low-Dimensional Dynamics
**arXiv**：[2602.08478v1](https://arxiv.org/abs/2602.08478) · [PDF](https://arxiv.org/pdf/2602.08478.pdf)  
**作者**：Albert Alcalde, Markus Widhalm, Emre Yılmaz  

**一句话要点**：提出时间延迟变换器，用于数据驱动建模低维非稳态时空动力学。

**关键词**：时间延迟变换器, 数据驱动建模, 非稳态动力学, 低维系统, 变换器架构

## 3 点简述
- 核心问题：数据驱动建模非稳态时空动力学，桥接线性算子方法与深度序列模型。
- 方法要点：设计简化单层单头变换器，解释为时间延迟动态模态分解的非线性推广。
- 实验效果：在线性系统匹配基线，非线性混沌系统显著优于线性方法，保持可解释性与高效性。

## 摘要（原文）

> We propose the time-delayed transformer (TD-TF), a simplified transformer architecture for data-driven modeling of unsteady spatio-temporal dynamics. TD-TF bridges linear operator-based methods and deep sequence models by showing that a single-layer, single-head transformer can be interpreted as a nonlinear generalization of time-delayed dynamic mode decomposition (TD-DMD). The architecture is deliberately minimal, consisting of one self-attention layer with a single query per prediction and one feedforward layer, resulting in linear computational complexity in sequence length and a small parameter count. Numerical experiments demonstrate that TD-TF matches the performance of strong linear baselines on near-linear systems, while significantly outperforming them in nonlinear and chaotic regimes, where it accurately captures long-term dynamics. Validation studies on synthetic signals, unsteady aerodynamics, the Lorenz '63 system, and a reaction-diffusion model show that TD-TF preserves the interpretability and efficiency of linear models while providing substantially enhanced expressive power for complex dynamics.

