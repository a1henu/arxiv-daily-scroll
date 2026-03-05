---
layout: default
title: Continuous Modal Logical Neural Networks: Modal Reasoning via Stochastic Accessibility
---

# Continuous Modal Logical Neural Networks: Modal Reasoning via Stochastic Accessibility
**arXiv**：[2603.04019v1](https://arxiv.org/abs/2603.04019) · [PDF](https://arxiv.org/pdf/2603.04019.pdf)  
**作者**：Antonin Sulc  

**一句话要点**：提出连续模态逻辑神经网络，通过神经随机微分方程将模态推理从离散结构提升到连续流形。

**关键词**：模态逻辑推理, 神经随机微分方程, 逻辑信息神经网络, 连续流形, 随机扩散

## 3 点简述
- 核心问题：传统模态逻辑推理基于离散Kripke结构，难以处理连续或高维场景。
- 方法要点：使用神经随机微分方程实现模态算子，通过逻辑信息神经网络将逻辑公式嵌入训练损失。
- 实验效果：在认知、时间和道义逻辑案例中，引导神经网络生成符合逻辑约束的解决方案。

## 摘要（原文）

> We propose Fluid Logic, a paradigm in which modal logical reasoning, temporal, epistemic, doxastic, deontic, is lifted from discrete Kripke structures to continuous manifolds via Neural Stochastic Differential Equations (Neural SDEs). Each type of modal operator is backed by a dedicated Neural SDE, and nested formulas compose these SDEs in a single differentiable graph. A key instantiation is Logic-Informed Neural Networks (LINNs): analogous to Physics-Informed Neural Networks (PINNs), LINNs embed modal logical formulas such as ($\Box$ bounded) and ($\Diamond$ visits\_lobe) directly into the training loss, guiding neural networks to produce solutions that are structurally consistent with prescribed logical properties, without requiring knowledge of the governing equations.
>   The resulting framework, Continuous Modal Logical Neural Networks (CMLNNs), yields several key properties: (i) stochastic diffusion prevents quantifier collapse ($\Box$ and $\Diamond$ differ), unlike deterministic ODEs; (ii) modal operators are entropic risk measures, sound with respect to risk-based semantics with explicit Monte Carlo concentration guarantees; (iii)SDE-induced accessibility provides structural correspondence with classical modal axioms; (iv) parameterizing accessibility through dynamics reduces memory from quadratic in world count to linear in parameters.
>   Three case studies demonstrate that Fluid Logic and LINNs can guide neural networks to produce consistent solutions across diverse domains: epistemic/doxastic logic (multi-robot hallucination detection), temporal logic (recovering the Lorenz attractor geometry from logical constraints alone), and deontic logic (learning safe confinement dynamics from a logical specification).

